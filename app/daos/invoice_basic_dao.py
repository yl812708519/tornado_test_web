#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'freeway'

from sqlalchemy import Column, String

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class InvoiceBasicType(object):
    #  增值税普通发票
    NORMAL = 'normal'
    #  增值税专用发票
    SPECIAL = 'special'


class InvoiceBasic(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(36))

    # 发票抬头
    title = Column(String(200))

    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Column(String(30))

    # 营业执照复印件
    certi_img = Column(String(200), default='')

    # 税务登记证号
    tax_reg_certi_num = Column(String(40), default='')

    # 基本户开户银行名称
    bank_name = Column(String(200), default='')

    # 基本开户账号
    bank_account = Column(String(60), default='')

    # 注册场所地址
    register_address = Column(String(300), default='')

    # 注册固定电话
    register_phone = Column(String(20), default='')

    # 一般纳税人资格认证复印件
    taxpayer_certi_img = Column(String(200), default='')

    # 税务登记复印件
    tax_certi_img = Column(String(200))

    # 开票类型
    make_invoice_type = Column(String(30))


@model(InvoiceBasic)
class InvoiceBasicDao(DatabaseTemplate):

    def get_by_uid(self, uid):
        return self.get_first_by_criterion(InvoiceBasic.user_id == uid)