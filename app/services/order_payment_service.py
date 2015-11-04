#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'

from app.commons import dateutil
from app.services.base_service import BaseService, ServiceException
from app.commons.biz_model import BizModel, Attribute
from configs.database_builder import DatabaseBuilder
from app.services.order_service import OrderService, OrderDao, OrderBO
from app.daos.order_payment_dao import OrderPayment, OrderPaymentDao
from app.services.order_tip_service import OrderTipService
from app.services.order_status_service import OrderStatusService, OrderStatusMap
from configs.order_status_map import OrderStatusMap
from app.services.applicant_service import ApplicantService


class OrderPaymentBO(BizModel):
    id = Attribute('')
    out_trade_no = Attribute(None)
    pay_mode = Attribute(None)
    pay_fee = Attribute(None)
    service_charge = Attribute(0)
    official_charge = Attribute(0)
    tax = Attribute(0)
    order_tip = Attribute(0)
    pay_config = Attribute(None)
    buyer_account = Attribute(None)
    order_id = Attribute(None)
    is_paid = Attribute(0)
    is_refund = Attribute(0)
    payment_time = Attribute('')
    updated_date = Attribute('')


class OrderPaymentService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get_by_order(self, order_id):
        with self.create_session(self._default_db) as session:
            order_payment_dao = OrderPaymentDao(session)
            order_payment = order_payment_dao.get_by_order_id(order_id)
            if order_payment:
                order_payment_bo = OrderPaymentBO(**order_payment.fields)
                return order_payment_bo

    def add_payment(self, order, order_tip, business_bo, is_invoice):
        with self.create_session(self._default_db) as session:
            if isinstance(order, OrderBO):
                order_bo = order
            else:
                order_obj = OrderDao(session).get(order)
                order_bo = OrderBO(**order_obj.fields)
            payment = self._add_payment(order_bo, order_tip, business_bo, is_invoice, session)
            return payment.id

    def parse_offline_payment(self, order_id, business_bo, is_invoice, p_info):
        with self.create_session(self._default_db) as session:
            order_service = OrderService()
            order_service.initialize_operator_by_id(order_id, session)
            order_bo = OrderBO(**order_service.order.fields)
            payment = self._add_payment(order_bo, 0, business_bo, is_invoice, session)
            # 根据当前业务信息，计算应付款
            due_price = business_bo.official_charge + business_bo.service_charge
            if is_invoice and not business_bo.service_charge:
                due_price += (business_bo.official_charge + business_bo.service_charge) * business_bo.tax
            # 实付款不小于应付款时，付款成功
            if float(due_price) <= float(p_info['pay_fee']):
                for field in ('pay_mode', 'buyer_account', 'payment_time', 'pay_config', 'out_trade_no'):
                    setattr(payment, field, p_info.get(field, ''))

                payment.is_paid = True
                payment.pay_fee = due_price

                order_service.pay_deal(order_id, payment, session)

                message = '付款成功，'
            else:
                message = '付款失败，还需补交%s元' % (float(due_price) - float(p_info['pay_fee']))
            return message + '实付款:%s, 应付款:%s，官费：%s，服务费：%s, 税费：%s' %\
                             (p_info['pay_fee'], due_price, float(business_bo.official_charge), float(business_bo.service_charge),
                              float((business_bo.official_charge + business_bo.service_charge) * business_bo.tax))

    def _add_payment(self, order_bo, order_tip, business_bo, is_invoice, session):
        order_id = order_bo.id
        order_payment_dao = OrderPaymentDao(session)
        order_payment = order_payment_dao.get_by_order_id(order_id)
        if order_payment:
            if order_payment.is_paid:
                raise ServiceException(20085, 'this order has paid')
            else:
                # 更新之前的支付信息
                for field in ('service_charge', 'official_charge'):
                    setattr(order_payment, field, getattr(business_bo, field))
                if int(is_invoice):
                    order_payment.tax = business_bo.tax
                order_payment.order_tip = order_tip
                order_payment_dao.update(order_payment)
                return order_payment
        else:
            payment = self._create_new_payment(order_id, order_tip, business_bo, is_invoice, order_payment_dao)
            # 如果有打赏金额，添加打赏的信息
            if order_tip:
                OrderTipService().add_order_tip(order_bo, order_tip, session)
            return payment

    @staticmethod
    def _create_new_payment(order_id, order_tip, business_bo, is_invoice, order_payment_dao):
        payment = OrderPayment()
        for field in ('service_charge', 'official_charge'):
            setattr(payment, field, getattr(business_bo, field))
        if int(is_invoice):
            payment.tax = business_bo.tax
        payment.order_id = order_id
        payment.order_tip = order_tip
        payment = order_payment_dao.add(payment)
        return payment

    def pay_order(self, payment_bo):
        """
        付款后更新订单状态， 修改对应的业务 is_paid 状态
        :param payment_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            order_payment_dao = OrderPaymentDao(session)
            payment = order_payment_dao.get(payment_bo.id)
            if payment and not payment.is_paid:
                # 更新支付信息
                for field in ('pay_mode', 'buyer_account', 'payment_time', 'pay_config', 'out_trade_no'):
                    setattr(payment, field, getattr(payment_bo, field, ''))
                payment.is_paid = True
                payment.pay_fee = payment_bo.pay_fee

                order_payment_dao.update(payment)

                order_id = payment.order_id
                order_service = OrderService()
                order_service.pay_deal(payment.trand_no, payment, session)

                return order_id

    # @staticmethod
    # def update_order_biz(order, payment_bo, session):
    #     # 更新订单信息
    #     order.status = OrderStatusMap.PAID
    #     order.is_paid = True
    #     if bool(payment_bo.service_charge + payment_bo.tax):
    #         order.is_invoice_able = True
    #     # 更新订单价格，确保再发票索取部分不会出现乌龙事件
    #     order.price = float(payment_bo.pay_fee) - float(payment_bo.order_tip)
    #
    #     # 更新业务信息
    #     biz_service = OrderService.get_detail_service(order.order_type)
    #     biz_dao = biz_service.get_biz_dao(session)
    #     biz_obj = biz_dao.get_by_order(order.id)
    #     biz_obj.is_paid = True
    #     biz_dao.update(biz_obj)
    #     OrderStatusService().update_order_status(order, OrderStatusMap.PAID, 0, session)
    #     biz_service.detail_pay(order, session)
    #     return order, biz_service



