#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from app.handlers.application import BaseHandler
from app.services.monitor_service import MonitorService

__author__ = 'zhaowenlei'


class MonitorOkHandelr(BaseHandler):

    def get(self):
        monitor_service = MonitorService()
        result = monitor_service.select_ok()
        if result:
            self.write('ok')
        else:
            logging.error("Database access error")
            self.write('fail')
