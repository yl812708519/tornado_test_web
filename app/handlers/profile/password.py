#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import authenticated

from app.commons.decoraters_tornado import validators
from app.commons.validators import REQUIRED, MAXLENGTH, EQUALTO
from app.commons.view_model import ViewModel
from app.services.account_service import AccountService
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.base_service import ServiceException
from configs.errors import Errors


__author__ = 'freeway'


class PasswordChangeHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        result = ViewModel(password='',
                           new_password='',
                           new_password_confirm='')
        self.render("password/password_change.html", **result)

    @validators(rules=
                {
                    "password": {REQUIRED: True},
                    "new_password": {REQUIRED: True},
                    "new_password_confirm": {REQUIRED: True, MAXLENGTH: 36, EQUALTO: "#new_password"}
                },
                messages=
                {
                    "new_password_confirm": {EQUALTO: u"密码不一致"}
                })
    @authenticated
    def put(self, *args, **kwargs):
        password = self.get_argument("password", '')
        new_password = self.get_argument("new_password", '')
        new_password_confirm = self.get_argument("new_password_confirm", '')

        if self.validation_success:
            try:
                account_service = AccountService()
                res = account_service.change_password(self.current_user.user_id, password, new_password)
                if res:
                    self.validation_success = True
            except ServiceException as e:
                self.validation_success = False
                self.validation_errors = dict(password=Errors.error_message(e.code))

        if self.validation_success:
            self.write({'code': '1'})
        else:
            self.write(self.validation_errors)


class PasswordJsonHandler(RestfulAPIHandler):

    def get(self, *args, **kwargs):
        """
        重置密码
        :param args:
        :param kwargs:
        :return:
        """

        user = self.current_user
        old_pwd = self.get_argument('password', '')

        acc_service = AccountService()
        try:
            if acc_service.is_correct_password(user.user_id, old_pwd):
                self.write_success()
            else:
                raise ServiceException(20010, 'password is wrong')
        except Exception, e:
            self.write_except(e)