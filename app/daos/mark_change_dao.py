#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, DateTime, Float
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin,  CreatedAtMixin, UpdatedAtMixin


class MarkChangeOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(40))

    # 订单id
    order_id = Column(BigInteger, default=None)

    # 服务类别
    biz = Column(String(50), default='')

    # 主体id
    applicant_id = Column(BigInteger, default=0)

    # 是否有共有人
    is_co_applicants = Column(Boolean, default=False)

    # 共有人app_ids
    co_app_ids = Column(String(400), default='')

    # 是否共有人变更
    is_co_app_changed = Column(Boolean, default=False)

    # 变更前共有人
    before_co_app_ids = Column(String(400), default='')

    # 变更后共有人
    after_co_app_ids = Column(String(400), default='')

    # 商标注册号
    mark_reg_num = Column(String(40), default='')

    # 删减商标分类
    cut_category = Column(String(4), default='')

    # 删减上篇/服务项目
    cut_items = Column(String(1000), default='')

    # 变更后文件接收人
    changed_recv_name = Column(String(200), default='')

    # 变更后邮政编码
    changed_post_num = Column(String(10), default='')

    # 变更后邮政编码
    changed_recv_addr = Column(String(200), default='')

    # 变更前申请人姓名
    before_app_name = Column(String(40), default='')

    #
    before_app_name_en = Column(String(50), default='')

    # 变更前申请人地址
    before_app_addr = Column(String(200), default='')

    #
    before_app_addr_en = Column(String(200), default='')

    # 是否变更管理规则
    is_rule_changed = Column(Boolean, default=False)

    # 变更前规则
    before_rule = Column(String(200), default='')

    # 上传变更后规则
    after_rule = Column(String(200), default='')

    # 是否有变更集体成员名单(0:否 1:没有)
    is_collective_changed = Column(Boolean, default=False)

    # 上传变更前集体成员名单
    before_collective = Column(String(200), default='')

    # 上传变更后集体成员名单
    after_collective = Column(String(200), default='')

    #
    is_confirm_able = Column(BigInteger, default=0)

    #
    is_delegated = Column(Boolean, default=False)

    #
    is_delegate_confirmed = Column(Boolean, default=False)

    #
    is_reviewed = Column(Boolean, default=False)

    #
    is_paid = Column(Boolean, default=False)


@model(MarkChangeOrder)
class MarkChangeOrderDao(DatabaseTemplate):

    def update_applicant_by_id(self, user_id, mark_change_id, applicant_id):
        return self.session.query(self.model_cls).\
            filter(MarkChangeOrder.id == mark_change_id,
                   MarkChangeOrder.user_id == user_id).\
            update({MarkChangeOrder.applicant_id: applicant_id})

    def get_by_order_user(self, order_id, user_id):
        return self.session.query(self.model_cls).\
            filter(MarkChangeOrder.user_id == user_id,
                   MarkChangeOrder.order_id == order_id).first()

    def get_by_order(self, order):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id,
                   self.model_cls.user_id == user_id).first()