#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition

class InvoiceBasicBO(BizModel):

    id = Attribute(None)
    # 用户id
    user_id = Attribute('')
    # 发票抬头
    title = Attribute('')
    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Attribute('')
    # 营业执照复印件
    certi_img = Attribute('')
    # 税务登记证号
    tax_reg_certi_num = Attribute('')
    # 基本户开户银行名称
    bank_name = Attribute('')
    # 基本开户账号
    bank_account = Attribute('')
    # 注册场所地址
    register_address = Attribute('')
    # 注册固定电话
    register_phone = Attribute('')
    # 一般纳税人资格认证复印件
    taxpayer_certi_img = Attribute('')
    # 税务登记复印件
    tax_certi_img = Attribute('')
    created_at = Attribute('')
    # 开具类型，个人，或者企业
    make_invoice_type = Attribute('')
    # 临时开票类型，为了往页面显示
    make_invoice_type_name = Attribute('')
    # 临时发票类型
    invoice_type_name = Attribute('')

    download_certi_img_url = Attribute('')
    download_taxpayer_certi_img_url = Attribute('')
    download_tax_certi_img_url = Attribute('')


class InvoiceReqBo(BizModel):

    id = Attribute(None)
    user_id = Attribute('')
    title = Attribute(default='', validators=Validators([Required()], name='发票抬头'))
    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Attribute(default='', validators=Validators([Required()], name='发票类型'))
    # 开具类型，个人，或者企业
    make_invoice_type = Attribute(default='', validators=Validators([Required()], name='开具类型'),
                                  v_condition=Condition('invoice_type', 'special'))
    tax_reg_certi_num = Attribute(default='', validators=Validators([Required()], name='税务登记证号'),
                                  v_condition=Condition('invoice_type', 'special'))
    bank_name = Attribute(default='', validators=Validators([Required()], name='基本户开户银行名称'),
                          v_condition=Condition('invoice_type', 'special'))
    bank_account = Attribute(default='', validators=Validators([Required()], name='基本开户账号'),
                             v_condition=Condition('invoice_type', 'special'))
    register_address = Attribute(default='', validators=Validators([Required()], name='注册场所地址'),
                                 v_condition=Condition('invoice_type', 'special'))
    register_phone = Attribute(default='', validators=Validators([Required()], name='注册固定电话'),
                               v_condition=Condition('invoice_type', 'special'))
    certi_img = Attribute(default='', validators=Validators([Required()], name='营业执照复印件'),
                          v_condition=Condition('invoice_type', 'special'))
    tax_certi_img = Attribute(default='', validators=Validators([Required()], name='税务登记复印件'),
                              v_condition=Condition('invoice_type', 'special'))
    taxpayer_certi_img = Attribute(default='', validators=Validators([Required()], name='一般纳税人资格认证复印件'),
                                   v_condition=Condition('invoice_type', 'special'))