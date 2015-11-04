#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String
from app.commons.database import DatabaseTemplate, model, BaseModel
from app.commons.database_mixin import IdMixin

__author__ = 'freeway'


class Country(IdMixin, BaseModel):
    code = Column(String(6))
    name = Column(String(20))
    acronym = Column(String(1))


@model(Country)
class CountryDao(DatabaseTemplate):
    def get_all(self):
        return self.session.query(self.model_cls).order_by(Country.id).all()
