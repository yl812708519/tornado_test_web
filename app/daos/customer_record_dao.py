#! /usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, BigInteger, Text, desc
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, CreatedAtMixin

__author__ = 'zhaowenlei'


class CustomerRecord(IdMixin, CreatedAtMixin, BaseModel):

    # 订单id
    order_id = Column(BigInteger)
    # 客服记录
    record = Column(Text)

@model(CustomerRecord)
class CustomerRecordDao(DatabaseTemplate):

    def gets_by_order_id(self, order_id):
        return self.session.query(self.model_cls).filter(self.model_cls.order_id == order_id).\
            order_by(desc(self.model_cls.created_at)).all()