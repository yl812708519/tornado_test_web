#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated
from app.handlers.application import RestfulAPIHandler
from app.services.mark_reg_apply_service import MarkRegApplyService
from app.services.ban_bos.mark_bo.mark_apply_bo import MarkApplyInfoBO, MarkApplyMainBO


class MarkRegApplyinfoHandler(RestfulAPIHandler):
    """
    商标注册 其他的服务（注册证补发申请，商标注册证明申请，更正商标申请）
    """
    @authenticated
    def post(self, *args, **kwargs):
        """
        更新 申请人信息
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        mark_apply_bo = self.get_req_bo(MarkApplyInfoBO)
        MarkRegApplyService().update_apply_info(mark_apply_bo, user.user_id)
        self.write_success()


class MarkRegApplyMainHandler(RestfulAPIHandler):
    """
    注册证补发申请，商标注册证明申请，更正商标申请 各自的主要业务信息 的表单获取 和 录入
    """

    @authenticated
    def post(self, *args, **kwargs):
        """
        修改数据
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        mark_bo = self.get_req_bo(MarkApplyMainBO)
        MarkRegApplyService().update_apply_main(mark_bo, user.user_id, mark_bo.biz)
        self.write_success()
