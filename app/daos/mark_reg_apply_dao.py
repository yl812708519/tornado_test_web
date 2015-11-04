#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, SmallInteger
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class MarkRegApplyOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    user_id = Column(String(36), default='')
    order_id = Column(BigInteger, default='')
    applicant_id = Column(BigInteger, default='')
    # link_man = Column(String(40), default='')
    # post_num = Column(String(40), default='')
    # phone = Column(String(40), default='')
    # agency = Column(String(40), default='')
    mark_reg_num = Column(String(255), default='')
    biz = Column(String(40), default='')
    reissue_reason = Column(String(255), default='')
    category_codes = Column(String(255), default='')
    is_reset = Column(Boolean, default=False)
    correct_items = Column(String(2000), default='')
    is_paid = Column(Boolean, default=False)
    is_confirm_able = Column(SmallInteger, default=3)
    is_confirmed = Column(Boolean, default=False)
    is_reviewed = Column(Boolean, default=False)
    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Column(Boolean, default=False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Column(Boolean, default=False)


@model(MarkRegApplyOrder)
class MarkRegApplyDao(DatabaseTemplate):

    def get_by_id_user(self, apply_id, uid):
        return self.session.query(self.model_cls).\
            filter(MarkRegApplyOrder.id == apply_id).\
            filter(MarkRegApplyOrder.user_id == uid).first()

    def get_by_order_user(self, order_id, uid):
        return self.session.query(self.model_cls).\
            filter(MarkRegApplyOrder.order_id == order_id).\
            filter(MarkRegApplyOrder.user_id == uid).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.get_by_order_user(order_id, user_id)

    def get_by_order(self, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).first()