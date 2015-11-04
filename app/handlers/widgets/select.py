#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.widgets.widget import Widget

__author__ = 'wangshubin'


class SelectWidget(Widget):
    """drop down list
    """
    def render(self, select_id="", is_multiple=False, name='', value='', has_null=True, null_value="", null_text="==请选择==", options=None, value_field='id',
               name_field='name', sub_type_field="sub_opt_type", cascade_options=None, ext_class='', data=None):

        # cascade_options = {
        #     "child_select_id": "",
        #     "has_null": True,
        #     "null_value": "",
        #     "null_text": "==请选择==",
        #     "data_url": "",
        #     "id_field": "",
        #     "value_field": "",
        #     "name_field": "",
        # }

        if options is None:
            options = []
        # 如果value是list,将value统一转换成str,便于select.html中作比较,防止因为类型不同而导致无法选中.
        temp_value = []
        if type(value) == list:
            temp_value = [str(val) for val in value]
        else:
            temp_value = [str(value)]
        result_params = dict()
        result_params['select_id'] = select_id  # 下拉框id
        result_params['is_multiple'] = is_multiple  # 是否是多选下拉,如果是True,需要value是数组,如果是False,需要value是单一数据
        result_params['name'] = name  # 下拉框name
        result_params['value'] = temp_value  # 默认选中项value
        result_params['has_null'] = has_null  # 是否有空选项
        result_params['null_text'] = null_text  # 空选项显示的文字
        result_params['null_value'] = null_value  # 空选项显示的值
        result_params['options'] = options  # 下拉项数据(option标签数据)
        result_params['value_field'] = value_field  # 指明options中哪个字段用于option标签的value
        result_params['name_field'] = name_field  # 指明options中哪个字段用于option标签的text
        result_params['sub_type_field'] = sub_type_field  # 指明options中哪个字段用于option标签的下级类别
        result_params['cascade_options'] = cascade_options  # 级联下拉选项
        result_params['ext_class'] = ext_class  # select表提案额外class,比如校验规则可以放到这里
        result_params['data'] = data if data and isinstance(data, dict) else dict()
        return self.render_string('widgets/select.html', **result_params)
