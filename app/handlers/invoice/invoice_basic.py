#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import authenticated

from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.ban_bos.invoice_basic import InvoiceReqBo
from app.services.invoice_basic_service import InvoiceBasicBO, InvoiceBasicService
from app.services.oss_upload_service import OssUploadService

__author__ = 'zhaowenlei'


class InvoiceBasicNewHandler(BaseHandler):

    @authenticated
    def get(self, invoice_basic_id=None, *args, **kwargs):
        """获取发票信息管理填加页面

        """
        user_id = self.current_user.user_id
        invoice_basic_service = InvoiceBasicService()
        has_user = invoice_basic_service.get_by_uid(user_id)
        invoice_basic_bo = InvoiceBasicBO()
        if invoice_basic_id is not None and has_user is not None:
            invoice_basic_bo = invoice_basic_service.get_by_id(invoice_basic_id)
            invoice_basic_bo = invoice_basic_service.add_full_path(invoice_basic_bo)
        if invoice_basic_id is None and has_user is not None:
            self.send_error(405)
            return
        if invoice_basic_id is not None and has_user is None:
            self.send_error(405)
            return
        result = dict(invoice_basic=invoice_basic_bo,
                      active_id='invoice_basic',
                      downloadurl=OssUploadService().download_image_site())
        self.render("ban_views/invoice/invoice_basic.html", **result)


class InvoiceBasicSubmitHandler(RestfulAPIHandler):

    def get_bo(self):
        req_bo = self.get_req_bo(InvoiceReqBo, need_validate=False)
        self.validate(req_bo, is_raise_all=True)
        return req_bo

    @authenticated
    def post(self, *args, **kwargs):
        """提交发票管理信息

        :param args:
        :param kwargs:
        """
        req_bo = self.get_bo()
        req_bo.user_id = self.current_user.user_id
        invoice_basic_service = InvoiceBasicService()
        invoice_basic_service.add(req_bo)

    @authenticated
    def put(self, *args, **kwargs):
        """修改发票管理信息

        :param args:
        :param kwargs:
        """
        req_bo = self.get_bo()
        req_bo.user_id = self.current_user.user_id
        invoice_basic_service = InvoiceBasicService()
        invoice_basic_service.update(req_bo)

class InvoiceBasicDetailHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        """获取发票信息管理详情页面

        :param args:
        :param kwargs:
        """
        user_id = self.current_user.user_id
        invoice_basic_service = InvoiceBasicService()
        invoice_basic_bo = invoice_basic_service.get_by_uid(user_id)
        if invoice_basic_bo.invoice_type:
            invoice_basic_bo.invoice_type_temp = invoice_basic_service.get_value_by_status_and_type('invoice_type',
                                                                                                    invoice_basic_bo.invoice_type)
        if invoice_basic_bo.make_invoice_type:
            invoice_basic_bo.make_invoice_type_temp = invoice_basic_service.get_value_by_status_and_type('make_invoice_type',
                                                                                                         invoice_basic_bo.make_invoice_type)
        invoice_basic_bo = invoice_basic_service.add_full_path(invoice_basic_bo)
        result = dict(invoice_basic=invoice_basic_bo,
                      active_id='invoice_basic')
        self.render('ban_views/invoice/invoice_basic_detail.html', **result)