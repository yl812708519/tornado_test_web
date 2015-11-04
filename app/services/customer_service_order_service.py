#! /usr/bin/env python
# coding:utf-8
import random

from app.commons.biz_model import BizModel, Attribute
from app.commons.dateutil import timestamp_to_string
from app.services.order_status_service import OrderStatusService, OrderStatusMap
from app.daos.customer_service_order_dao import CustomerServiceBizDao, \
    CustomerServiceOrderDao, CustomerServiceOrder
from app.daos.customer_service_user_dao import CustomerServicestatsDao, CustomerServiceUserDao
from app.daos.order_dao import OrderDao
from app.services.base_service import BaseService, ServiceError
from configs.database_builder import DatabaseBuilder


__author__ = 'zhaowenlei'


class CustomerServiceOrderBO(BizModel):

    # 客服id
    csu_id = Attribute(None)
    # 订单
    order_id = Attribute(None)
    # 处理类型(待填订单，确认订单)
    treat_type = Attribute('')
    # 完成状态(未处理、已确认)
    is_finished = Attribute(0)
    created_at = Attribute(None)


class CSOrderBO(CustomerServiceOrderBO):
    name = Attribute(None)
    user_id = Attribute(None)
    price = Attribute(None)
    created_at = Attribute(None)


class CustomerServiceOrderService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def gets_by_type(session, order_type):
        customer_service_biz_dao = CustomerServiceBizDao(session)
        return customer_service_biz_dao.gets_by_type(order_type)

    @staticmethod
    def get_by_order(session, order_id):
        cs_order_dao = CustomerServiceOrderDao(session)
        cs_order = cs_order_dao.get_by_order(order_id)
        return CustomerServiceOrderBO() if cs_order is None else CustomerServiceOrderBO(cs_order.fields)

    @staticmethod
    def get_biz_csu_id(session, order_type, user_id):
        user_order = OrderDao(session).get_first_by_type_uid(order_type, user_id)
        if user_order:
            cs_biz = CustomerServiceBizDao(session).get_by_csu_id(user_order.csu_id)
            # 按 用户与当前业务 读取之前的客服id
            if cs_biz is not None and order_type in [cs_biz.biz_name for cs_biz in cs_biz]:
                return user_order.csu_id
        # 没有之前信息， 随机产生对应业务的客服id
        customer_service_bizs = CustomerServiceBizDao(session).gets_by_type(order_type)
        length = len(customer_service_bizs)
        if length == 0:
            raise ServiceError(10005, 'customer service is not ready')
        rand_num = random.randrange(0, length)
        return getattr(customer_service_bizs[rand_num], 'csu_id')

    @staticmethod
    def add_cs_order(order, treat_type, csu_id, session):
        cs_dao = CustomerServiceOrderDao(session)
        cs_order = cs_dao.get_by_order_treat_type(order.id, treat_type)
        if not cs_order:
            customer_service_order = CustomerServiceOrder()
            customer_service_order.order_id = order.id
            customer_service_order.treat_type = treat_type
            customer_service_order.csu_id = csu_id
            cs = CustomerServiceOrderDao(session).add(customer_service_order)
        else:
            # 确保重置订单确认状态后订单流程不会出错
            cs_order.treat_type = treat_type
            cs_order.csu_id = csu_id
            cs_order.is_finished = False
            cs = CustomerServiceOrderDao(session).update(cs_order)
        CustomerServiceOrderService().update_untreated_order_num(session, csu_id)
        return CustomerServiceOrderBO(**cs.fields)

    @staticmethod
    def update_untreated_order_num(session, csu_id):
        cs_service_dao = CustomerServicestatsDao(session)
        cs_service_stats = cs_service_dao.get_by_csu_id(csu_id)
        if cs_service_stats:
            cs_service_stats.untreated_order_num += 1
            cs_service_dao.update(cs_service_stats)

    @staticmethod
    def condition_for_workbench(csu_id, order_id=None, treat_type=None):
        conditions = [CustomerServiceOrder.csu_id == csu_id,
                      CustomerServiceOrder.is_finished == 0]
        if treat_type:
            conditions.append(CustomerServiceOrder.treat_type == treat_type)
        if order_id:
            conditions.append(CustomerServiceOrder.order_id.like('%'+str(order_id)+'%'))
        return conditions

    def gets_for_workbench(self, csu_id, order_id=None, treat_type=None, offset=0, count=15):
        with self._default_db.create_session() as session:
            customer_service_order_dao = CustomerServiceOrderDao(session)
            conditions = self.condition_for_workbench(csu_id, order_id, treat_type)

            customer_service_orders = customer_service_order_dao.gets_for_workbench(offset, count, *conditions)
            if customer_service_orders:
                CSOrder_bos = []
                CSOrder_ids = []
                for customer_service_order in customer_service_orders:
                    CSOrder_bos.append(CSOrderBO(**customer_service_order.fields))
                    CSOrder_ids.append(customer_service_order.order_id)

                order_dict = OrderDao(session).get_dict_by_ids(CSOrder_ids)
                if order_dict:
                    for csorder_bo in CSOrder_bos:
                        # 查询具体的订单信息
                        order_id = csorder_bo.order_id
                        order = order_dict.get(order_id, None)
                        if order:
                            csorder_bo.name = order.name
                            csorder_bo.user_id = order.user_id
                            csorder_bo.price = float(order.price)
                            csorder_bo.created_at = timestamp_to_string(csorder_bo.created_at, '%Y-%m-%d %H:%M:%S')
                    return CSOrder_bos

    def count_for_workbench(self, csu_id, order_id=None, treat_type=None):
        with self._default_db.create_session() as session:
            customer_service_order_dao = CustomerServiceOrderDao(session)
            conditions = self.condition_for_workbench(csu_id, order_id, treat_type)
            count = customer_service_order_dao.count(*conditions)
            return count

    def is_csuser_allowed(self, csu_id, order_id, treat_type):
        """
        由于 确认订单和代填订单的权限一样
        :param csu_id:
        :type csu_id:
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """
        with self._default_db.create_session() as session:
            csorder = CustomerServiceOrderDao(session).get_by_csu_order_treat_type(csu_id, order_id, treat_type)
            return True if csorder else False

    @staticmethod
    def update_csorder(order, session, treat_type):
        cs_order_dao = CustomerServiceOrderDao(session)
        csorder = cs_order_dao.get_by_order_treat_type(order.id, treat_type)
        if csorder:
            if not csorder.is_finished:
                csorder.is_finished = 1
                csu_id = csorder.csu_id
                cs_stats_dao = CustomerServicestatsDao(session)
                cs_stats = cs_stats_dao.get_by_csu_id(csu_id)
                if cs_stats.untreated_order_num > 0:
                    cs_stats.untreated_order_num -= 1
                    cs_stats.confirm_order_num += 1
                cs_stats_dao.update(cs_stats)
            return True
        else:
            return False

if __name__ == '__main__':
    a = CustomerServiceOrderService().gets_for_workbench(1, '', '')
    print a