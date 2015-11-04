#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Boolean, BigInteger, desc, func, Date

from app.commons import dateutil
from app.commons.database import DatabaseTemplate, BaseModel, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class Province(IdMixin, BaseModel):
    
    name = Column(String(80), default='')
    value = Column(String(80), default='')


@model(Province)
class ProvinceDao(DatabaseTemplate):
    """
    省数据访问类
    """
    def get_by_value(self, value):
        """根据value查询单条记录
        :param value:
        :return: Province
        """
        return self.session.query(self.model_cls).filter(Province.value == value).first()

    def get_dict_by_values(self, values):
        provinces = self.session.query(self.model_cls).filter(self.model_cls.value.in_(values)).all()
        inst_dict = dict()
        for province in provinces:
            inst_dict[province.value] = province
        return inst_dict


class City(IdMixin, BaseModel):
    name = Column(String(80), default='')
    value = Column(String(80), default='')
    province_value = Column(String(80), default='')


@model(City)
class CityDao(DatabaseTemplate):
    """
    省数据访问类
    """
    def get_by_value(self, value):
        """根据value查询单条记录
        :param value:
        :return: Province
        """
        return self.session.query(self.model_cls).filter(City.value == value).first()

    def get_dict_by_values(self, values):
        cities = self.session.query(self.model_cls).filter(self.model_cls.value.in_(values)).all()
        inst_dict = dict()
        for city in cities:
            inst_dict[city.value] = city
        return inst_dict


class Area(IdMixin, BaseModel):
    name = Column(String(80), default='')
    value = Column(String(80), default='')
    city_value = Column(String(80), default='')


@model(Area)
class AreaDao(DatabaseTemplate):
    """
    省数据访问类
    """
    def get_by_value(self, value):
        """根据value查询单条记录
        :param value:
        :return: Province
        """
        return self.session.query(self.model_cls).filter(Area.value == value).one()

    def get_dict_by_values(self, values):
        areas = self.session.query(self.model_cls).filter(self.model_cls.value.in_(values)).all()
        inst_dict = dict()
        for area in areas:
            inst_dict[area.value] = area
        return inst_dict
