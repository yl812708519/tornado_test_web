#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger, String, Text, Boolean

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin

__author__ = 'zhaowenlei'

class CopyrightSoftOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(40))
    # 主体id
    applicant_id = Column(BigInteger)
    # 订单id
    order_id = Column(BigInteger)
    # 服务类别
    biz = Column(String(50), default='')
    # 名称
    soft_name = Column(String(100), default='')
    # 软件简称
    soft_abb = Column(String(50), default='')
    # version_num
    version_num = Column(String(20), default='')
    # 软件作品说明(原创，　修改(含翻译软件、合成软件)
    soft_description = Column(BigInteger, default=1)
    # 修改选择项
    modify_select = Column(String(50), default='')
    # 修改合成或翻译说明
    trans_description = Column(String(400), default='')
    # 软件开发完成日期
    soft_finish_date = Column(BigInteger)
    # 否发表(1:已发表，2:未发表)
    is_publish = Column(BigInteger, default=1)
    # 发表日期
    publish_date = Column(BigInteger)
    # 首次发表国家
    first_publish_country = Column(String(20), default='')
    # 首次发表城市
    first_publish_city = Column(String(20), default='')
    # 开发方式
    develop_way = Column(BigInteger, default=1)
    # 权利取得方式
    right_get_way = Column(BigInteger, default=1)
    # 继受取得(受让  承受  继承)
    acquisition_select = Column(BigInteger, default=1)
    # 软件是否已登记
    is_soft_reg = Column(BigInteger, default=0)
    # 原登记号
    source_reg_num = Column(String(30), default='')
    # 原登记是否做过变更或补充
    is_reg_num_change = Column(BigInteger, default=0)
    # 变更或补充证明编号
    change_reg_num = Column(String(150), default='')
    # 权利范围(全部１、部分２)
    right_range = Column(BigInteger, default=1)
    # 范围的部分选项
    range_select = Column(String(100), default='')
    # 硬件运行硬件环境
    hardware_env = Column(String(255), default='')
    # 软件运行软件环境
    software_env = Column(String(255), default='')
    # 编程语言
    pro_lan = Column(String(100), default='')
    # 源程序量
    source_pro_size = Column(String(40), default='')
    # 软件功能和技术特点
    function_feature = Column(String(700), default='')
    # 源程序
    source_program = Column(String(200), default='')
    # 程序使用说明书
    program_description = Column(String(200), default='')
    # 是否代填
    is_delegated = Column(Boolean, default=False)
    # 是否代填确认
    is_delegate_confirmed = Column(Boolean, default=False)
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Column(BigInteger, default=0)
    # 共有人选择
    common_app_ids = Column(String(200), default='')
    # 是否付款(0:未付款, 1:付款)
    is_paid = Column(BigInteger, default=0)
    # 表单确认字段
    is_confirm_able = Column(BigInteger, default=5)
    # 是否确认
    is_confirmed = Column(BigInteger, default=0)
    # 交存方式(一般交存、例外交存)
    deposit_way = Column(BigInteger, default=0)
    # 文档种类(一种文档、多种文档，种类为)
    file_type = Column(BigInteger, default=0)
    # 多种文档，种类数
    file_type_num = Column(BigInteger, default=0)
    # 使用黑色宽斜线覆盖、前10页和任选连续的50、目标程序的连续的前、后各30页和源程序任选连续的20页
    page_select_way = Column(BigInteger, default=0)
    # 使用黑色宽斜线覆盖，页码为：XX
    page_num = Column(BigInteger, default=0)
    # 软件著作权申请书(又后台上传)
    requisition = Column(String(200), default='')
    # 创建时间
    created_at = Column(BigInteger)
    # 更新时间
    updated_at = Column(BigInteger)
    # 软件基本信息部分是否完成
    is_info_finished = Column(Boolean, default=False)
    turn_num = Column(String(50), default='')

@model(CopyrightSoftOrder)
class CopyrightSoftOrderDao(DatabaseTemplate):

    def get_by_order_user(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(CopyrightSoftOrder.user_id == user_id,
                   CopyrightSoftOrder.order_id == order_id).first()

    def get_by_order_id(self, order_id, user_id):
        return self.session.query(self.model_cls).\
            filter(CopyrightSoftOrder.user_id == user_id,
                   CopyrightSoftOrder.order_id == order_id).first()

    def get_by_order(self, order):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id,
                   self.model_cls.user_id == user_id).first()