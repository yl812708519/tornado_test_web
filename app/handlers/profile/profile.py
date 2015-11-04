#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.account_service import AccountService

__author__ = 'yanglu'

from tornado.web import authenticated
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.commons.view_model import ViewModel
from app.commons.decoraters_tornado import validators
from app.commons.validators import REQUIRED
from configs.errors import Errors

from app.services.base_service import ServiceException
from app.services.user_service import UserService, UserProfileBO, UserBO


class ProfileHandler(BaseHandler):

    @authenticated
    def get(self):
        user = self.current_user
        profile_bo = UserService().get_profile(user.user_id)
        result = dict(profile=ViewModel.to_view(profile_bo))
        referer = self.request.headers['Referer']
        result['referer'] = referer
        self.render('user/profile.html', **result)

    @authenticated
    @validators(rules=
                {
                    "nickname": {REQUIRED: True}
                },
                messages=
                {
                    "nickname": {REQUIRED: u'为空肯定不行啊'}
                })
    def post(self):
        """
        修改 个人信息
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        profile = dict(
            nickname=self.get_argument('nickname', ''),
            email=self.get_argument('email', ''),
            mobile=self.get_argument('mobile', ''),
            company=self.get_argument('company', ''),
            company_desc=self.get_argument('company_desc', ''),
            user_id=user.user_id,
            province=self.get_argument('province', ''),
            city=self.get_argument('city', ''),
            area=self.get_argument('area', ''),
            address=self.get_argument('address', '')
        )

        if self.validation_success:
            user_service = UserService()
            user_profile_bo = UserProfileBO(**profile)
            try:
                user_service.update(user.user_id, user_profile_bo.nickname, avatar='')
                user_service.add_profile(user_profile_bo)
                self.redirect(self.get_argument('referer'))
            except Exception, e:
                if isinstance(e, ServiceException):
                    self.write(dict(code=e.code, msg=Errors.error_message(e.code)))
                else:
                    raise e
        else:
            result = dict(validation_errors=self.validation_errors,
                          profile=ViewModel.to_view((UserProfileBO(**profile))))
            self.render('user/profile.html', **result)

    @authenticated
    @validators(rules=
                {
                    "nickname": {REQUIRED: True},
                    "email": {REQUIRED: True}
                },
                messages=
                {
                    "nickname": {REQUIRED: u'姓名不能为空'},
                    "email": {REQUIRED: u'邮箱不能为空'}
                })
    def put(self, *args, **kwargs):
        """
        修改 个人信息
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        profile = dict(
            id=self.get_argument('profile_id', ''),
            nickname=self.get_argument('nickname', ''),
            email=self.get_argument('email', ''),
            company=self.get_argument('company', ''),
            company_desc=self.get_argument('company_desc', ''),
            user_id=user.user_id,
            mobile=self.get_argument('mobile', ''),
            province=self.get_argument('province', ''),
            city=self.get_argument('city', ''),
            area=self.get_argument('area', ''),
            address=self.get_argument('address', '')
        )
        if self.validation_success:
            user_service = UserService()
            try:
                user_service.update_profile(UserProfileBO(**profile))
                self.redirect(self.get_argument('referer'))
            except Exception, e:
                if isinstance(e, ServiceException):
                    self.write(dict(code=e.code, msg=Errors.error_message(e.code)))
                else:
                    raise e
        else:
            result = dict(validation_errors=self.validation_errors,
                          profile=ViewModel.to_view((UserProfileBO(**profile))))
            self.render('user/profile.html', **result)

#
# class ProfileAPIHandler(RestfulAPIHandler):
#
#     @authenticated
#     @validators(rules=
#                 {
#                     "nickname": {REQUIRED: True}
#                 },
#                 messages=
#                 {
#                     "nickname": {REQUIRED: u'为空肯定不行啊'}
#                 })
#     def post(self):
#         """
#         判断提交数据是否重复。。目前有nickname
#         :return:
#         """
#
#         nickname = self.get_argument('nickname', None)
#         user_id = self.current_user.user_id
#         user_service = UserService()
#         try:
#             if user_service.is_exist_nickname(nickname, user_id):
#                 raise ServiceException(20030, 'this nickname has register')
#             else:
#                 self.write({'result': 1})
#         except Exception, e:
#             self.write_except(e)

