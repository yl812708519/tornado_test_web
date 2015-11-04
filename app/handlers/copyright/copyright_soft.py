#! /usr/env python
# coding:utf-8
from tornado.web import authenticated

from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.ban_bos.copyright_soft import CopyrightSoftOrderApplicantReqBO, CopyrightSoftOrderInfoReqBO, CopyrightSoftOrderFeatureReqBO, \
    CopyrightSoftOrderAttachReqBO
from app.services.copyright_soft_service import CopyrightSoftOrderService

__author__ = 'zhaowenlei'


class CopyrightSoftOrderApplicantHandler(RestfulAPIHandler):

    @authenticated
    def post(self):
        """修改主体信息

        :return:
        :rtype:
        """
        req_bo = self.get_req_bo(CopyrightSoftOrderApplicantReqBO)
        req_bo.user_id = self.current_user.user_id
        copyright_soft_order_service = CopyrightSoftOrderService()
        copyright_soft_order_service.update_applicant(req_bo)


class CopyrightSoftOrderInfoHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        req_bo = self.get_req_bo(CopyrightSoftOrderInfoReqBO, need_validate=False)
        self.validate(req_bo, is_raise_all=True)
        req_bo.user_id = self.current_user.user_id
        copyright_soft_order_service = CopyrightSoftOrderService()
        copyright_soft_order_service.update_info(req_bo)


class CopyrightSoftOrderFeatureHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        req_bo = self.get_req_bo(CopyrightSoftOrderFeatureReqBO, need_validate=False)
        self.validate(req_bo, is_raise_all=True)
        req_bo.user_id = self.current_user.user_id
        copyright_soft_order_service = CopyrightSoftOrderService()
        copyright_soft_order_service.update_feature(req_bo)


class CopyrightSoftOrderAttachHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        req_bo = self.get_req_bo(CopyrightSoftOrderAttachReqBO)
        req_bo.user_id = self.current_user.user_id
        copyright_soft_order_service = CopyrightSoftOrderService()
        copyright_soft_order_service.update_attach(req_bo)



