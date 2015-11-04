#! /usr/bin/env python
# -*- coding:utf-8 -*-
from app.thrift.gen_py.csorder.ttypes import Extest

__author__ = 'yanglu'

import functools
from app.services.customer_service_order_service import CustomerServiceOrderService
from app.services.order_status_service import OrderStatusService, OrderStatusMap
from app.services.order_tip_service import OrderTipService
from app.services.order_service import OrderService, ServiceException
from app.services.order_payment_service import OrderPaymentService, OrderPaymentDao
from app.services.business_service import BusinessService
from app.services.sms_code_service import SmsCodeService, SmsTemplateBuilder
import json


def get_raise(method):
    @functools.wraps(method)
    def _wapper(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except ServiceException, e:
            raise Extest(e.code, e.msg)
        except Exception:
            raise Extest(1000, 'system error')
    return _wapper


class ThriftCSOrderHandler(object):

    @staticmethod
    def biz_bos_to_json(biz_bos):
        biz_list = list()
        if biz_bos:
            for biz_bo in biz_bos:
                biz_list.append(biz_bo.attributes)
            return json.dumps(biz_list)
        else:
            return ''

    @staticmethod
    @get_raise
    def get_for_workbench(csu_id, order_id, treat_type, offset, count):
        csorder_bos = CustomerServiceOrderService().gets_for_workbench(csu_id, order_id, treat_type, offset, count)
        csorders = ThriftCSOrderHandler().biz_bos_to_json(csorder_bos)
        return csorders

    @staticmethod
    @get_raise
    def count_for_workbench(csu_id, order_id, treat_type):
        count = CustomerServiceOrderService().count_for_workbench(csu_id, order_id, treat_type)
        return count

    @staticmethod
    @get_raise
    def is_csuser_allowed(csu_id, order_id, treat_type):
        return CustomerServiceOrderService().is_csuser_allowed(csu_id, order_id, treat_type)

    @staticmethod
    @get_raise
    def handle_csorder(order_id, treat_type, stuff_id, next_status):
        """
        更新客服处理的订单状态
        并更新计数表
        :param order_id:
        :type order_id:
        :param treat_type: delegate/review
        :type treat_type: string
        :return:
        :rtype:
        """

        result = OrderService().handle_csorder(order_id, treat_type, stuff_id, next_status)
        return result

    @get_raise
    def offline_payment(self, order_id, order_type, is_invoice, payment_json):
        """
        获得业务信息, 后台修改订单付款状态
        :param order_type:
        :type order_type:
        :return:
        :rtype:
        """
        business = BusinessService().get_by_name(order_type)
        payment = json.loads(payment_json)
        message = OrderPaymentService().parse_offline_payment(order_id, business, is_invoice, payment)
        return str(message)

    # def get_raise(self):
    #     raise Extest(1000, 'Exceptions')


class ThriftOrderStatusHandler(object):

    @staticmethod
    def gets_by_order_type(order_type):
        statuses = OrderStatusService().get_by_order_type(order_type)
        return json.dumps(statuses)

    @staticmethod
    def get_biz_status_by_type(order_type, is_paid_included):
        """
        获取业务状态
        :param order_type:
        :type order_type:
        :param is_paid_included: 业务状态中否包含已付款（判断条件,inc中的用户权限）
        :type is_paid_included:  bool
        :return:
        :rtype:
        """
        statuses = OrderStatusService().get_biz_status_by_type(order_type, is_paid_included)
        return json.dumps(statuses)

    @staticmethod
    def update_order_status(order_id, status, stuff_id):
        OrderStatusService().thrift_update_order_status(order_id, status, stuff_id)
        return True

    @staticmethod
    def get_order_status():
        status_dict = OrderStatusService().get_order_status()
        return json.dumps(status_dict)

    @staticmethod
    def get_dict_by_order_types(order_types):
        status_dict = OrderStatusService().get_dict_by_types(order_types)
        return json.dumps(status_dict)

    def reset_confirm(self, stuff_id, order_id, order_type):
        OrderService().reset_confirm(stuff_id, order_id)


class ThriftOrderTipHandler(object):

    @staticmethod
    def count_get_tips(offset, count):
        count, tip_bos = OrderTipService().count_get_tips(offset, count)
        return dict(total_count=str(count),
                    tips=ThriftCSOrderHandler().biz_bos_to_json(tip_bos))


class ThriftSmsNotifyHandler(object):

    @staticmethod
    def send_sms_notify(mobile, temp_name, args_json):
        format_args = json.loads(args_json)
        SmsCodeService().send_notify_msg(mobile, temp_name, format_args)
        return 'success'
