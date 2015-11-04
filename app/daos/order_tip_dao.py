#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, BigInteger, Integer, Boolean, desc
from app.commons.database import DatabaseTemplate, model, BaseModel
from app.commons.database_mixin import IdMixin, CreatedAtMixin

__author__ = 'yanglu'


class OrderTip(IdMixin, CreatedAtMixin, BaseModel):
    csu_id = Column(BigInteger)
    user_id = Column(String(40), default='')
    stuff_name = Column(String(40))
    order_id = Column(BigInteger)
    order_name = Column(String(40))
    is_paid = Column(Boolean, default=False)
    tip_price = Column(Integer)
    paid_at = Column(BigInteger, default=0)


@model(OrderTip)
class OrderTipDao(DatabaseTemplate):

    def gets_by_stuff_id(self, stuff_id):
        # 通过员工id查询打赏的列表
        return self.session.query(self.model_cls).\
            filter(self.model_cls.stuff_id == stuff_id).all()

    def get_by_order(self, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).\
            filter(self.model_cls.is_paid == 1).first()

    def get_by_order_user_price(self, order, user, price):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order).\
            filter(self.model_cls.tip_price == price).\
            filter(self.model_cls.user_id == user).first()

    def gets(self, offset, count):
        return self.session.query(self.model_cls).\
            order_by(desc(self.model_cls.paid_at)).offset(offset).limit(count).all()