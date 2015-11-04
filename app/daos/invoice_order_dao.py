#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.database import DatabaseTemplate, model, BaseModel

__author__ = 'zhaowenlei'

from sqlalchemy import Column, BigInteger
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class InvoiceOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 发票id
    invoice_id = Column(BigInteger)
    # 订单id
    order_id = Column(BigInteger)


@model(InvoiceOrder)
class InvoiceOrderDao(DatabaseTemplate):

    def gets_by_invoice_id(self, invoice_id):
        return self.session.query(self.model_cls).filter(self.model_cls.invoice_id == invoice_id).all()