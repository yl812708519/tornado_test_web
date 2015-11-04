#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.biz_model import BizModel, Attribute
from app.daos.area_process_dao import CityDao, ProvinceDao, AreaDao
from app.daos.options_dao import OptionDao
from configs.database_builder import DatabaseBuilder

__author__ = 'WangShubin'


class OptionBO(BizModel):

    opt_value = Attribute(None)
    opt_title = Attribute(default='')
    opt_type = Attribute(None)
    opt_selected = Attribute(None)
    opt_order = Attribute(default=None)
    sub_opt_type = Attribute(default=None)

    id = Attribute(None)
    name = Attribute('')
    value = Attribute('')
    province_value = Attribute('')
    city_value = Attribute('')


class OptionsService(object):
    """各种k，v数据服务信息
    """

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get_city_by_value(self, value):
        """根据value查询中文
        :param value:
        :return: 中文名称
        """
        with self._default_db.create_session() as session:
            city_dao = CityDao(session)
            city = city_dao.get_by_value(value)
            return OptionBO(**city.fields)

    def get_province_by_value(self, value):
        """根据value查询中文
        :param value:
        :return: 中文名称
        """
        with self._default_db.create_session() as session:
            province_dao = ProvinceDao(session)
            province = province_dao.get_by_value(value)
            return OptionBO(**province.fields)

    def get_area_by_value(self, value):
        """根据value查询中文
        :param value:
        :return: 中文名称
        """
        with self._default_db.create_session() as session:
            area_dao = AreaDao(session)
            area = area_dao.get_by_value(value)
            return OptionBO(**area.fields)

    def gets_by_type(self, opt_type):
        with self._default_db.create_session() as session:
            option_dao = OptionDao(session)
            options = option_dao.gets_by_type(opt_type)
            return [OptionBO(**option.fields) for option in options] if len(options) > 0 else None

    def get_by_type_value(self, opt_type, opt_value):
        with self._default_db.create_session() as session:
            option_dao = OptionDao(session)
            option = option_dao.get_by_type_value(opt_type, opt_value)
            return OptionBO(**option.fields) if option else None

    def gets_main_ipc_type(self):

        with self._default_db.create_session() as session:
            option_dao = OptionDao(session)
            main_ipc_types = option_dao.gets_by_type("IPC_TYPE")
            return [OptionBO(**main_ipc_type.fields) for main_ipc_type in main_ipc_types] if len(main_ipc_types) > 0 else None

    def gets_patent_type(self):

        with self._default_db.create_session() as session:
            option_dao = OptionDao(session)
            patent_types = option_dao.gets_by_type("PATENTS_TYPE")
            return [OptionBO(**patent_type.fields) for patent_type in patent_types] if len(patent_types) > 0 else None

    def gets_patent_main_category(self):
        return self.gets_by_type("PATENT_CATEGORY")

    def gets_trademark_main_category(self):
        return self.gets_by_type("TRADEMARK")


