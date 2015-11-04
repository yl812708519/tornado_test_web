#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.widgets.widget import Widget

__author__ = 'freeway'


class HtmlSelectWidget(Widget):
    """drop down list
    """
    def render(self, html_id='', name='', value='', readonly='', options=None, value_field='id', name_field='name'):
        if options is None:
            options = []
        result_params = dict()
        result_params['id'] = html_id
        result_params['name'] = name
        result_params['value'] = value
        result_params['readonly'] = readonly
        result_params['value_field'] = value_field
        result_params['name_field'] = name_field
        result_params['options'] = options
        return self.render_string('widgets/html_select.html', **result_params)
