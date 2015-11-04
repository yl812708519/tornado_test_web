#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from app.commons.biz_model import BizModel, Attribute
from app.daos.customer_record_dao import CustomerRecordDao
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder
from configs.thrift_builder import ThriftBuilder

__author__ = 'zhaowenlei'

class CustomerRecordBO(BizModel):

    id = Attribute(None)
    order_id = Attribute(None)
    record = Attribute('')
    created_at = Attribute(None)

class CustomerRecordService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def gets_by_order_id(self, order_id):
        with self.create_session(self._default_db) as session:
            cs_record_dao = CustomerRecordDao(session)
            cs_records = cs_record_dao.gets_by_order_id(order_id)
            return [CustomerRecordBO(**cs_record.fields) for cs_record in cs_records]

