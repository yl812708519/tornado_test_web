#! /usr/bin/evt python
# -*- coding:utf-8 -*-

__author__ = 'yanglu'


class StaticOptionService(object):
    mark_reg_service = None

    # 商标注册预判的状态对应信息
    mark_forecast_status = {'apply_able': '可申请',
                            'review': '审核中',
                            'non_apply': '不可申请'}