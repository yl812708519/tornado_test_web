#! /usr/env python
# coding:utf-8

import json
from tornado.web import authenticated
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.ban_bos.copyright_opus import CopyrightOpusOrderApplicantReqBO, \
    CopyrightOpusOrderInfoReqBO, CopyrightOpusOrderAttReqBO
from app.services.copyright_opus_service import CopyrightOpusOrderService
from app.services.oss_upload_service import OssUploadService

__author__ = 'zhaowenlei'


class CopyrightOpusOrderApplicantHandler(RestfulAPIHandler):

    @authenticated
    def post(self):
        """修改主体信息

        :return:
        :rtype:
        """
        req_bo = self.get_req_bo(CopyrightOpusOrderApplicantReqBO)
        req_bo.user_id = self.current_user.user_id
        copyright_opus_order_service = CopyrightOpusOrderService()
        copyright_opus_order_service.update_applicant(req_bo)


class CopyrightOpusOrderInfoHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        """文字版权基本信息提交

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        req_bo = self.get_req_bo(CopyrightOpusOrderInfoReqBO, need_validate=False)
        self.validate(req_bo, is_raise_all=True)
        copyright_opus_order_service = CopyrightOpusOrderService()
        req_bo.user_id = self.current_user.user_id
        # img_url = OssUploadService().download_image_site('yestar')
        copyright_opus_order_service.update_info(req_bo)


class CopyrightOpusOrderAttaHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        """文字版权附加信息提交

        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        req_bo = self.get_req_bo(CopyrightOpusOrderAttReqBO, need_validate=False)
        self.validate(req_bo, is_raise_all=True)
        copyright_opus_order_service = CopyrightOpusOrderService()
        req_bo.user_id = self.current_user.user_id
        copyright_opus_order_service.update_att(req_bo)