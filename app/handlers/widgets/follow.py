#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2011-6-27
@author: willian.huw
'''
from app.handlers.widgets.widget import Widget

class FollowWidget(Widget):
    def render(self, **result_params):
        return self.render_string('widgets/follow.html', **result_params)
