#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, BigInteger, desc, Text
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin


__author__ = 'liuli'


class Provide(IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin, BaseModel):
    # 点击图片跳转路径
    url = Column(String(200), default=None)
    # 文章标题
    title = Column(String(200), default=None)
    # 文章内容
    content = Column(String(200), default=None)
    # 是否显示
    is_hidden = Column(BigInteger, default=0)
    # 按编号排序
    order_num = Column(BigInteger, default=1)
    # 图片保存路径
    img_url = Column(String(200), default=None)

@model(Provide)
class ProvideDao(DatabaseTemplate):

    def gets_by_search_conditions(self, offset=0, count=10):
        conditions = list()
        # 查询未删除记录
        conditions.append(self.model_cls.is_deleted == 0)
        conditions.append(self.model_cls.is_hidden == 0)
        return self.session.query(self.model_cls).filter(*conditions). \
            order_by(desc(self.model_cls.order_num)). \
            limit(count).offset(offset).all()

