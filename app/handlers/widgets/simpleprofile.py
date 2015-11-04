#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2011-6-27
@author: willian.huw
"""
from app.handlers.widgets.widget import Widget


class SimpleProfileWidget(Widget):
    def render(self, **result_params):
        return self.render_string('widgets/simpleprofile.html', **result_params)