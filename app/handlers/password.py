#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.view_model import ViewModel
from app.daos.account_dao import AccountType
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.commons.validators import REQUIRED, EQUALTO, MAXLENGTH
from app.commons.decoraters_tornado import validators
from app.services.account_service import AccountService
from app.services.sms_code_service import SmsValidType, SmsCodeService
from app.services.user_service import UserService


class PasswordCheckCodeHandler(BaseHandler):

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                })
    def post(self, *args, **kwargs):
        mobile = self.get_argument('mobile', '')
        next_url = self.get_argument('next_url', '/')
        if not self.validation_success:
            self.redirect("/session/new")
            return
        sms_code_service = SmsCodeService()
        sms_code_service.send_sms_code(mobile,
                                       SmsValidType.RESET_PASSWORD,
                                       self.request.remote_ip)
        result = ViewModel(
            country_code='86',
            mobile=mobile,
            next=next_url,
            verification_token='',
        )
        self.render("password/check_code.html", **result)


class PasswordResetHandler(BaseHandler):

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                })
    def put(self, *args, **kwargs):
        """ 跳转到重置密码的显示页面
        """
        if not self.validation_success:
            self.redirect("session/new")
            return

        mobile = self.get_argument('mobile', '')
        verification_token = self.get_argument('verification_token', '')
        next_url = self.get_argument('next_url', '/')
        account_service = AccountService()
        account = account_service.get_account(mobile, AccountType.MOBILE)

        if account is not None:
            result = ViewModel(
                country_code='86',
                mobile=mobile,
                verification_token=verification_token,
                password='',
                password_confirm='',
                next=next_url
            )
            self.render("password/reset.html", **result)
        else:
            # 当前账号不存在或校验不通过跳转到登录页面
            self.redirect("session/new")


class PasswordResetLoginHandler(BaseHandler):

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "password": {REQUIRED: True, MAXLENGTH: 36},
                    "password_confirm": {REQUIRED: True, MAXLENGTH: 36, EQUALTO: "#password"}
                },
                messages=
                {
                    "password_confirm": {EQUALTO: u"密码不一致"}
                })
    def put(self, *args, **kwargs):
        """执行修改密码的操作并且登录
        """
        mobile = self.get_argument('mobile', '')
        verification_token = self.get_argument('verification_token', '')
        validation_code = self.get_argument('validation_code', '')
        password = self.get_argument('password', '')
        password_confirm = self.get_argument('password_confirm', '')
        next_url = self.get_argument('next_url', '/')

        result = ViewModel(country_code='86',
                           mobile=mobile,
                           verification_token=verification_token,
                           password=password,
                           password_confirm=password_confirm,
                           validation_data=self.validation_data,
                           validation_errors=self.validation_errors,
                           next=next_url)

        if not self.validation_success:
            self.render("password/reset.html", **result)
            return

        account_service = AccountService()
        # account_service.change_password_by_verification_token(mobile,
        #                                                       verification_token,
        #                                                       password,
        #                                                       self.request.remote_ip)
        # account = account_service.get_account(mobile, AccountType.MOBILE)

        user_id = account_service.reset_password(password, password_confirm, mobile, self.request.remote_ip)
        user_service = UserService()
        user = user_service.get(user_id)
        self.set_login_token(user, False)
        self.redirect(next_url)


class PasswordCheckCodeAPIHandler(RestfulAPIHandler):
    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "verification_token": {REQUIRED: True},
                    "validation_code": {REQUIRED: True}
                })
    def put(self, *args, **kv):
        """ 检查输入的手机验证码是否正确
        """
        mobile = self.get_argument('mobile', '')
        validation_code = self.get_argument('validation_code', '')
        sms_code_service = SmsCodeService()
        sms_code_service.validate_sms_code(mobile, SmsValidType.RESET_PASSWORD,
                                           validation_code, self.request.remote_ip)
        self.write_success()


class PasswordSendSmsMsgAPIHandler(RestfulAPIHandler):

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "verification_token": {REQUIRED: True}
                })
    def put(self, *args, **kv):
        """ 重新发送手机验证码
        """
        mobile = self.get_argument('mobile', '')
        verification_token = self.get_argument('verification_token', '')
        account_service = AccountService()
        account_service.resend_verification_code(mobile, verification_token,
                                                 SmsValidType.RESET_PASSWORD, self.request.remote_ip)
        self.write_success()