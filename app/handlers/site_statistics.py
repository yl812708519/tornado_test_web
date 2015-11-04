#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons import dateutil
from app.handlers.application import BaseHandler
from app.services.site_statistics_service import SiteStatisticService


class SiteStatisticHandler(BaseHandler):

    def get(self):
        h = self.get_argument('hour', '')
        start_time = dateutil.timestamp() - (((24 + int(h)) * 60 * 60) * 1000)
        end_time = dateutil.timestamp() - ((int(h) * 60 * 60) * 1000)
        site_statistic_service = SiteStatisticService()
        signup_num = site_statistic_service.get_signup_num(start_time, end_time)
        transaction_num = site_statistic_service.get_transaction_num(start_time, end_time)
        untreated_order_num = site_statistic_service.get_untreated_order_num(start_time, end_time)
        confirm_order_num = site_statistic_service.get_confirm_order_num(start_time, end_time)
        res = site_statistic_service.add(signup_num, transaction_num, untreated_order_num, confirm_order_num, start_time)
        if res:
            self.write('ok')
        else:
            self.write('fail')

