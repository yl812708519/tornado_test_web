#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2011-6-27

@author: willian.huw
'''
from app.handlers.widgets.widget import Widget

class CommonWidget(Widget):

    def render(self, path, **result_params):
        return self.render_string(path, **result_params)
