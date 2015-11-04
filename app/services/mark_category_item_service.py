#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from app.services.base_service import BaseService
from app.commons.biz_model import BizModel, Attribute
from configs.database_builder import DatabaseBuilder
from app.daos.mark_category_item_dao import MarkCategoryItemDao, MarkCategoryItem
from app.services.base_service import ServiceException


class MarkCategoryBO(BizModel):
    id = Attribute()
    # 分类编号
    code = Attribute(0)
    # 分类名
    name = Attribute(0)
    # 父级分类编号
    parent_code = Attribute('')


class MarkCategoryItemService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def gets_by_parent_code(self, parent_code):
        """
        获取子类别(三级类)
        :param parent_code:
        :return:
        """
        with self.create_session(self._default_db) as session:
            categories = MarkCategoryItemDao(session).gets_by_parent_code(parent_code)
            items = [MarkCategoryBO(**cate.fields) for cate in categories] \
                if categories is not None else []
            return items

    def handle_category(self, category, itemtrees, items):
        # 处理前台传入的分类信息
        # 确保所有item所属于一个category
        # 传入信息全都是id
        with self.create_session(self._default_db) as session:

            category_ids = items + itemtrees
            category_ids.append(category)
            c_dict = MarkCategoryItemDao(session).get_dict_by_ids(category_ids)
            item_bos = []
            itemtree_bos = []
            for cid in category_ids:
                c_obj = c_dict[long(cid)]
                if not isinstance(c_obj, MarkCategoryItem):
                    continue
                if cid in items:
                    item_bos.append(MarkCategoryBO(**c_obj.fields))
                elif cid in itemtrees:
                    itemtree_bos.append(MarkCategoryBO(**c_obj.fields))
                elif cid == category:
                    category_bo = MarkCategoryBO(**c_obj.fields)
            for item_bo in item_bos:
                if not (item_bo.code.startswith(category_bo.code) or item_bo.code.startswith('C'+category_bo.code)):
                    raise ServiceException(20054, 'items error')
