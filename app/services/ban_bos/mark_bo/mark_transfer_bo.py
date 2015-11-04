#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition, In


class MarkTransferBaseBO(BizModel):
    id = Attribute('')
    user_id = Attribute('')
    order_id = Attribute()
    biz = Attribute('')
    # post_num = Attribute('')
    # link_man = Attribute('')
    # phone = Attribute('')
    mark_reg_num = Attribute('')
    is_confirmed = Attribute('')
    is_reviewed = Attribute('')
    is_paid = Attribute('')
    created_at = Attribute('')
    updated_at = Attribute('')
    order_tpl = Attribute('mark/mark_transfer')
    base_type = Attribute('mark')
    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Attribute(False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Attribute(False)


class MarkTransferApplyBO(MarkTransferBaseBO):
    transfer_app_id = Attribute()
    transfer_app = Attribute('')
    acceptor_app_id = Attribute()
    acceptor_app = Attribute('')
    domestic_acc = Attribute('')
    domestic_acc_addr = Attribute('')
    domestic_acc_post_num = Attribute('')
    is_co_owner = Attribute(False)
    transfer_co_apps = Attribute(default=[], attri_type=list, split=',')
    acceptor_co_apps = Attribute(default=[], attri_type=list, split=',')


class MarkTransferReissueBO(MarkTransferBaseBO):
    applicant_id = Attribute('')
    apply_app_name = Attribute('')
    transfer_name = Attribute('')
    acceptor_name = Attribute('')


class MarkTransferInfoBO(BizModel):
    order_id = Attribute('', validators=Validators([Required()]))
    transfer_app_id = Attribute('', validators=Validators([Required()]),
                                v_condition=Condition('biz', 'mark_transfer_apply'))
    acceptor_app_id = Attribute('', validators=Validators([Required()]),
                                v_condition=Condition('biz', 'mark_transfer_apply'))
    domestic_acc = Attribute('')
    domestic_acc_addr = Attribute('')
    domestic_acc_post_num = Attribute('')

    biz = Attribute('', validators=Validators([Required(),
                                               In(['reissue_mark_transfer', 'mark_transfer_apply'])]))
    applicant_id = Attribute('', validators=Validators([Required()]),
                             v_condition=Condition('biz', 'reissue_mark_transfer'))


class MarkTransferMainBO(BizModel):
    order_id = Attribute('', validators=Validators([Required()]))
    mark_reg_num = Attribute('', validators=Validators([Required()]))
    biz = Attribute('', validators=Validators([Required(),
                                               In(['reissue_mark_transfer', 'mark_transfer_apply'])]))
    transfer_name = Attribute('', validators=Validators([Required()]),
                              v_condition=Condition('biz', 'reissue_mark_transfer'))
    acceptor_name = Attribute('', validators=Validators([Required()]),
                              v_condition=Condition('biz', 'reissue_mark_transfer'))


class MarkTransferCommonBO(BizModel):
    order_id = Attribute('', validators=Validators([Required()]))
    transfer_co_apps = Attribute(default=[], attri_type=list, split=',')
    acceptor_co_apps = Attribute(default=[], attri_type=list, split=',')