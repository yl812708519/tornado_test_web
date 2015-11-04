#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlencode
from app.commons.decoraters_tornado import validators
from app.commons.validators import REQUIRED, MAXLENGTH, EQUALTO, MINLENGTH, EMAIL
from app.commons.view_model import ViewModel
from app.daos.account_dao import AccountType

from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.account_service import AccountService
from app.services.base_service import ServiceException
from app.services.sms_code_service import SmsCodeService, SmsValidType
from app.services.user_service import UserService, UserProfileBO
from configs.settings import Settings


class SignUpHandler(BaseHandler):
    def get(self, *args):
        """获取注册页面

        :param args:
        """
        result = dict(title='注册',
                      validation_data=dict(),
                      next=self.get_argument('next', '/'),
                      next_url=urlencode({'next': self.get_argument('next', '/')}))
        self.render('signup/signup.html', **result)

    @validators(rules={"mobile": {REQUIRED: True},
                       "validate_code": {REQUIRED: True, MINLENGTH: 6, MAXLENGTH: 6},
                       "nickname": {REQUIRED: True},
                       "password": {REQUIRED: True, MAXLENGTH: 20},
                       "password_confirm": {REQUIRED: True, MAXLENGTH: 36, EQUALTO: "#password"}
                       },
                messages={"mobile": {REQUIRED: u'手机不能为空'},
                          "validate_code": {REQUIRED: u'验证码不为空',
                                            MINLENGTH: u'验证码长度必须是6位',
                                            MAXLENGTH: u'验证码长度必须是6位'},
                          "nickname": {REQUIRED: u"姓名不能为空"},
                          "password": {REQUIRED: u'密码不能为空', MAXLENGTH: u'长度不能超过20位'},
                          "password_confirm": {EQUALTO: u"密码不一致"}
                          }
                )
    def post(self):
        """提交注册信息


        """
        email = self.get_argument('email', '')
        mobile = self.get_argument('mobile', '')
        pwd = self.get_argument('password', '')
        next_url = self.get_argument('next_url', '/')
        validation_code = self.get_argument('validate_code', '')
        nickname = self.get_argument('nickname', '')

        if self.validation_errors:
            self.render('signup/signup.html', **{'validation_errors': self.validation_errors,
                                                 'validation_data': self.validation_data})
        else:
            # 创建account user
            account_service = AccountService()
            account = account_service.is_exist_user(mobile=mobile, email=email)
            sms_code_service = SmsCodeService()
            sms_code_service.validate_sms_code(mobile, SmsValidType.SIGNUP,
                                               validation_code, self.request.remote_ip)
            if account is False:
                accounts = dict(mobile=mobile,
                                email=email)
                account_service = AccountService()
                user_id = account_service.add_account(accounts, pwd, self.request.remote_ip, nickname)
                user_service = UserService()
                user = user_service.get(user_id)
                self.set_login_token(user, False)
                self.redirect(next_url)
            else:
                self.redirect("/session/new")


class SignUpCheckMobileHandler(BaseHandler):
    def put(self, *args, **kwargs):
        mobile = self.get_argument('mobile', '')
        account_service = AccountService()
        if account_service.is_exist_account(mobile, AccountType.MOBILE):
            # 当前的手机对应的账号已经存在，跳转到登录页面
            self.redirect(Settings.LOGIN_URL)
            return

        # 当前的手机对应的账号不存在，发送短信验证码
        sms_code_service = SmsCodeService()
        sms_code_service.send_sms_code_for_account_name(mobile, SmsValidType.SIGNUP,
                                                        self.request.remote_ip)
        result = ViewModel(
            step='check_code',
            country_code='86',
            mobile=mobile
        )
        self.render("signup/check_code.html", **result)


class SignUpCheckCodeHandler(BaseHandler):
    def put(self, *args, **kwargs):
        mobile = self.get_argument('mobile', '')
        verification_token = self.get_argument('verification_token', '')
        account_service = AccountService()
        account = account_service.get_account(mobile, Avalidate_codeccountType.MOBILE)
        sms_code_service = SmsCodeService()
        sms_code_service.validate_sms_code(mobile, SmsValidType.SIGNUP,
                                           verification_token, self.request.remote_ip)
        if account is None:
            result = ViewModel(
                step='set_password',
                country_code='86',
                mobile=mobile,
                verification_token=verification_token,
                password='',
                password_confirm=''
            )
            self.render("signup/password.html", **result)
        else:
            self.redirect("session/new")


class SignUpPasswordHandler(BaseHandler):
    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "verification_token": {REQUIRED: True},
                    "password": {REQUIRED: True, MAXLENGTH: 36},
                    "password_confirm": {REQUIRED: True, MAXLENGTH: 36, EQUALTO: "#password"}
                },
                messages=
                {
                    "password_confirm":  {EQUALTO: u"密码不一致"}
                })
    def put(self, *args, **kwargs):
        mobile = self.get_argument('mobile', '')
        result = self.validation_data
        result.update(step='set_password')

        if not self.validation_success:
            self.render("signup/password.html", validation_errors=self.validation_errors, **result)
            return

        account_service = AccountService()
        account = account_service.get_account(mobile, AccountType.MOBILE)
        sms_code_service = SmsCodeService()
        sms_code_service.validate_sms_code(mobile, SmsValidType.SIGNUP,
                                           result.verification_token, self.request.remote_ip)
        if account is None:
            account_service = AccountService()
            account = account_service.add_account(mobile, result.password, self.request.remote_ip)
            user_service = UserService()
            user = user_service.get(account.user_id)
            self.set_login_token(user, False)
            # TODO: 设置用户登录成功跳转到主页面
            self.redirect("/")
        else:
            self.redirect("/session/new")


class SignUpSendSmsMsgAPIHandler(RestfulAPIHandler):

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "verification_token": {REQUIRED: True}
                })
    def put(self, *args, **kv):
        mobile = self.get_argument('mobile', '')
        verification_token = self.get_argument('verification_token', '')
        account_service = AccountService()
        account_service.resend_verification_code(mobile, verification_token,
                                                 SmsValidType.SIGNUP, self.request.remote_ip)
        self.write_success()


class SignUpAPIHandler(RestfulAPIHandler):

    def post(self, *args, **kwargs):
        step = self.get_argument('step', 'check_mobile')
        if step == 'check_mobile':
            self._check_mobile()
        elif step == 'check_email':
            self._check_email()
        elif step == 'check_code':
            self._check_code()

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                },
                messages=
                {
                    "mobile":  {REQUIRED: u"请输入手机号"}
                })
    def _check_mobile(self):
        mobile = self.get_argument('mobile', None)
        if self.validation_errors:
            self.write(self.validation_errors)
            # {'country_code': u'\u5fc5\u9009\u5b57\u6bb5'}
            # 此处应该把错误写到页面
            return
        sms_code_service = SmsCodeService()
        account_service = AccountService()
        # 验证该手机号有没有注册过
        try:
            account_service.send_sms_code_for_signup(mobile, self.request.remote_ip)
            result = dict(mobile=mobile,
                          status=1)
            self.write(result)
        except Exception, e:
            self.write_except(e)

    def _check_email(self):
        email = self.get_argument('email', '')
        try:
            # 验证邮箱是否重复
            acc_service = AccountService()
            if acc_service.get_account(AccountType.EMAIL, email) is not None:
                raise ServiceException(20001, 'this email has register')
            self.write_success()
        except Exception, e:
            self.write_except(e)

    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                    "country_code": {REQUIRED: True},
                    "verification_token": {REQUIRED: True},
                    "validation_code": {REQUIRED: True, MAXLENGTH: 6, MINLENGTH: 6}
                })
    def _check_code(self):
        mobile = self.get_argument('mobile', '')
        validation_code = self.get_argument('validate_code', '')
        try:
            sms_code_service = SmsCodeService()
            sms_code_service.validate_sms_code(mobile, 'SIGNUP',
                                               validation_code, self.request.remote_ip)
            self.write_success()
        except Exception, e:
            self.write_except(e)