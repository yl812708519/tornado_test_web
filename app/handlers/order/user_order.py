#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tornado.web import authenticated
from app.handlers.application import BaseHandler
from app.commons.view_model import ViewModel
from app.services.order_service import OrderBO, OrderService


class UserOrdersHandler(BaseHandler):
    """
        用户订单列表 及 相关操作
    """
    @authenticated
    def get(self, *args, **kwargs):
        """
        列表
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        order_service = OrderService()

        current_page = self.get_argument('currentPage', 1)
        page_size = self.get_argument('page_size', 12)
        offset = (int(current_page) - 1) * page_size

        order_dict = order_service.count_gets_by_user_id(user.user_id, offset, page_size)
        result = dict(orders=ViewModel.to_views(order_dict['order_bos']),
                      current_page=current_page,
                      total_page=int(order_dict['total_count'] + page_size - 1)/page_size,)
        self.render('ban_views/order/user_order.html', **result)