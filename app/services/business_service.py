#! /usr/bin/evt python
# -*- coding:utf-8 -*-

__author__ = 'yanglu'

from app.commons.biz_model import BizModel, Attribute
from app.commons.memcache_factory import MemCacheFactory
from configs.database_builder import DatabaseBuilder
from app.daos.business_dao import BusinessDao
from app.services.base_service import BaseService


class BusinessBO(BizModel):
    id = Attribute('')
    name = Attribute('')
    produce = Attribute('')
    service_charge = Attribute('')
    official_charge = Attribute('')
    market_price = Attribute('')
    type = Attribute('')
    tax = Attribute(default=0)
    freight = Attribute(default=0)


class BusinessService(BaseService):
    """
    产品，以后会改成 数据库取出，memcache保存的方式
    """
    _cache_session = 'biz'

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @classmethod
    def _parse_to_key(cls, name):
        """
        产品的 name
        :param arg:
        :return:
        """
        return "produce:{0}".format(name)

    def _get_by_name(self, name):
        with self._default_db.create_session() as session:
            produce = BusinessDao(session).get_by_name(name)
            return BusinessBO(**produce.fields) if produce is not None else None

    def get_by_type(self, p_type):
        with self._default_db.create_session() as session:
            produces = BusinessDao(session).gets_by_type(p_type)
            produce_bos = [BusinessBO(**produce.fields) for produce in produces]
        return produce_bos

    def get_by_name(self, name):
        # memcacahe_factory = MemCacheFactory.get_instance(session=self._cache_session)
        # key = self._parse_to_key(name)
        # memcacahe_factory.delete(key)
        # produce_bo = memcacahe_factory.get(key)
        produce_bo = None
        if not produce_bo or not produce_bo.id:
            produce_bo = self._get_by_name(name)
            # memcacahe_factory.set(key, produce_bo)
        return produce_bo
