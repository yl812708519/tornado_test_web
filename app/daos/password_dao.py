#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import String, Column, BigInteger

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


__author__ = 'freeway'


class Password(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    account_id = Column(String(36))
    hashed_password = Column(String(32))
    salt = Column(String(5))

@model(Password)
class PasswordDao(DatabaseTemplate):
    """密码据访问对象"""

    def get_by_account_id(self, account_id):
        """根据账号id获取与之对应的密码

        :param account_id:
        :return:
        """
        return self.get_first_by_criterion(Password.account_id == account_id)
