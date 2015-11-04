#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.handlers.widgets.widget import Widget
from app.commons import dateutil


class DateWidget(Widget):

    def render(self, datetime, style='offset'):
        if style == 'offset':
            return dateutil.offset_time(datetime)
        else:
            #date
            return dateutil.datetime_to_string(datetime)