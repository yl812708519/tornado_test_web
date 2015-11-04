#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 当前未使用， 合同页面整合至 订单页面 2015.08.23
from tornado.web import HTTPError
from tornado.web import authenticated
from app.handlers.application import BaseHandler
from app.commons.view_model import ViewModel
from app.services.order_service import OrderBO, OrderService
from app.services.contract_service import ContractService


class OrderContractsHandler(BaseHandler):
    """
        订单 合同/材料 页面
    """

    @authenticated
    def get(self, order_id):
        """
        列表
        :param args: order_id
        :return:
        """
        user = self.current_user
        order = OrderService().get(order_id, user.user_id)
        if order is None:
            raise HTTPError(404)
        contracts = ContractService().gets_by_biz_name(order.order_type)
        result = dict(contracts=ViewModel.to_views(contracts),
                      order=ViewModel.to_view(order),
                      order_id=order_id)
        self.render('ban_views/order/order_contract.html', **result)