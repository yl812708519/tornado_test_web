#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.services.applicant_service import ApplicantBO


class OrderBO(BizModel):
    id = Attribute()
    user_id = Attribute(None)
    csu_id = Attribute(None)
    # cs_user = Attribute(attri_type=)
    name = Attribute(None)
    order_type = Attribute(None)
    order_type_str = Attribute(None)
    price = Attribute(None)
    status = Attribute(None)
    status_name = Attribute('')
    is_in_trash = Attribute(False)
    created_at = Attribute(None)
    created_date = Attribute(None)
    updated_at = Attribute(None)
    is_tiped = Attribute(0)
    is_invoice_able = Attribute(0)
    is_invoiced = Attribute(0)
    is_paid = Attribute(0)


class OrderPaymentBO(BizModel):
    out_trade_no = Attribute(None)
    pay_mode = Attribute(None)
    pay_fee = Attribute(None)
    pay_config = Attribute(None)
    buyer_account = Attribute(None)
    order_id = Attribute(None)
    payment_date = Attribute(None)


class OrderAppBO(ApplicantBO):
    applicant_id = Attribute('')
    source_type = Attribute('')
    source_id = Attribute('')