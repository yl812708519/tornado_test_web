#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Boolean

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import UpdatedAtMixin, CreatedAtMixin, IdMixin


class User(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    name = Column(String(50), default='')
    user_id = Column(String(36))
    # hashed_password = Column(String(36))
    # salt = Column(String(5))
    avatar = Column(String(200), default='')
    gender = Column(String(1), default='N')
    is_locked = Column(Boolean, default=False)

@model(User)
class UserDao(DatabaseTemplate):
    """用户数据访问对象"""

    def get(self, identity):
        """根据user_id获取user对象

        :param identity: user_id
        :return: 获取user
        """
        return self.get_first_by_criterion(User.user_id == identity)

    def gets_by_user_ids(self, user_ids):
        return self.session.query(self.model_cls).filter(self.model_cls.user_id.in_(user_ids)).all()

    def get_by_name(self, nickname):
        """根据名称获取user对象

        :param name: 用户名称
        :return: user 对象
        """
        return self.get_first_by_criterion(User.name == nickname)

    def reset_password(self, user_id, hashed_password, salt):
        """
        更新密码。
        :param user_id:
        :param hashed_password:
        :param salt:
        :return:
        """
        return self.session.query(self.model_cls).\
            filter(User.user_id == user_id).\
            update({'hashed_password': hashed_password,
                    'salt': salt})
