#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import datetime
from app.commons import dateutil

__author__ = 'freeway'


class DateutilTestCase(unittest.TestCase):

    def test_timestamp(self):
        timestamp = dateutil.timestamp()
        self.assertEqual(len(str(timestamp)), 13)

    def test_format_to_string(self):
        now = datetime.datetime.now()
        date_str = dateutil.datetime_to_string(now)
        self.assertEqual(now.year, int(date_str[:4]))
        self.assertEqual(now.month, int(date_str[5:7]))
        self.assertEqual(now.day, int(date_str[8:]))
