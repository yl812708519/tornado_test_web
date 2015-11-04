#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib import urlencode
from app.commons import dateutil
from app.commons.decoraters_tornado import validators

from app.commons.validators import REQUIRED
from app.commons.view_model import ViewModel
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.account_service import AccountService
from app.services.base_service import ServiceException
from configs.errors import Errors


class SessionNewHandler(BaseHandler):
    def get(self, *args):

        result = ViewModel(
            title=u'登录',
            country_code='86',
            mobile='',
            password='',
            captcha='',
            show_captcha=False,
            next=self.get_argument('next', '/'),
            next_url=urlencode({'next': self.get_argument('next', '/')})
        )
        self.render("session/new.html", **result)


class AccountCheckAPIHandler(RestfulAPIHandler):
    @validators(rules=
                {
                    "mobile": {REQUIRED: True},
                })
    def post(self, *args):
        mobile = self.get_argument('mobile', '')
        account_service = AccountService()
        account = account_service.get_account_by_mobile(mobile)
        if account is not None:
            self.write_success()
        else:
            self.write_except(ServiceException(20004, 'the account is not exist'))


class SessionHandler(BaseHandler):

    def delete(self, *args, **kwargs):
        """ 退出登录

        :param args:
        :param kwargs:
        :return:
        """
        self.logout()
        self.redirect('/')

    @validators(rules=
                {
                    # "country_code": {REQUIRED: True},
                    "mobile": {REQUIRED: True},
                    "password": {REQUIRED: True}
                },
                messages=
                {
                    # "country_code": {REQUIRED: u'国家编号不能为空'},
                    "mobile": {REQUIRED: u'手机号码不能为空'},
                    "password": {REQUIRED: u'密码不能为空'}
                })
    def post(self, *args, **kwargs):
        # 下次进入是否自动登录
        is_auto_login = ('on' == self.get_argument('remember', None))
        captcha = self.get_argument('captcha', u'')
        next_url = self.get_argument('next_url', '/')
        result = ViewModel(
            country_code=self.get_argument('country_code', u'86'),
            mobile=self.get_argument('mobile', u''),
            password=self.get_argument('password', u''),
            captcha='',
            show_captcha=False,
            t=dateutil.timestamp(),
            next=next_url,
            next_url=urlencode({'next': self.get_argument('next', '/')})
        )
        if self.validation_success:
            # 校验通过
            account_service = AccountService()
            try:
                user_bo = account_service.authenticate(result.mobile, result.password,
                                                       self.request.remote_ip, captcha)
                if is_auto_login:
                    self.set_login_token(user_bo, True)
                else:
                    self.set_login_token(user_bo, False)
                self.redirect(next_url)
                return
            except ServiceException as e:
                if e.code >= 20005:
                    result.show_captcha = True
                if e.code in [20008, 20009]:
                    self.validation_errors = dict(captcha=Errors.error_message(e.code))
                else:
                    self.validation_errors = dict(password=Errors.error_message(e.code))
                self.render("session/new.html", title=u'登录', validation_errors=self.validation_errors, **result)
        else:
            # 校验失败
            self.render("session/new.html", title=u'登录', validation_errors=self.validation_errors, **result)
