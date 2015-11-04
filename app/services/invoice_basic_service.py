#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.ban_bos.invoice_basic import InvoiceBasicBO
from app.services.base_service import BaseService
from app.daos.invoice_basic_dao import InvoiceBasicDao, InvoiceBasic
from app.services.oss_upload_service import OssUploadService
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'


class InvoiceBasicService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def get_value_by_status_and_type(get_type, value):
        d = {'make_invoice_type': {"person": '个人', "com": '企业'},
             'invoice_type': {"normal": "增值税普通发票", "special": "增值税专用发票"}}

        return d[get_type][value]

    def get_by_id(self, invoice_basic_id):
        """根据 invoice_basic_id 查询单条记录

        :param invoice_basic_id:invoice_basic_id表 id
        :return: invoice_basic 表中单条记录
        """
        with self.create_session(self._default_db) as session:
            invoice_basic_dao = InvoiceBasicDao(session)
            invoice_basic = invoice_basic_dao.get(invoice_basic_id)
            return InvoiceBasicBO(**invoice_basic.fields) if invoice_basic else None

    def get_by_uid(self, user_id):
        """根据 user_id 查询单条记录

        :param user_id:user_id
        :return: invoice_basic 表中单条记录
        """
        with self.create_session(self._default_db) as session:
            invoice_basic_dao = InvoiceBasicDao(session)
            invoice_basic = invoice_basic_dao.get_by_uid(user_id)
            return InvoiceBasicBO(**invoice_basic.fields) if invoice_basic else None

    def add(self, invoice_basic_bo):
        """添加发票管理信息

        :param invoice_basic_bo
        """
        with self.create_session(self._default_db) as session:
            invoice_basic_dao = InvoiceBasicDao(session)
            invoice_basic = InvoiceBasic()
            invoice_basic.update(invoice_basic_bo.attributes)
            return invoice_basic_dao.add(invoice_basic)

    def update(self, req_bo):
        """更新发票管理信息

        :param invoice_basic_bo
        """
        with self.create_session(self._default_db) as session:
            invoice_basic_dao = InvoiceBasicDao(session)
            invoice_basic = invoice_basic_dao.get(req_bo.id)
            invoice_basic.update(req_bo.flat_attributes)
            return invoice_basic_dao.update(invoice_basic)

    @staticmethod
    def get_full_path(tail_path):
        head_path = OssUploadService().download_image_site()
        return head_path + tail_path if tail_path else ''

    def add_full_path(self, bo):
        bo.download_certi_img_url = self.get_full_path(bo.certi_img)
        bo.download_tax_certi_img_url = self.get_full_path(bo.tax_certi_img)
        bo.download_taxpayer_certi_img_url = self.get_full_path(bo.taxpayer_certi_img)
        return bo
