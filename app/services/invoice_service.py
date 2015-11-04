#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from app.services.ban_bos.invoice import InvoiceReqBO
from app.services.base_service import BaseService, ServiceException
from app.commons.biz_model import BizModel, Attribute
from app.daos.invoice_dao import InvoiceDao, Invoice
from app.daos.order_dao import OrderDao
from app.services.delivery_address_service import DeliveryAddressService
from app.services.invoice_order_service import InvoiceOrderBO, InvoiceOrderService
from app.services.order_service import OrderBO, OrderService
from configs.database_builder import DatabaseBuilder


__author__ = 'zhaowenlei'


class InvoiceService(BaseService):
    
    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def get_by_type(type_value):
        d = {'mark_reg': '商标注册', 'mark_transfer_apply': '商标转让',
             'age_rec_applicant': '商标变更', 'sub_service_applicant': '商标变更',
             'reg_col_pro_applicant': '商标变更', 'reissue_mark_transfer': '商标转让'}

        return d[type_value]

    def gets_order_by_ids(self, ids):
        """方法

        :param applicant_bo:applicant表 BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            orders = order_dao.gets_by_ids(ids)
            return [OrderBO(**order.fields) for order in orders]

    def get_by_id(self, invoice_id, user_id):
        """获取单条记录

        :param invoice_id:
        :param user_id:
        """
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceDao(session)
            invoice = invoice_dao.get_by_id(invoice_id, user_id)
            return InvoiceReqBO(**invoice.fields)

    def add(self, invoice_bo):
        """添加发票

        :param invoice_bo: BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceDao(session)
            invoice = Invoice()
            invoice.update(invoice_bo.attributes)
            return InvoiceReqBO(**(invoice_dao.add(invoice)).fields)

    def add_invoice(self, req_bo):
        req_bo.order_ids = eval(req_bo.order_ids)
        order_ids = [int(order_id) for order_id in req_bo.order_ids]
        order_service = OrderService()
        order_bos = order_service.gets_by_ids_user(order_ids, req_bo.user_id)
        for order_bo in order_bos:
            if order_bo.is_invoiced is True:
                raise ServiceException(20091, 'This order has already been invoiced')
        order_total_price = sum([order_bo.price for order_bo in order_bos])
        if order_total_price != float(req_bo.invoice_price):
            # 前台传过来的金额存在错误，无法完成请求
            raise ServiceException(20092, 'Choose the wrong amount')
        # 重新取出有效的订单id，防止前端伪造数据
        order_ids = [order_bo.id for order_bo in order_bos]
        delivery_address_service = DeliveryAddressService()
        delivery_address_bo = delivery_address_service.get_by_id(req_bo.delivery_address_id)
        req_bo.recipient = delivery_address_bo.name
        req_bo.contact_mobile = delivery_address_bo.mobile
        req_bo.postalcode = delivery_address_bo.postalcode
        req_bo.delivery_address = delivery_address_bo.address

        result_invoice = self.add(req_bo)
        if result_invoice:
            order_service.update_invoiced_by_ids(order_ids)
        invoice_order_bos = []
        for order_id in order_ids:
            invoice_order_bo = InvoiceOrderBO()
            invoice_order_bo.invoice_id = result_invoice.id
            invoice_order_bo.order_id = order_id
            invoice_order_bos.append(invoice_order_bo)

        invoice_order_service = InvoiceOrderService()
        invoice_order_service.add_all(invoice_order_bos)

    def count_by_user_id(self, user_id, start_time='', end_time='', mailing_status='', invoice_status='',
                         offset=0, page_size=10):
        """获取发票列表

        :param invoice_bo: BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceDao(session)
            total, invoices = invoice_dao.count_by_user_id(user_id, start_time, end_time, mailing_status,
                                                           invoice_status, offset, page_size)
            invoice_bos = [InvoiceReqBO(**invoice.fields) for invoice in invoices]
            return dict(total=total,
                        invoice_bos=invoice_bos)

    def gets_by_user_price_date_invoice_able(self, user_id, start_date='', end_date='', start_price='', end_price='',
                                             offset=0, page_size=10):
        """获取索取发票列表

        :param invoice_bo: BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            total, orders = order_dao.gets_by_user_price_date_invoice_able(user_id, start_date, end_date, start_price,
                                                                           end_price, offset, page_size)
            order_bos = [OrderBO(**order.fields) for order in orders]
            return dict(total=total,
                        order_bos=order_bos)

    def update_invoice_by_id(self, invoice_id, user_id):
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceDao(session)
            return invoice_dao.update_invoice_by_id(invoice_id, user_id)
