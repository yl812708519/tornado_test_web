#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, IsDeletedMixin, UpdatedAtMixin, CreatedAtMixin


class DeliveryAddress(IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin, BaseModel):
    user_id = Column(String(36), default='')
    name = Column(String(50), default='')
    mobile = Column(String(20), default='')
    province_code = Column(String(10), default='')
    city_code = Column(String(10), default='')
    area_code = Column(String(10), default='')
    # town_code = Column(String(10), default='')
    address = Column(String(100), default='')
    postalcode = Column(String(10), default='')


@model(DeliveryAddress)
class DeliveryAddressDao(DatabaseTemplate):
    """收货地址访问对象"""
    def gets_by_user_id(self, user_id):
        """
        根据用户id查询收货地址
        :param user_id:
        :return:
        """
        return self.session.query(self.model_cls).filter(self.model_cls.user_id == user_id,
                                                         self.model_cls.is_deleted == False).all()