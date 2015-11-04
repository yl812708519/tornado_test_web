#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger, String, Text, Boolean

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin

__author__ = 'zhaowenlei'

class CopyrightOpusOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(40))
    # 主体id
    applicant_id = Column(BigInteger)
    # 订单id
    order_id = Column(BigInteger)
    # 服务类别
    biz = Column(String(50), default='')
    # 作品名称
    opus_name = Column(String(200), default='')
    # 作品样本
    opus_sample = Column(String(200), default='')
    # 作者姓名或名称
    author_name = Column(String(80), default='')
    # 作品创作性质
    opus_nature = Column(BigInteger, default=1)
    # 作品创作性质说明(除原创外，都应该填写创作说明)
    nature_description = Column(String(200), default='')
    # 创作完成日期
    opus_finish_date = Column(BigInteger)
    # 完成创作国家
    opus_finish_country = Column(String(20), default='')
    # 完成创作城市
    opus_finish_city = Column(String(20), default='')
    # 发表状态（已发表、未发表）
    publish_status = Column(BigInteger, default=1)
    # 首次发表时间
    first_publish_date = Column(BigInteger)
    # 首次发表国家
    first_publish_country = Column(String(20), default='')
    # 首次发表城市
    first_publish_city = Column(String(20), default='')
    # 权利取得方式
    right_get_way = Column(BigInteger, default=1)
    # 权利取得方式说明(当权利取得方式选择“其他”时,填写此项)
    right_get_description = Column(String(200), default='')
    # 权利归属方式
    right_ascription_way = Column(BigInteger, default=1)
    # 权利归属方式说明
    right_ascription = Column(String(200), default='')
    # 权利拥有状况(全部、部分)
    right_own_state = Column(BigInteger, default=1)
    # 权利拥有选择(部分的选项)
    right_own_select = Column(String(200), default='')
    # 权利拥有状态说明
    right_own_des = Column(String(200), default='')
    # 创作目的
    opus_purpose = Column(Text, default='')
    # 创作过程
    opus_process = Column(Text, default='')
    # 创作独创性
    opus_alone_create = Column(Text, default='')
    # 作品著作权申请书
    requisition = Column(String(200), default='')
    # 是否代填
    is_delegated = Column(Boolean, default=0)
    # 是否代填确认
    is_delegate_confirmed = Column(Boolean, default=0)
    # 是否有共同申请人(0:否 1:没有)
    is_common_app = Column(BigInteger, default=0)
    # 是否付款(0:未付款, 1:付款)
    is_paid = Column(BigInteger, default=0)
    # 电子介质
    dielectric = Column(String(200), default='')
    # 电子介质(件)
    dielectric_piece = Column(BigInteger)
    # 纸介质
    paper_medium = Column(BigInteger)
    # 纸介质(张)
    paper_medium_page = Column(BigInteger)
    # 表单确认字段
    is_confirm_able = Column(BigInteger, default=4)
    # 共有人选择
    common_app_ids = Column(String(200), default='')
    # 是否已确认(确认后将不可修改，可以由后台客服修改当前的状态)
    is_confirmed = Column(BigInteger, default=0)
    # 作品基本信息是否完成
    is_info_finished = Column(Boolean, default=False)
    # 作品状态说明是否完成
    is_des_finished = Column(Boolean, default=False)
    # 版权类型
    opus_type = Column(String(20), default='')
    turn_num = Column(String(50), default='')


@model(CopyrightOpusOrder)
class CopyrightOpusOrderDao(DatabaseTemplate):

    def get_by_order_user(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(CopyrightOpusOrder.user_id == user_id,
                   CopyrightOpusOrder.order_id == order_id).first()

    def get_by_order_id(self, order_id, user_id):
        return self.session.query(self.model_cls).\
            filter(CopyrightOpusOrder.user_id == user_id,
                   CopyrightOpusOrder.order_id == order_id).first()

    def get_by_order(self, order):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id,
                   self.model_cls.user_id == user_id).first()