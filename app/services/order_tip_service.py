#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from app.services.base_service import BaseService, ServiceException
from configs.database_builder import DatabaseBuilder
from app.commons.biz_model import BizModel, Attribute
from app.commons import dateutil
from app.daos.order_tip_dao import OrderTip, OrderTipDao
from app.daos.order_dao import OrderDao
from app.daos.customer_service_order_dao import CustomerServiceOrderDao
from app.daos.customer_service_user_dao import CustomerServiceUserDao


class OrderTipBO(BizModel):
    csu_id = Attribute('')
    stuff_name = Attribute('')
    user_id = Attribute('')
    order_id = Attribute('')
    order_name = Attribute('')
    tip_price = Attribute(0)
    is_paid = Attribute()
    created_at = Attribute('')
    paid_at = Attribute('')


class OrderTipService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get_by_order(self, order_id):
        with self.create_session(self._default_db) as session:
            tip = OrderTipDao(session).get_by_order(order_id)

            tip_bo = OrderTipBO(**tip.fields) if tip else OrderTipBO()
            tip_bo.tip_price = str(tip_bo.tip_price) + '.00'
            return tip_bo

    def count_get_tips(self, offset, count):
        with self.create_session(self._default_db) as session:
            tips = OrderTipDao(session).gets(offset, count)
            if tips:
                tip_bos = []
                for tip in tips:
                    tip_bo = OrderTipBO(**tip.fields)
                    tip_bo.is_paid = '已支付' if tip_bo.is_paid else '未支付'
                    tip_bo.created_at = dateutil.timestamp_to_string(tip_bo.created_at, '%Y-%m-%d %H:%M:%S')
                    tip_bo.paid_at = dateutil.timestamp_to_string(tip_bo.paid_at)
                    tip_bos.append(tip_bo)
                return OrderTipDao(session).count(), tip_bos
            else:
                return 0, tuple()

    def add_order_tip(self, order_bo, tip_price, session):
        """
        添加 打赏的信息
        :param order_id:
        :param tip_price:
        :return:
        """
        order_tip_dao = OrderTipDao(session)
        if tip_price:
            cs_user = CustomerServiceUserDao(session).get_by_csu_id(order_bo.csu_id)
            tip = OrderTip()
            tip.order_id = order_bo.id
            tip.user_id = order_bo.user_id
            tip.tip_price = tip_price
            tip.order_name = order_bo.name
            tip.csu_id = order_bo.csu_id
            tip.stuff_name = cs_user.name
            order_tip_dao.add(tip)

    @staticmethod
    def pay_tip(order_id, user_id, tip_price, session):
        order_tip_dao = OrderTipDao(session)
        tip = order_tip_dao.get_by_order_user_price(order_id, user_id, tip_price)
        if tip:
            tip.is_paid = True
            tip.paid_at = dateutil.timestamp()
            order_tip_dao.update(tip)
