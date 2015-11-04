#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute

__author__ = 'zhaowenlei'

class CopyrightOwnerBO(BizModel):
    biz_id = Attribute(None)
    name = Attribute(default='')
    type = Attribute(default='')
    region = Attribute(default='')
    province = Attribute(default='')
    city = Attribute(default='')
    certi_type = Attribute(default='')
    certi_num = Attribute(default='')
    com_type = Attribute(default='')
    park = Attribute(default='')
    sign_situation = Attribute(default='')