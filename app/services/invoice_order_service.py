#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.base_service import BaseService
from app.commons.biz_model import Attribute, BizModel
from app.daos.invoice_order_dao import InvoiceOrderDao, InvoiceOrder
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'


class InvoiceOrderBO(BizModel):

    id = Attribute(None)
    invoice_id = Attribute(None)
    order_id = Attribute(None)
    created_at = Attribute('')


class InvoiceOrderService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def add(self, invoice_order_bo):
        """添加

        :param invoice_bo: BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceOrderDao(session)
            invoice_order = InvoiceOrder()
            invoice_order.update(invoice_order_bo)
            return invoice_dao.add(invoice_order)

    def add_all(self, invoice_order_bos):
        """添加

        :param invoice_bo: BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            invoice_dao = InvoiceOrderDao(session)
            invoice_orders = []
            for invoice_order_bo in invoice_order_bos:
                invoice_order = InvoiceOrder()
                invoice_order.update(invoice_order_bo.attributes)
                invoice_orders.append(invoice_order)
            return invoice_dao.add_all(invoice_orders)

    def gets_by_invoice_id(self, invoice_id):
        """根据 invoice_basic_id 查询单条记录

        :param invoice_basic_id:invoice_basic_id表 id
        :return: invoice_basic 表中单条记录
        """
        with self.create_session(self._default_db) as session:
            invoice_order_dao = InvoiceOrderDao(session)
            invoice_orders = invoice_order_dao.gets_by_invoice_id(invoice_id)
            return [InvoiceOrderBO(**invoice_order.fields) for invoice_order in invoice_orders]