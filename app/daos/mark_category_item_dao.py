#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import String, or_
from sqlalchemy import Column
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, UpdatedAtMixin
from app.commons.database_mixin import CreatedAtMixin

__author__ = 'freeway'


class MarkCategoryItem(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    code = Column(String(40), default=None)  # 商标编码
    name = Column(String(500), default=None)  # 编码名称
    parent_code = Column(String(40), default=None)  # 商标父编码 ""表示顶级


@model(MarkCategoryItem)
class MarkCategoryItemDao(DatabaseTemplate):
    """ 商标分类及小项

    """

    def get_by_code(self, code):
        return self.get_first_by_criterion(MarkCategoryItem.code == code)

    def gets_by_parent_code(self, parent_code):
        query = self.session.query(MarkCategoryItem)\
            .filter(MarkCategoryItem.parent_code == parent_code)\
            .order_by(MarkCategoryItem.code)
        return query.all()

    def gets_by_codes_category(self, codes, category):
        """
        商标分类中 code不唯一， 为防止跨类重复，增加category筛选
        :param codes:
        :type codes:
        :param category:
        :type category:
        :return:
        :rtype:
        """
        no_order_instances = self.session.query(self.model_cls)\
            .filter(self.model_cls.code.in_(codes))\
            .filter(or_(self.model_cls.parent_code.like(category+'%'), self.model_cls.parent_code == 0)).all()
        inst_dict = dict()
        for instance in no_order_instances:
            inst_dict[instance.code] = instance
        instances = list()
        for identity in codes:
            instance = inst_dict.get(identity, None)
            if instance is not None:
                instances.append(instance)
        return instances

    def get_dict_by_codes_category(self, codes, category):
        """
        商标分类中 code不唯一， 为防止跨类重复，增加category筛选
        :param codes:
        :type codes:
        :param category:
        :type category:
        :return:
        :rtype:
        """
        no_order_instances = self.session.query(self.model_cls)\
            .filter(self.model_cls.code.in_(codes))\
            .filter(or_(self.model_cls.parent_code.like(category+'%'), self.model_cls.parent_code == 0)).all()
        inst_dict = dict()
        for instance in no_order_instances:
            inst_dict[instance.code] = instance
        return inst_dict

    def get_thrid(self):
        no_order_instances = self.session.query(self.model_cls).filter(self.model_cls.parent_code > 45).all()

        return no_order_instances