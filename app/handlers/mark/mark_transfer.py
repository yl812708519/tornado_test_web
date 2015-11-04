#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated, HTTPError
from app.handlers.application import RestfulAPIHandler
from app.services.ban_bos.mark_bo.mark_transfer_bo import MarkTransferInfoBO, MarkTransferMainBO, MarkTransferCommonBO
from app.services.mark_transfer_service import MarkTransferService


class MarkTrasferApplicantHandler(RestfulAPIHandler):
    """
    商标转让服务，转让人受让人、申请人的主题信息修改
    """

    @authenticated
    def post(self):
        """
        修改 转让主体，受让主体，申请主体(补发申请时的)
        :return:
        """
        user = self.current_user
        mark_service = MarkTransferService()
        mark_bo = self.get_req_bo(MarkTransferInfoBO)
        mark_service.update_applicant(user.user_id, mark_bo)
        # 转让人和受让人不能相同
        if mark_bo.biz == 'mark_transfer_apply' and mark_bo.acceptor_app_id == mark_bo.transfer_app_id:
            raise HTTPError(400)
        self.write_success()


class MarkTrasferBizHandler(RestfulAPIHandler):
    """
    商标转让服务，转让人受让人、申请人的主题信息修改
    """

    @authenticated
    def post(self):
        """
        修改 转让主体，受让主体，申请主体(补发申请时的)
        :return:
        """
        user = self.current_user
        mark_service = MarkTransferService()
        mark_bo = self.get_req_bo(MarkTransferMainBO)

        mark_service.update_biz_info(user.user_id, mark_bo)
        self.write_success()


class MarkTransferCommonHandler(RestfulAPIHandler):
    """
    处理商标转让业务的商标共有人和受让共有人
    """

    @authenticated
    def post(self):
        """
        修改 转让主体，受让主体，申请主体(补发申请时的)
        :return:
        """
        user = self.current_user
        mark_service = MarkTransferService()
        mark_bo = self.get_req_bo(MarkTransferCommonBO)

        mark_service.update_co_apps(user.user_id, mark_bo)
        self.write_success()
