#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition


class MarkRegApplyBO(BizModel):
    # 通用属性
    id = Attribute('')
    user_id = Attribute('')
    order_id = Attribute('')
    applicant_id = Attribute('')
    applicant = Attribute('')
    mark_reg_num = Attribute('')
    biz = Attribute('')
    is_paid = Attribute(False)
    is_confirmed = Attribute(False)
    is_reviewed = Attribute(False)
    order_tpl = Attribute('mark/mark_reg_apply')
    base_type = Attribute('mark')
    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Attribute(False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Attribute(False)


class MarkRegReissueBO(MarkRegApplyBO):
    reissue_reason = Attribute('')


class MarkRegProvideProofBO(MarkRegApplyBO):
    category_codes = Attribute('')
    category_code_list = Attribute('')


class MarkRegCorrectItemBO(MarkRegProvideProofBO):
    is_reset = Attribute(False)
    correct_items = Attribute('')
    category_code_list = Attribute('')


class MarkApplyInfoBO(BizModel):
    order_id = Attribute('', validators=Validators([Required()]))
    applicant_id = Attribute('', validators=Validators([Required()]))
    mark_reg_num = Attribute('', validators=Validators([Required()]))


class MarkApplyMainBO(BizModel):
    order_id = Attribute('', validators=Validators([Required()]))
    biz = Attribute('', validators=Validators([Required()]))
    reissue_reason = Attribute('', validators=Validators([Required()]),
                               v_condition=Condition('biz', 'reissue_reg_credential'))
    category_codes = Attribute('', validators=Validators([Required()]), attri_type=list,
                               v_condition=Condition('biz', ('provide_mark_reg_proof', 'correct_mark_reg_items')))
    correct_items = Attribute('', validators=Validators([Required()]),
                              v_condition=Condition('biz', 'correct_mark_reg_items'))
    is_reset = Attribute(False, validators=Validators([Required()]), attri_type=bool,
                         v_condition=Condition('biz', 'correct_mark_reg_items'))