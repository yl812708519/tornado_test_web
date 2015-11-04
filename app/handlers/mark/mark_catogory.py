#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.handlers.application import RestfulAPIHandler
from app.commons.view_model import ViewModel
from app.services.mark_category_item_service import MarkCategoryItemService
from app.services.base_service import ServiceException
from tornado.web import HTTPError



class MarkCategoryJsonHandler(RestfulAPIHandler):
    """
        ajax返回第三季分类的数据
    """

    def post(self):
        """

        :return:
        """
        parent_code = self.get_argument('parent_code', None)
        items = MarkCategoryItemService().gets_by_parent_code(parent_code) if parent_code else []
        result = dict(list=ViewModel.to_views(items))
        self.write(result)

