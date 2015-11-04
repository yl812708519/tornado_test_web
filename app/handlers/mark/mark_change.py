#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from app.handlers.application import RestfulAPIHandler
from app.services.ban_bos.mark_bo.mark_change_bo import MarkChangeInfoBO, MarkChangeAttachBO, MarkChangeApplicantBO
from app.services.mark_change_service import MarkChangeOrderService


__author__ = 'zhaowenlei'


class MarkChangeApplicantJsonHandler(RestfulAPIHandler):

    @authenticated
    def post(self):
        """
        修改主体信息
        """
        user_id = self.current_user.user_id
        mark_bo = self.get_req_bo(MarkChangeApplicantBO)
        mark_change_order_service = MarkChangeOrderService()
        mark_change_order_service.update_applicant(mark_bo, user_id)
        self.write_success()


class MarkChangeInfoJsonHandler(RestfulAPIHandler):

    @authenticated
    def post(self, *args, **kwargs):
        user_id = self.current_user.user_id
        mark_change_service = MarkChangeOrderService()
        mark_bo = self.get_req_bo(MarkChangeInfoBO)
        mark_change_service.update_info(user_id, mark_bo)
        self.write_success()


class MarkChangeAttachHandler(RestfulAPIHandler):

    @authenticated
    def post(self, *args, **kwargs):
        user = self.current_user
        mark_bo = self.get_req_bo(MarkChangeAttachBO)
        mark_change_service = MarkChangeOrderService()
        mark_change_service.update_attach(user.user_id, mark_bo)
        self.write_success()

