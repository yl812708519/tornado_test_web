#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from app.commons import dateutil
from configs.order_status_map import BizStatusMap, BaseOrderStatus, OrderStatusMap
from app.services.base_service import BaseService, ServiceException
from configs.database_builder import DatabaseBuilder
from app.commons.biz_model import BizModel, Attribute
from app.services.sms_code_service import SmsCodeService
from app.services.user_service import UserProfileDao
from app.daos.order_status_dao import OrderStatus, OrderStatusDao
from app.daos.order_dao import OrderDao


class OrderStatusBO(BizModel):
    status = Attribute('')
    name = Attribute('')
    created_at = Attribute('')
    # next_status = Attribute('')


class OrderStatusService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def get_by_order_type(order_type, is_only_biz=False, is_paid_included=False):
        if is_only_biz:
            # 只取出业务信息
            return BizStatusMap.get_biz_status(order_type, is_paid_included)
        status_map = getattr(BizStatusMap(), order_type, tuple())
        return status_map

    @staticmethod
    def get_biz_status_by_type(order_type, is_paid_include):
        return BizStatusMap.get_biz_status(order_type, is_paid_include)

    @staticmethod
    def get_dict_by_types(types):
        status_dict = dict()
        for t in types:
            status_dict[t] = getattr(BizStatusMap, t, dict())
        return status_dict

    @staticmethod
    def get_order_status():
        # status_dict = dict()
        # for order_type in order_types:
        #     status_dict[order_type] = getattr(BizStatusMap, 'mark_reg')
        # status_dict['order_status'] =
        return BaseOrderStatus()

    def thrift_update_order_status(self, order_id, status, stuff_id=0):
        """
        更新订单状态 并发送短信通知， 已支付，等待审核状态更新时员工id为空
        :param order_id:
        :type order_id:
        :param status:
        :type status:
        :param stuff_id:
        :type stuff_id:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            order = OrderDao(session).get(order_id)
            self.update_order_status(order, status, stuff_id, session)
            order_dao.update(order)

    def update_order_status(self, order, status, stuff_id, session):
        """
        更新订单状态 并发送短信通知， 已支付，等待审核状态更新时员工id为空

        :param status: 更改为的status
        :type status:
        :param stuff_id:
        :type stuff_id:
        :return:
        :rtype:
        """
        order.status = status
        self.recode_order_status(order, status, session, stuff_id)

    @staticmethod
    def recode_order_status(order, status, session, stuff_id=0):
        """
        更新订单状态 并发送短信通知， 已支付，等待审核状态更新时员工id为空

        :param status:
        :type status:
        :param stuff_id:
        :type stuff_id:
        :return:
        :rtype:
        """
        order_status = OrderStatus()
        order_status.order_id = order.id
        order_status.status = status
        order_status.stuff_id = stuff_id
        OrderStatusDao(session).add_history(order_status)
        if status not in (OrderStatusMap.WAIT_DELEGATE, OrderStatusMap.WAIT_REVIEW):
            OrderStatusService.send_status_changed_msg(order, session)

    @staticmethod
    def send_status_changed_msg( order, session):
        """
        :return:
        """
        user_profile = UserProfileDao(session).get_by_user(order.user_id)
        stauts = OrderStatusService.get_by_order_type(order.order_type)
        status_name = stauts.get(order.status)
        SmsCodeService().send_notify_msg(user_profile.mobile,
                                         "order_status_changed",
                                         [order.name,
                                          status_name,
                                          order.id,
                                          dateutil.timestamp_to_string(order.updated_at)])

    def get_statuses_by_order(self, order_id, order_type):
        """
        获取 该订单的 状态变化列表
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            statuses = OrderStatusDao(session).gets_by_order(order_id)
            # all_statuses = self.get_by_order_type(order_type)
            s_list = []
            for status in statuses:
                status_bo = OrderStatusBO(status.fileds)
                s_list.append(status_bo)
            return s_list

