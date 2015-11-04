#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.biz_model import BizModel, Attribute
from app.handlers.site_statistics_dao import SiteStatisticDao
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'


class SiteStatisticBO(BizModel):
    
    id = Attribute(None)
    signup_num = Attribute(None)
    transaction_num = Attribute(None)
    untreated_order_num = Attribute(None)
    confirm_order_num = Attribute(None)
    collected_at = Attribute(None)


class SiteStatisticService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def count_by_user_id(self, offset=0, page_size=15):
        with self._default_db.create_session() as session:
            site_statistic_dao = SiteStatisticDao(session)
            count, site_statistics = site_statistic_dao.count_by_user_id(offset, page_size)
            return count, [SiteStatisticBO(**site_statistic.fields) for site_statistic in site_statistics]

    def execute_sql(self, sql):
        with self._default_db.create_session() as session:
            return session.execute(sql).rowcount

    def get_signup_num(self, start_time, end_time):
            return self.execute_sql("select * from accounts where created_at >= '%d' and created_at <= '%d'" % (start_time, end_time))

    def get_transaction_num(self, start_time, end_time):
        return self.execute_sql("select * from orders where status = 'paid' and created_at >= '%d' and created_at <= '%d'" % (start_time, end_time))

    def get_untreated_order_num(self, start_time, end_time):
        return self.execute_sql("select * from customer_service_orders where is_finished = 0 and created_at >= '%d' and created_at <= '%d'" % (start_time, end_time))

    def get_confirm_order_num(self, start_time, end_time):
        return self.execute_sql("select * from customer_service_orders where is_finished = 1 and created_at >= '%d' and created_at <= '%d'" % (start_time, end_time))

    def add(self, signup_num, transaction_num,
            untreated_order_num, confirm_order_num,
            collected_at):
        with self._default_db.create_session() as session:
            site_statistics_sql = "insert into site_statistics(signup_num, transaction_num, untreated_order_num, confirm_order_num, collected_at) " \
                              "VALUES ({0}, {1}, {2}, {3}, {4})".format(signup_num, transaction_num, untreated_order_num, confirm_order_num, collected_at)
            return session.execute(site_statistics_sql)