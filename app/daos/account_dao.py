#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger, String, Integer, Boolean
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin

__author__ = 'freeway'


class AccountType(object):
    MOBILE = 'mobile'
    EMAIL = 'email'


class AccountStatus(object):
    SEND_CODE = 'send_code'
    INPUT_PASSWORD = 'input_password'
    INPUT_REAL_PROFILE = 'input_real_profile'


class Account(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    # 用户id
    user_id = Column(BigInteger, default='')
    # 账号类型
    account_type = Column(String(10), default=None)
    # 账号名称
    account = Column(String(80), default=None)
    # 连续登录失败次数
    fail_count = Column(Integer, default=0L)
    # 锁定的时间，预计1-2小时候解锁
    locked_at = Column(BigInteger, default=0L)


@model(Account)
class AccountDao(DatabaseTemplate):

    def get_by_name_account_type(self, name, account_type):
        """

        :param account:
        :param account_type:
        :return:
        """
        return self.get_first_by_criterion(Account.account == name, Account.account_type == account_type)

    def get_by_user_id_account_type(self, user_id, account_type):
        """ 根据用户id和账号类型获取账号

        :param user_id: 用户id
        :param account_type: 账号类型
        :return:
        """
        return self.get_first_by_criterion(Account.user_id == user_id, Account.account_type == account_type)

    def get_by_user_id(self, user_id):
        """ 根据user_id获取帐号

        :param user_id: 用户id
        :return:
        """
        return self.session.query(self.model_cls).filter(Account.user_id == user_id).first()