#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, Condition, MaxLength

__author__ = 'zhaowenlei'


class CopyrightOpusOrderCommonBO(BizModel):
    # 用户id
    user_id = Attribute('')
    # 订单id
    order_id = Attribute(None)


class CopyrightOpusReqBO(CopyrightOpusOrderCommonBO):
    """软件版权提交BO

    """
    id = Attribute(None)
    # 主体id
    applicant_id = Attribute(None)
    # 服务类别
    biz = Attribute(default='')
    # 作品名称
    opus_name = Attribute(default='')
    # 作品样本
    opus_sample = Attribute(default='')
    # 作者姓名或名称
    author_name = Attribute(default='')
    # 作品创作性质
    opus_nature = Attribute(default=0)
    # 作品创作性质说明(除原创外，都应该填写创作说明)
    nature_description = Attribute(default='')
    # 创作完成日期
    opus_finish_date = Attribute('')
    # 完成创作国家
    opus_finish_country = Attribute(default='')
    # 完成创作城市
    opus_finish_city = Attribute(default='')
    # 发表状态（已发表、未发表）
    publish_status = Attribute(default=0)
    # 首次发表时间
    first_publish_date = Attribute('')
    # 首次发表国家
    first_publish_country = Attribute(default='')
    # 首次发表城市
    first_publish_city = Attribute(default='')
    # 权利取得方式
    right_get_way = Attribute(default=0)
    # 权利取得方式说明(当权利取得方式选择“其他”时,填写此项)
    right_get_description = Attribute(default='')
    # 权利归属方式
    right_ascription_way = Attribute(default=0)
    # 权利归属方式说明
    right_ascription = Attribute(default='')
    # 权利拥有状况(全部、部分)
    right_own_state = Attribute(default=0)
    # 权利拥有状态说明
    right_own_des = Attribute(default='')
    # 权利拥有选择(部分的选项)
    right_own_select = Attribute(default='')
    # 创作目的
    opus_purpose = Attribute(default='')
    # 创作过程
    opus_process = Attribute(default='')
    # 创作独创性
    opus_alone_create = Attribute(default='')
    # 作品著作权申请书
    requisition = Attribute(default='')
    # 是否代填
    is_delegated = Attribute(default=0)
    # 是否代填确认
    is_delegate_confirmed = Attribute(default=0)
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Attribute(default=0)
    # 是否付款(0:未付款, 1:付款)
    is_paid = Attribute(default=0)
    # 电子介质
    dielectric = Attribute(default='')
    # 电子介质(件)
    dielectric_piece = Attribute(None)
    # 纸介质
    paper_medium = Attribute(None)
    # 纸介质(张)
    paper_medium_page = Attribute(None)
    # 共有人选择
    common_app_ids = Attribute(default='')
    # 作品署名(后台有)
    opus_signature = Attribute(default='')


class CopyrightOpusResBO(CopyrightOpusReqBO):
    """软件版权详情BO

    """
    common_app_applicants = Attribute('')
    order_tpl = Attribute('copyright/copyright_opus')
    base_type = Attribute('copyright')
    applicant = Attribute('')
    right_own_selects = Attribute('')
    status_fields = Attribute('')
    opus_nature_title = Attribute('')
    publish_status_title = Attribute('')
    right_get_way_title = Attribute('')
    right_ascription_way_title = Attribute('')
    right_own_state_title = Attribute('')
    is_info_finished = Attribute('')
    is_des_finished = Attribute('')
    flag = Attribute('')
    today = Attribute('')
    copyright_owner = Attribute('')
    parks = Attribute('')
    provinces = Attribute('')
    opus_type = Attribute('')
    turn_num = Attribute(default='')


class CopyrightOpusOrderApplicantReqBO(CopyrightOpusOrderCommonBO):
    """更新主体BO

    """
    # 主体id
    applicant_id = Attribute(None, validators=Validators([Required()], name='主体'))
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Attribute(default=0)
    # 共有人选择
    common_app_ids = Attribute(default='', validators=Validators([Required()], name='共同申请人'), split=',',
                               v_condition=Condition('is_common_app', 1), attri_type=list, generic_type=int)


class CopyrightOpusOrderInfoReqBO(CopyrightOpusOrderCommonBO):

    # 作品名称
    opus_name = Attribute(default='',  validators=Validators([Required(), MaxLength(200)], name='作品名称'))
    # 作者姓名或名称
    author_name = Attribute(default='', validators=Validators([Required(), MaxLength(80)], name='作者姓名或名称'))
    # 作品创作性质
    opus_nature = Attribute(default=1)
    # 作品创作性质说明(除原创外，都应该填写创作说明)
    nature_description = Attribute(default='', validators=Validators([MaxLength(200)], name='作品创作性质说明'))
    # 创作完成日期
    opus_finish_date = Attribute(default='', validators=Validators([Required()], name='创作完成日期'), time_stamp=True)
    # 完成创作国家
    opus_finish_country = Attribute(default='', validators=Validators([Required()], name='完成创作国家'))
    # 完成创作城市
    opus_finish_city = Attribute(default='', validators=Validators([Required()], name='完成创作城市'))
    # 首次发表国家
    first_publish_country = Attribute(default='', validators=Validators([Required()], name='首次发表国家'),
                                      v_condition=Condition('publish_status', 1))
    # 首次发表城市
    first_publish_city = Attribute(default='', validators=Validators([Required()], name='首次发表城市'),
                                   v_condition=Condition('publish_status', 1))
    # 发表状态（1已发表、2 未发表）
    publish_status = Attribute(default=1)
    # 首次发表时间
    first_publish_date = Attribute(default='', validators=Validators([Required()], name='首次发表时间'),
                                   v_condition=Condition('publish_status', 1), time_stamp=True)
    # 作品样本
    opus_sample = Attribute(default='', validators=Validators([Required()], name='作品样本'))


class CopyrightOpusOrderAttReqBO(CopyrightOpusOrderCommonBO):

    # 权利取得方式
    right_get_way = Attribute(default=0)
    # 权利取得方式说明(当权利取得方式选择“其他”时,填写此项)
    right_get_description = Attribute(default='', validators=Validators([MaxLength(200)]))
    # 权利归属方式
    right_ascription_way = Attribute(default=1)
    # 权利归属方式说明
    right_ascription = Attribute(default='', validators=Validators([Required()], name='权利归属方式说明'))
    # 权利拥有状况(全部、部分)
    right_own_state = Attribute(default=1)
    # 权利拥有选择(部分的选项)
    right_own_select = Attribute(default='', validators=Validators([Required()], name='请选择权利拥有状况'), split=',',
                                 v_condition=Condition('right_own_state', 2), attri_type=list, generic_type=int)
    # 创作目的
    opus_purpose = Attribute(default='', validators=Validators([Required()], name='创作目的'))
    # 创作过程
    opus_process = Attribute(default='', validators=Validators([Required()], name='创作过程'))
    # 创作独创性
    opus_alone_create = Attribute(default='', validators=Validators([Required()], name='创作独创性'))
    # 权利拥有状态说明
    right_own_des = Attribute(default='', validators=Validators([MaxLength(200)]))