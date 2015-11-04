#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import Column, BigInteger, String, Float, desc
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin


class OrderStatus(IdMixin, CreatedAtMixin, BaseModel):

    order_id = Column(BigInteger, default=None)
    stuff_id = Column(BigInteger, default=None)
    status = Column(String(40), default='')


@model(OrderStatus)
class OrderStatusDao(DatabaseTemplate):

    def add_history(self, instance):
        return self.add(instance)

    def gets_by_order(self, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).\
            order_by(desc(self.model_cls.created_at)).all()
