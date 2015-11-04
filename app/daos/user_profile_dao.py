#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'

from app.commons import dateutil
from sqlalchemy import Column, String, Boolean, Integer

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import UpdatedAtMixin, IdMixin, CreatedAtMixin


class UserProfile(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    nickname = Column(String(50), default='')
    user_id = Column(String(36))
    mobile = Column(String(36), default='')
    email = Column(String(120), default='')
    company = Column(String(80), default='')
    company_desc = Column(String(255), default='')
    province = Column(Integer, default=0)
    city = Column(Integer, default=0)
    area = Column(Integer, default=0)
    address = Column(String(200), default='')


@model(UserProfile)
class UserProfileDao(DatabaseTemplate):

    def get_by_user(self, user_id):
        """
        获取user_id 对应的profile信息
        :param user_id:
        :return:
        """
        return self.session.query(self.model_cls).filter(UserProfile.user_id == user_id).first()

    def update_profile(self, profile):
        """
        更新 用户profile 信息
        :param instance:
        :return:
        """
        profile['updated_at'] = dateutil.timestamp()
        # del profile['email']
        # del profile['mobile']
        return self.session.query(self.model_cls).\
            filter(UserProfile.user_id == profile['user_id']).update(profile)