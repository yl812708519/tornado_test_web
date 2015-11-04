#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import Column, BigInteger, String, Float, Boolean
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin


class OrderPayment(IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin, BaseModel):

    order_id = Column(BigInteger, default=None)
    service_charge = Column(Float, default=None)
    official_charge = Column(Float, default=None)
    tax = Column(Float, default=0)
    order_tip = Column(Float, default=None)
    pay_mode = Column(String(45), default='')
    pay_fee = Column(Float, default=0)
    pay_config = Column(String(200), default='')
    buyer_account = Column(String(200), default='')
    out_trade_no = Column(String(200), default='')
    payment_time = Column(String(80), default=0)
    is_paid = Column(Boolean, default=False)
    is_refund = Column(Boolean, default=False)


@model(OrderPayment)
class OrderPaymentDao(DatabaseTemplate):
    """
    支付结果记录表
    """
    def get_by_order_id(self, order_id):
        """
        通过订单获取相关的 支付信息
        :param order_id:
        :return:
        """
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).\
            filter(self.model_cls.is_deleted == 0).first()