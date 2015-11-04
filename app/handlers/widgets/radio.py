#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.widgets.widget import Widget

__author__ = 'wangshubin'


class RadioWidget(Widget):
    """drop down list
    """
    def render(self, name='', value='', radio_type="ori_inline", checked_class="btn-pink", not_checked_class="btn-wrap",
               options=None, value_field='id', name_field='name', ext_class='', data_fields=''):

        # 如果value是list,将value统一转换成str,便于select.html中作比较,防止因为类型不同而导致无法选中.
        temp_value = []
        if type(value) == list:
            temp_value = [str(val) for val in value]
        else:
            temp_value = [str(value)]
        result_params = dict()
        result_params['name'] = name  # 下拉框name
        result_params['value'] = temp_value  # 默认选中项value
        result_params['radio_type'] = radio_type  # ori/ori_inline/cus/cus_inline(原始/原始 inline/自定义/自定义 inline )
        result_params['checked_class'] = checked_class  # 选中样式
        result_params['not_checked_class'] = not_checked_class  # 未选中样式


        result_params['options'] = options  # 下拉项数据(option标签数据)
        result_params['value_field'] = value_field  # 指明options中哪个字段用于option标签的value
        result_params['name_field'] = name_field  # 指明options中哪个字段用于option标签的text
        result_params['ext_class'] = ext_class  # select表提案额外class,比如校验规则可以放到这里
        result_params['data_fields'] = data_fields if type(data_fields) in (list, tuple) else ()
        return self.render_string('widgets/radio.html', **result_params)
