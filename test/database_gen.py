#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inflection
from tornado.template import os, Loader
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder

__author__ = 'freeway'


class GenMeta(object):

    def __init__(self, entity):
        self.column_name = entity[0]
        self.column_default = entity[1]
        self.data_type = entity[2]
        self.column_key = entity[3]
        self.is_nullable = entity[4]
        self.character_maximum_length = entity[5]
        self.column_comment = entity[6]

class DbModelMeta(object):

    def __init__(self):
        self.has_id = False
        self.is_string_id = False
        self.has_created_at = False
        self.has_updated_at = False
        self.has_is_deleted = False
        self.table_metas = None
        self.class_name = ''


class DatabaseGenService(BaseService):

    def __init__(self):
        # DatabaseBuilder.run_mode = 'test'
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def gen_db_model(self, schema_name, table_name):
        sql = """ SELECT column_name, column_default, data_type, column_key, is_nullable,
                         character_maximum_length, column_comment
                  FROM information_schema.columns
                  WHERE TABLE_SCHEMA = :schema_name AND
                        TABLE_NAME = :table_name
                  ORDER BY ORDINAL_POSITION"""

        with self.create_session(self._default_db) as session:
            entities = session.execute(sql, dict(schema_name=schema_name, table_name=table_name))
            metas = [GenMeta(entity) for entity in entities if entity[0] != 'pkid']
            model_meta = DbModelMeta()
            model_meta.table_metas = metas
            for meta in metas:
                if model_meta.has_id is False:
                    model_meta.has_id = meta.column_name == 'id'
                    model_meta.is_string_id = meta.column_name == 'id' and \
                                              u'varchar' == meta.data_type
                if model_meta.has_created_at is False:
                    model_meta.has_created_at = meta.column_name == 'created_at'
                if model_meta.has_updated_at is False:
                    model_meta.has_updated_at = meta.column_name == 'updated_at'
                if model_meta.has_is_deleted is False:
                    model_meta.has_is_deleted = meta.column_name == 'is_deleted'
            model_meta.class_name = inflection.singularize(inflection.camelize(table_name))

            template_path = os.path.join(os.path.dirname(__file__))
            t = Loader(template_path, **{}).load('model.tpl')
            print t.generate(**model_meta.__dict__)


if __name__ == "__main__":

    # DatabaseBuilder.run_mode = 'test'
    gen = DatabaseGenService()
    # gen.gen_db_model('aiwanr_test', 'weixin_subscribes')
    gen.gen_db_model('36ban_dev', 'mark_change_orders')
