#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import HTTPError
from tornado.web import authenticated
from configs.order_status_map import OrderStatusMap
from configs.database_builder import DatabaseBuilder
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.commons.view_model import ViewModel
from app.services.applicant_service import ApplicantService
from app.services.business_service import BusinessService
from app.services.customer_service_user_service import CustomerServiceUserService
from app.services.order_tip_service import OrderTipService, OrderTipBO
from app.services.contract_service import ContractService
from app.services.order_service import OrderService
from app.services.ban_bos.order_bo import OrderPaymentBO
from app.services.order_payment_service import OrderPaymentService
from app.commons.pay_factory import AlipayFactory


class OrderDetailHandler(BaseHandler):
    """
    订单
    """

    @authenticated
    def get(self, order_id):
        user = self.current_user
        order = OrderService().get(order_id, user.user_id)
        if order is None:
            raise HTTPError(404)
        result = dict(order=ViewModel.to_view(order),
                      is_order=True,
                      order_payment=OrderPaymentBO(),
                      order_tip=OrderTipBO())

        if order.status == OrderStatusMap.WRITE_INFO:
            app_dict = ApplicantService().count_gets_by_user_id(user.user_id)
            result['applicants'] = ViewModel.to_views(app_dict['applicant_bos'])
            result['app_total'] = app_dict['total']
        biz_bo = BusinessService().get_by_name(order.order_type)
        result['biz'] = ViewModel.to_view(biz_bo)

        order, detail = OrderService().get_detail_by_id_user(order_id, user.user_id)
        result['tips_index'] = order.tip_index
        result['detail'] = ViewModel.to_view(detail)
        result['order'] = ViewModel.to_view(order)
        if order.is_paid:
            result['order_payment'] = OrderPaymentService().get_by_order(order_id)
            contracts = ContractService().gets_by_biz_name(order.order_type, biz_bo.type, result['detail'].base_type)
            result['contracts'] = ViewModel.to_views(contracts)
            order_tip = OrderTipService().get_by_order(order_id)
            result['order_tip'] = order_tip

        # 订单模板 默认为 业务的名字.html, 在bo中以默认值给出
        order_tpl = result['detail'].order_tpl

        result['referer'] = self.request.headers.get('referer', '/')
        result['cs_user'] = CustomerServiceUserService().get_by_csu_id(order.csu_id)

        result['order_id'] = order.id
        self.render('ban_views/order/'+order_tpl+'.html', **result)

    @staticmethod
    def detail_service(order_type):
        return OrderService().get_detail_service(order_type)


class OrderStatusHandler(RestfulAPIHandler):

    @authenticated
    def get(self, order_id, *args, **kwargs):
        """
        获取订单的状态列表
        :param order_id:
        :type order_id:
        :param args:
        :type args:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        user = self.current_user
        statuses = OrderService().get_status_by_order_user(order_id, user.user_id)
        if statuses:
            return self.write(statuses)
        else:
            self.write_error(404)


class OrderTrashHandler(RestfulAPIHandler):

    def put(self, *args, **kwargs):
        """
        移入垃圾箱
        :param args:
        :param kwargs:
        :return:
        """
        order_id = self.get_argument('order_id', '')
        if order_id:
            user = self.current_user
            order_service = OrderService()
            order_service.move_to_trash(order_id, user.user_id)
            self.write_success()


class OrderDelegateHandler(RestfulAPIHandler):
    @authenticated
    def put(self):
        """
            代填的处理部分
        """
        order_id = self.get_argument('order_id', '')
        order_name = self.get_argument('order_name', '')
        user = self.current_user
        order_service = OrderService()
        res = order_service.apply_delegated(order_id, user.user_id)
        if res:
            cs_user_service = CustomerServiceUserService()
            cus_ser_user_bo = cs_user_service.get_by_csu_id(res.csu_id)
            self.write(cus_ser_user_bo.qq)
            self.finish()
            cs_user_service.create_cs_notice_email('delegate', order_name, cus_ser_user_bo.email)
        else:
            self.write(0)


class OrderConfirmHandler(RestfulAPIHandler):

    def put(self, *args, **kwargs):
        """
        处理 确认订单
        """
        order_id = self.get_argument('order_id')
        order_name = self.get_argument('order_name', '')
        OrderService().confirm_order(order_id, self.current_user.user_id)
        self.write_success()
        self.finish()
        cs_user_service = CustomerServiceUserService()
        cus_ser_user_bo = cs_user_service.get_by_order_id(order_id)
        cs_user_service.create_cs_notice_email('confirm', order_name, cus_ser_user_bo.email)

