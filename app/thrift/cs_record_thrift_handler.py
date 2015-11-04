#!/usr/bin/env python
# coding:utf-8
import json
from app.services.customer_record_service import CustomerRecordService

__author__ = 'zhaowenlei'

class ThriftCsRecordHandler(object):
    @staticmethod
    def biz_bos_to_json(biz_bos):
        biz_list = list()
        if biz_bos:
            for biz_bo in biz_bos:
                biz_list.append(biz_bo.attributes)
            return json.dumps(biz_list)
        else:
            return ''

    @staticmethod
    def gets_by_order_id(order_id):
        cs_record_bos = CustomerRecordService().gets_by_order_id(order_id)
        return ThriftCsRecordHandler.biz_bos_to_json(cs_record_bos)