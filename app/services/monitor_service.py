#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.biz_model import BizModel, Attribute
from app.daos.area_process_dao import CityDao, ProvinceDao, AreaDao
from app.daos.options_dao import OptionDao
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'

class MonitorService(object):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def select_ok(self):
        with self._default_db.create_session() as session:
            return session.execute('select 1').rowcount