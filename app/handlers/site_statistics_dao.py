#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger, desc, func
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin

__author__ = 'zhaowenlei'

class SiteStatistic(IdMixin, BaseModel):

    signup_num = Column(BigInteger)
    transaction_num = Column(BigInteger)
    untreated_order_num = Column(BigInteger)
    confirm_order_num = Column(BigInteger)
    collected_at = Column(BigInteger)


@model(SiteStatistic)
class SiteStatisticDao(DatabaseTemplate):

    def count_by_user_id(self, offset=0, page_size=10):

        site_statistics = self.session.query(self.model_cls).filter().\
            order_by(desc(self.model_cls.collected_at)).limit(page_size).offset(offset).all()

        total_count = self.session.query(func.count('*')).select_from(self.model_cls).\
            filter().scalar()

        return total_count, site_statistics