#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, Float
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class Business(IdMixin, BaseModel):
    name = Column(String(80), default='')
    produce = Column(String(80), default='')
    service_charge = Column(Float, default='')
    official_charge = Column(Float, default='')
    market_price = Column(String(40), default='')
    type = Column(String(40), default='')
    tax = Column(Float, default=0)


@model(Business)
class BusinessDao(DatabaseTemplate):

    def get_by_name(self, name):
        return self.session.query(self.model_cls).filter(self.model_cls.name == name).first()

    def gets_by_type(self, type):
        return self.session.query(self.model_cls).filter(self.model_cls.type == type).all()