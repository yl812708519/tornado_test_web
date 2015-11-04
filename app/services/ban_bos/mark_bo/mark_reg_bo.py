#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition


class MarkRegOrderBO(BizModel):
    id = Attribute()
    # 订单编号
    order_id = Attribute(0)

    # 业务类型
    biz = Attribute('')

    # 用户id
    user_id = Attribute(0)

    # 商标名称
    name = Attribute('')

    # 商标描述
    description = Attribute('')

    # 商标图片
    mark_img = Attribute('')
    # 是否指定颜色
    is_specify_color = Attribute(False)

    # 商标类型
    mark_type = Attribute('')

    collective_list = Attribute('')
    collective_list_url = Attribute('')

    # 申请主体id
    applicant_id = Attribute('')
    applicant = Attribute('')

    # 商标类别
    category = Attribute('')
    category_name = Attribute('')

    # 商标小项树结构(使用json数据结构)
    itemtree = Attribute(default=[], split=',', attri_type=list)
    itemtree_names = Attribute(default=[], attri_type=list)

    # 商标小项（以,进行分割，小项最多增加到100）
    items = Attribute(default=[], split=',', attri_type=list)
    item_names = Attribute(default=[], attri_type=list)

    # 以3维方式注册
    is_three_d = Attribute(False)

    # 3D 五面图片
    three_d_image = Attribute('')

    # 以颜色组合注册
    is_color = Attribute(False)

    # 颜色组合图片
    color_image = Attribute('')

    # 以声音标志注册
    is_voice = Attribute(False)

    # 声音文件
    voice_file = Attribute('')
    voice_file_url = Attribute('')

    # 以肖像权注册
    is_portrait = Attribute(False)

    # 肖像图片
    portrait_img = Attribute('')

    # 共同申请人
    is_co_applicants = Attribute(False)

    # 共同申请人id json
    co_applicant_ids = Attribute(default=[], split=',', attri_type=list)
    co_applicants = Attribute(default=[], attri_type=list)

    # 优先权 no:否 before:在先优先权 exhibition:展会优先权
    is_prority = Attribute('no')

    # 优先权-申请/展出国家/地区
    prority_app_region = Attribute('')

    # 优先权-申请/展出日期 (yyyy-MM-dd)
    prority_app_date = Attribute('')

    # 优先权-申请号
    prority_app_serial_num = Attribute('')

    # 商标申请号
    app_serial_num = Attribute('')

    # 上传的管理规则文件(集体商标注册 和 证明商标注册有此项)
    regulation_file = Attribute('')
    regulation_file_url = Attribute('')

    # 是否付款
    is_paid = Attribute(False)

    # 是否已确认(确认后将不可修改，可以由后台客服修改当前的状态)
    is_confirmed = Attribute(False)

    # 是否已复查(审查通过后就可以下载资料)
    is_reviewed = Attribute(False)

    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Attribute(False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Attribute(False)
    # 表示不同业务使用的模板
    order_tpl = Attribute('mark/mark_reg')
    base_type = Attribute('mark')


class MarkApplicantBO(BizModel):
    # 订单编号
    order_id = Attribute(0)
    # 申请主体id
    applicant_id = Attribute(default=0, validators=Validators([Required()]))
    # 共同申请人
    is_co_applicants = Attribute(False, validators=Validators([Required()]), attri_type=bool)
    # 共同申请人id json
    co_applicant_ids = Attribute(default=[], attri_type=list, split=',', validators=Validators([Required()]),
                                 v_condition=Condition('is_co_applicants', 1))


class MarkInfoBO(BizModel):
    # 订单编号
    order_id = Attribute(0, validators=Validators([Required()]))
    # 订单类型：用于判断 集体成员名单、商标管理规则
    biz = Attribute('', validators=Validators([Required()]))
    # 商标名称
    name = Attribute('', validators=Validators([Required()]))
    # 商标描述
    description = Attribute('', validators=Validators([Required()]))
    # 商标图片
    mark_img = Attribute('', validators=Validators([Required()]))
    # 是否指定颜色
    is_specify_color = Attribute(False, validators=Validators([Required()]))
    # 上传的管理规则文件(集体商标注册 和 证明商标注册有此项)
    regulation_file = Attribute('', validators=Validators([Required()]),
                                v_condition=Condition('biz', ('collective_mark_reg', 'prove_mark_reg')))
    # 集体成员名单
    collective_list = Attribute('', validators=Validators([Required()]),
                                v_condition=Condition('biz', 'collective_mark_reg'))


class MarkCategoryBO(BizModel):
    # 订单编号
    order_id = Attribute(0)
    # 商标类别
    category = Attribute('', validators=Validators([Required()]))

    # 商标小项树结构(使用json数据结构)
    itemtree = Attribute(default=[], attri_type=list, split=',', validators=Validators([Required()]))

    # 商标小项（以,进行分割，小项最多增加到100）
    items = Attribute(default=[], attri_type=list, split=',', validators=Validators([Required()]))


class MarkAttachBO(BizModel):
    # 订单编号
    order_id = Attribute(0)
    # 以3维方式注册
    is_three_d = Attribute(False, attri_type=bool)

    # 3D 五面图片
    three_d_image = Attribute('', validators=Validators([Required()]),
                              v_condition=Condition('is_three_d', 1))

    # 以颜色组合注册
    is_color = Attribute(False, attri_type=bool)

    # 颜色组合图片
    color_image = Attribute('', validators=Validators([Required()]),
                            v_condition=Condition('is_color', 1))

    # 以声音标志注册
    is_voice = Attribute(False, attri_type=bool)

    # 声音文件
    voice_file = Attribute('', validators=Validators([Required()]),
                           v_condition=Condition('is_voice', 1))

    # 以肖像权注册
    is_portrait = Attribute(False, attri_type=bool)

    # 肖像图片
    portrait_img = Attribute('', validators=Validators([Required()]),
                             v_condition=Condition('is_portrait', 1))
    # 优先权 no:否 before:在先优先权 exhibition:展会优先权
    is_prority = Attribute('no')

    # 优先权-申请/展出国家/地区
    prority_app_region = Attribute('', validators=Validators([Required()]),
                                   v_condition=Condition('is_prority', ('before', 'exhibition')))

    # 优先权-申请/展出日期 (yyyy-MM-dd)
    prority_app_date = Attribute('', validators=Validators([Required()]),
                                 v_condition=Condition('is_prority', ('before', 'exhibition')))

    # 优先权-申请号
    prority_app_serial_num = Attribute('', validators=Validators([Required()]),
                                       v_condition=Condition('is_prority', ('before')))