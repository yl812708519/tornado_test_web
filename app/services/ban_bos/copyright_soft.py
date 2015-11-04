#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, MaxLength, MinLength, Condition

__author__ = 'zhaowenlei'


class CopyrightSoftCommonBO(BizModel):
    # 用户id
    user_id = Attribute('')
    # 订单id
    order_id = Attribute('')

class CopyrightSoftReqBO(CopyrightSoftCommonBO):
    """软件版权提交BO

    """
    id = Attribute(None)
    # 主体id
    applicant_id = Attribute('')
    # 服务类别
    biz = Attribute(default='')
    # 名称
    soft_name = Attribute(default='')
    # 软件简称
    soft_abb = Attribute(default='')
    # 版本号
    version_num = Attribute(default='')
    # 软件作品说明(原创，　修改(含翻译软件、合成软件)
    soft_description = Attribute(default=1)
    # 修改选择项
    modify_select = Attribute(default='')
    # 修改合成或翻译说明
    trans_description = Attribute(default='')
    # 软件开发完成日期
    soft_finish_date = Attribute(default='')
    # 否发表(1:已发表，2:未发表)
    is_publish = Attribute('')
    # 发表日期
    publish_date = Attribute(default='')
    # 首次发表国家
    first_publish_country = Attribute(default='')
    # 首次发表城市权利范围
    first_publish_city = Attribute(default='')
    # 开发方式
    develop_way = Attribute(default=0)
    # 权利取得方式
    right_get_way = Attribute(default=0)
    # 继受取得(受让  承受  继承)
    acquisition_select = Attribute(default=0)
    # 软件是否已登记
    is_soft_reg = Attribute(default=0)
    # 原登记号
    source_reg_num = Attribute(default='')
    # 原登记是否做过变更或补充
    is_reg_num_change = Attribute(default=0)
    # 变更或补充证明编号
    change_reg_num = Attribute(default='')
    # 权利范围(全部１、部分２)
    right_range = Attribute(default=0)
    # 范围的部分选项
    range_select = Attribute(default='')
    # 硬件运行硬件环境
    hardware_env = Attribute(default='')
    # 软件运行软件环境
    software_env = Attribute(default='')
    # 编程语言
    pro_lan = Attribute(default='')
    # 源程序量
    source_pro_size = Attribute(default='')
    # 软件功能和技术特点
    function_feature = Attribute(default='')
    # 源程序
    source_program = Attribute(default='')
    # 程序使用说明书
    program_description = Attribute(default='')
    # 是否代填
    is_delegated = Attribute(default=False)
    # 是否代填确认
    is_delegate_confirmed = Attribute(default=False)
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Attribute(default=0)
    # 共有人选择
    common_app_ids = Attribute(default='')
    # 是否付款(0:未付款, 1:付款)
    is_paid = Attribute(default=0)
    # 表单确认字段
    is_confirm_able = Attribute(default=5)
    # 是否确认
    is_confirmed = Attribute(default=0)
    # 交存方式(一般交存、例外交存)
    deposit_way = Attribute(default=0)
    # 文档种类(一种文档、多种文档，种类为)
    file_type = Attribute(default=0)
    # 多种文档，种类数
    file_type_num = Attribute(default=0)
    # 使用黑色宽斜线覆盖、前10页和任选连续的50、目标程序的连续的前、后各30页和源程序任选连续的20页
    page_select_way = Attribute(default=0)
    # 使用黑色宽斜线覆盖，页码为：XX
    page_num = Attribute(default=0)
    today = Attribute('')
    # 软件著作权申请书(又后台上传)
    requisition = Attribute(default='')
    copyright_owner = Attribute('')
    parks = Attribute('')
    provinces = Attribute('')
    opus_type = Attribute('')
    turn_num = Attribute(default='')

class CopyrightSoftRespBO(CopyrightSoftReqBO):
    """软件版权详情BO

    """
    right_ranges = Attribute(default='')
    # 软件著作权申请书(又后台上传)
    requisition = Attribute(default='')
    common_app_applicants = Attribute('')
    order_tpl = Attribute('copyright/copyright_soft')
    base_type = Attribute('copyright')
    applicant = Attribute('')
    titles = Attribute('')
    soft_description_title = Attribute('')
    is_publish_title = Attribute('')
    develop_way_title = Attribute('')
    right_get_way_title = Attribute('')
    right_range_title = Attribute('')
    is_info_finished = Attribute('')


class CopyrightSoftOrderApplicantReqBO(CopyrightSoftCommonBO):
    """更新主体BO

    """
    # 主体id
    applicant_id = Attribute(None, validators=Validators([Required()], name='主体'))
    # 软件基本信息部分是否完成
    is_info_finished = Attribute(default=False)
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Attribute(default=0)
    # 共有人选择
    common_app_ids = Attribute(default='', validators=Validators([Required()], name='共同申请人'), split=',',
                               v_condition=Condition('is_common_app', 1), attri_type=list, generic_type=int)

class CopyrightSoftOrderInfoReqBO(CopyrightSoftCommonBO):
    """更新软件信息bo

    """
    # 名称
    soft_name = Attribute(default='', validators=Validators([Required(), MaxLength(200)], name='软件名称'))
    # 软件简称
    soft_abb = Attribute(default='', validators=Validators([MaxLength(100)], name='软件简称'))
    # 版本号
    version_num = Attribute(default='', validators=Validators([Required(), MaxLength(40)], name='版本号'))
    # 软件作品说明(原创，　修改(含翻译软件、合成软件)
    soft_description = Attribute(default=0)
    # 修改选择项
    modify_select = Attribute(default='', validators=Validators([Required()], name='修改选择项'),split=',',
                              v_condition=Condition('soft_description', 2), attri_type=list, generic_type=int)
    # 修改合成或翻译说明
    trans_description = Attribute(default='', validators=Validators([Required(), MaxLength(400)], name='修改合成或翻译说明'),
                                  v_condition=Condition('soft_description', 2))
    # 软件开发完成日期
    soft_finish_date = Attribute(default='', validators=Validators([Required()], name='软件开发完成日期'), time_stamp=True)
    # 否发表(1:已发表，2:未发表)
    is_publish = Attribute(default='')
    # 发表日期
    publish_date = Attribute(default='', validators=Validators([Required()], name='发表日期'),
                             v_condition=Condition('is_publish', 1), time_stamp=True)
    # 首次发表国家
    first_publish_country = Attribute(default='', validators=Validators([Required()], name='首次发表国家'),
                                      v_condition=Condition('is_publish', 1))
    # 首次发表城市
    first_publish_city = Attribute(default='', validators=Validators([Required()], name='首次发表城市'),
                                   v_condition=Condition('is_publish', 1))
    # 开发方式
    develop_way = Attribute(default=0)
    # 权利取得方式
    right_get_way = Attribute(default=1)
    # 继受取得(受让  承受  继承)
    acquisition_select = Attribute(default=1)
    # 软件是否已登记
    is_soft_reg = Attribute(default=0)
    # 原登记号
    source_reg_num = Attribute(default='', validators=Validators([Required(), MaxLength(30)], name='原登记号'),
                               v_condition=Condition('is_soft_reg', 1))
    # 原登记是否做过变更或补充
    is_reg_num_change = Attribute(default=0)
    # 变更或补充证明编号
    change_reg_num = Attribute(default='', validators=Validators([Required(), MaxLength(150)], name='变更或补充证明编号'),
                               v_condition=Condition('is_reg_num_change', 1))
    # 权利范围(全部１、部分２)
    right_range = Attribute(default=1)
    # 范围的部分选项
    range_select = Attribute(default='', validators=Validators([Required()], name='选择部分选项时，请选择以下选项'),
                             split=',', v_condition=Condition('right_range', 2), attri_type=list)

class CopyrightSoftOrderFeatureReqBO(CopyrightSoftCommonBO):
    """软件版权特点bo

    """
    # 硬件运行硬件环境
    hardware_env = Attribute(default='', validators=Validators([Required(), MaxLength(255)], name='硬件运行硬件环境'))
    # 软件运行软件环境
    software_env = Attribute(default='', validators=Validators([Required(), MaxLength(255)], name='软件运行软件环境'))
    # 编程语言
    pro_lan = Attribute(default='', validators=Validators([Required(), MaxLength(100)], name='编程语言'))
    # 源程序量
    source_pro_size = Attribute(default='', validators=Validators([Required(), MaxLength(40)], name='源程序量'))
    # 软件功能和技术特点
    function_feature = Attribute(default='', validators=Validators([Required(), MaxLength(700)], name='软件功能和技术特点'))


class CopyrightSoftOrderAttachReqBO(CopyrightSoftCommonBO):
    """附加信息bo

    """
    # 源程序
    source_program = Attribute(default='')
    # 程序使用说明书
    program_description = Attribute(default='')