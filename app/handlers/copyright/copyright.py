#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlencode

from app.commons.view_model import ViewModel
from app.handlers.application import BaseHandler
from app.handlers.order.order import OrderDetailHandler
from app.services.business_service import BusinessService

__author__ = 'zhaowenlei'


class CopyrightBizHandler(BaseHandler):

    def get(self, biz_type):
        mark_biz_type = 'copyright_' + biz_type
        bizs = BusinessService().get_by_type(mark_biz_type)
        result = dict(bizs=ViewModel.to_views(bizs),
                      default=bizs[0],
                      biz_type=biz_type,
                      active_id=mark_biz_type)

        self.render('ban_views/copyright_businesses.html', **result)

    def post(self, *args, **kwargs):
        """
        添加商标业务的订单和相应业务数据
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        biz_type = self.get_argument('biz_type', '')
        next_url = self.request.headers.get('Referer')
        if not user:
            # post请求的用户登录判断
            # authenticated post请求会报403
            url = self.get_login_url()
            url += "?" + urlencode(dict(next=next_url))
            self.redirect(url)
            return
        detail_service = OrderDetailHandler.detail_service(biz_type)
        #  basebanservice.add
        detail_order_id = detail_service.add(user.user_id, biz_type)
        self.redirect('/order/'+str(detail_order_id))
