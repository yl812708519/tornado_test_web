# /usr/env/bin python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, SmallInteger
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class MarkTransferOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    user_id = Column(String(36), default=None)
    order_id = Column(BigInteger, default=None)
    biz = Column(String(30), default='')
    transfer_app_id = Column(BigInteger, default='')
    acceptor_app_id = Column(BigInteger, default='')
    # post_num = Column(String(20), default='')
    # link_man = Column(String(20), default='')
    # phone = Column(String(20), default='')
    domestic_acc = Column(String(50), default='')
    domestic_acc_addr = Column(String(100), default='')
    domestic_acc_post_num = Column(String(20), default='')
    mark_reg_num = Column(String(255), default='')
    is_co_owner = Column(Boolean, default=False)
    transfer_co_apps = Column(String(1000), default='')
    acceptor_co_apps = Column(String(1000), default='')
    applicant_id = Column(BigInteger, default='')
    transfer_name = Column(String(100), default='')
    acceptor_name = Column(String(100), default='')
    is_paid = Column(String(100), default=False)
    is_confirm_able = Column(SmallInteger, default=3)
    is_confirmed = Column(Boolean, default=False)
    is_reviewed = Column(Boolean, default=False)
    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Column(Boolean, default=False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Column(Boolean, default=False)


@model(MarkTransferOrder)
class MarkTransferOrderDao(DatabaseTemplate):

    def get_by_user_order(self, user, order):
        return self.session.query(self.model_cls).\
            filter(MarkTransferOrder.user_id == user, MarkTransferOrder.order_id == order).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.get_by_user_order(user_id, order_id)

    def get_by_id_user(self, id, user):
        return self.session.query(self.model_cls).\
            filter(MarkTransferOrder.user_id == user, MarkTransferOrder.id == id).first()

    def get_by_order(self, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).first()