#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, MaxLength, MinLength, Condition


class InvoiceReqBO(BizModel):

    id = Attribute(None)
    # 用户id
    user_id = Attribute('')
    # 发票抬头
    title = Attribute(default='')
    # 发票编号
    invoice_num = Attribute(default='')
    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Attribute(default='')
    # 一般纳税人资格认证复印件
    taxpayer_certi_image = Attribute('')
    # 收件人
    recipient = Attribute('')
    # 收货地址
    delivery_address = Attribute('')
    # 联系电话
    contact_mobile = Attribute('')
    # 快递编号
    express_num = Attribute('')
    # 物流公司
    express_company = Attribute('')
    # 发票金额
    invoice_price = Attribute(0)
    # 邮政编码
    postalcode = Attribute('')
    # 创建时间
    created_at = Attribute('')
    # 邮寄状态(preparing:待邮寄, sent:已邮寄)
    mailing_status = Attribute('preparing')
    # 发票状态 0:待开发票 1:已开发票, 2作废
    invoice_status = Attribute('')

    select_order_num = Attribute('')
    # 开具类型(企业:commany/个人:person)
    make_invoice_type = Attribute('')
    # 是否作废
    is_cancel = Attribute(0)
    # 临时开票类型，为了往页面显示
    make_invoice_type_name = Attribute('')
    # 临时发票类型
    invoice_type_name = Attribute('')


class InvoiceAddReqBO(BizModel):

    id = Attribute(None)
    # 用户id
    user_id = Attribute('')
    # 发票抬头
    title = Attribute(default='')
    # 发票金额
    invoice_price = Attribute(default=0, validators=Validators([Required()], name='发票金额'))
    # 发票编号
    invoice_num = Attribute(default='')
    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Attribute(default='')
    # 发票邮寄地址
    delivery_address_id = Attribute(default='', validators=Validators([Required()], name='发票邮寄地址'))
    # 开具类型(企业:company/个人:person)
    make_invoice_type = Attribute(default='')
    order_ids = Attribute(default='')
    # 收件人
    recipient = Attribute('')
    # 收货地址
    delivery_address = Attribute('')
    # 联系电话
    contact_mobile = Attribute('')
    # 邮政编码
    postalcode = Attribute('')
    # 一般纳税人资格认证复印件
    taxpayer_certi_image = Attribute('')