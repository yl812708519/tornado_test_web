#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.services.ban_bos.applicant import ApplicantBO
from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition


class MarkChangeOrderBO(BizModel):

    id = Attribute(default=None)
    # 用户id
    user_id = Attribute()

    # 订单id
    order_id = Attribute()

    # 服务类别
    biz = Attribute()

    # 主体id
    applicant_id = Attribute()
    applicant = Attribute(default=ApplicantBO(), attri_type=ApplicantBO)

    # 是否有共有人
    is_co_applicants = Attribute()

    # 共有人app_ids
    co_app_ids = Attribute(attri_type=list, split=',')
    co_apps = Attribute(attri_type=list, generic_type=ApplicantBO)

    # 是否共有人变更
    is_co_app_changed = Attribute()

    # 变更前共有人
    before_co_app_ids = Attribute(attri_type=list, split=',')
    before_co_apps = Attribute(attri_type=list, generic_type=ApplicantBO)

    # 变更后共有人
    after_co_app_ids = Attribute(attri_type=list, split=',')
    after_co_apps = Attribute(attri_type=list, generic_type=ApplicantBO)

    # 商标注册号
    mark_reg_num = Attribute()

    # 删减商标分类
    cut_category = Attribute(attri_type=list, split=',')

    # 删减上篇/服务项目
    cut_items = Attribute()

    # 变更后文件接收人
    changed_recv_name = Attribute()

    # 变更后邮政编码
    changed_post_num = Attribute()

    # 变更后邮政编码
    changed_recv_addr = Attribute()

    # 变更前申请人姓名
    before_app_name = Attribute()

    #
    before_app_name_en = Attribute()

    # 变更前申请人地址
    before_app_addr = Attribute()

    #
    before_app_addr_en = Attribute()

    # 是否变更管理规则
    is_rule_changed = Attribute()

    # 变更前规则
    before_rule = Attribute()

    # 上传变更后规则
    after_rule = Attribute()

    # 是否有变更集体成员名单(0:否 1:没有)
    is_collective_changed = Attribute()

    # 上传变更前集体成员名单
    before_collective = Attribute()

    # 上传变更后集体成员名单
    after_collective = Attribute()

    #
    is_confirm_able = Attribute()

    #
    is_delegated = Attribute()

    #
    is_delegate_confirmed = Attribute()

    #
    is_reviewed = Attribute()

    created_at = Attribute(None)
    order_tpl = Attribute('mark/mark_change')
    base_type = Attribute('mark')
    # applicant = Attribute(None)


class MarkChangeApplicantBO(BizModel):

    order_id = Attribute(validators=Validators([Required()]))
    biz = Attribute(validators=Validators([Required()]))
    applicant_id = Attribute(validators=Validators([Required()]))
    is_co_applicants = Attribute(validators=Validators([Required()]), attri_type=bool)
    co_applicant_ids = Attribute(validators=Validators([Required()]), attri_type=list, split=',',
                                 v_condition=Condition('is_co_applicants', 1))
    # 变更申请人/注册人名义/地址/变更集体/证明商标管理规划/集体成员名单

    is_co_app_changed = Attribute(validators=Validators([Required()]), attri_type=bool,
                                  v_condition=Condition('biz', 'reg_col_pro_applicant'))
    before_co_app_ids = Attribute(validators=Validators([Required()]), attri_type=list, split=',',
                                  v_condition=Condition('is_co_app_changed', '1'))
    after_co_app_ids = Attribute(validators=Validators([Required()]), attri_type=list, split=',',
                                 v_condition=Condition('is_co_app_changed', '1'))


class MarkChangeInfoBO(BizModel):

    order_id = Attribute(validators=Validators([Required()]))
    biz = Attribute(validators=Validators([Required()]))
    mark_reg_num = Attribute(validators=Validators([Required()]))

    # 变更申请人/注册人名义/地址/变更集体/证明商标管理规划/集体成员名单

    before_app_name = Attribute(validators=Validators([Required()]),
                                v_condition=Condition('biz', 'reg_col_pro_applicant'))
    before_app_name_en = Attribute(validators=Validators([Required()]),
                                   v_condition=Condition('biz', 'reg_col_pro_applicant'))
    before_app_addr = Attribute(validators=Validators([Required()]),
                                v_condition=Condition('biz', 'reg_col_pro_applicant'))
    before_app_addr_en = Attribute(validators=Validators([Required()]),
                                   v_condition=Condition('biz', 'reg_col_pro_applicant'))
    # 变更商标代理人/文件接收人申请

    changed_recv_name = Attribute(validators=Validators([Required()]),
                                  v_condition=Condition('biz', 'age_rec_applicant'))
    changed_post_num = Attribute(validators=Validators([Required()]),
                                 v_condition=Condition('biz', 'age_rec_applicant'))
    changed_recv_addr = Attribute(validators=Validators([Required()]),
                                  v_condition=Condition('biz', 'age_rec_applicant'))

    # 删减商标分类/服务项目

    cut_category = Attribute(validators=Validators([Required()]), attri_type=list, split=',',
                             v_condition=Condition('biz', 'sub_service_applicant'))
    cut_items = Attribute(validators=Validators([Required()]),
                          v_condition=Condition('biz', 'sub_service_applicant'))


class MarkChangeAttachBO(BizModel):

    order_id = Attribute(validators=Validators([Required()]))
    biz = Attribute(validators=Validators([Required()]))

    # 变更申请人/注册人名义/地址/变更集体/证明商标管理规划/集体成员名单

    is_rule_changed = Attribute(attri_type=bool, validators=Validators([Required()]))
    before_rule = Attribute(validators=Validators([Required()]),
                            v_condition=Condition('is_rule_changed', 1))
    after_rule = Attribute(validators=Validators([Required()]),
                           v_condition=Condition('is_rule_changed', 1))

    is_collective_changed = Attribute(attri_type=bool, validators=Validators([Required()]))
    before_collective = Attribute(validators=Validators([Required()]),
                                  v_condition=Condition('is_collective_changed', 1))
    after_collective = Attribute(validators=Validators([Required()]),
                                 v_condition=Condition('is_collective_changed', 1))
