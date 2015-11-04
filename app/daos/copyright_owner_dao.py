#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import CreatedAtMixin, UpdatedAtMixin, IdMixin

__author__ = 'zhaowenlei'


class CopyrightOwner(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    biz_id = Column(BigInteger)
    name = Column(String(20), default='')
    type = Column(String(20), default='')
    region = Column(String(20), default='')
    province = Column(String(20), default='')
    city = Column(String(20), default='')
    certi_type = Column(String(20), default='')
    certi_num = Column(String(20), default='')
    com_type = Column(String(20), default='')
    park = Column(String(20), default='')
    sign_situation = Column(String(20), default='')


@model(CopyrightOwner)
class CopyrightOwnerDao(DatabaseTemplate):

    def get_by_biz_id(self, biz_id):
        return self.session.query(self.model_cls).filter(self.model_cls.biz_id == biz_id).first()
