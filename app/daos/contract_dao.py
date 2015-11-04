#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from sqlalchemy import Column, String, BigInteger, desc, or_, Boolean

from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin


class BizContract(IdMixin, CreatedAtMixin, BaseModel):
    biz_name = Column(String(40))
    contract = Column(String(40))
    contract_name = Column(String(30))
    seal_demand = Column(String(40), default='')
    part_num = Column(String(30), default='')
    remark = Column(String(100), default='')
    sort = Column(BigInteger, default=0)
    is_download_able = Column(Boolean, default=False)
    is_show = Column(Boolean, default=True)


@model(BizContract)
class ContractDao(DatabaseTemplate):

    def gets_by_biz_name(self, biz_name, biz_group_name, base_type):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.biz_name.in_([biz_name, biz_group_name, base_type]))\
            .order_by(desc(self.model_cls.sort)).all()


