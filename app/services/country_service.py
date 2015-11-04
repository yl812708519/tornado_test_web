#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.biz_model import BizModel, Attribute
from app.daos.country_dao import CountryDao
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder

__author__ = 'freeway'


class CountryBO(BizModel):
    code = Attribute('')
    name = Attribute('')


class CountryService(BaseService):
    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get_all(self):
        with self.create_session(self._default_db) as session:
            country_dao = CountryDao(session)
            return [CountryBO(**country.fields) for country in country_dao.get_all()]
