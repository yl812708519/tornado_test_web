#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.copyright_opus_service import CopyrightOpusOrderService
from app.services.copyright_soft_service import CopyrightSoftOrderService
from app.services.customer_service_order_service import CustomerServiceOrderService

__author__ = 'yanglu'

import functools
from tornado.web import HTTPError
from app.commons import dateutil
from app.services.base_service import BaseService, ServiceException
from app.services.ban_bos.order_bo import OrderBO
from configs.database_builder import DatabaseBuilder
from configs.order_status_map import OrderStatusMap, BaseOrderStatus
from app.daos.order_dao import OrderDao
from app.services.mark_change_service import MarkChangeOrderService
from app.services.mark_reg_service import MarkRegService
from app.services.mark_reg_apply_service import MarkRegApplyService
from app.services.mark_transfer_service import MarkTransferService
from app.services.order_status_service import OrderStatusService, OrderStatusDao
from app.services.applicant_service import ApplicantService
from app.services.order_tip_service import OrderTipService


def order_decorater(method):
    """
     获取订单信息的装饰器
     得到订单、业务详情、session
    :param method:
    :type method:
    :return:
    :rtype:
    """
    @functools.wraps(method)
    def _wapper(order_service, order_id, user_id):
        if not isinstance(order_service, OrderService):
            return method(order_service, user_id, order_id)
        with order_service.create_session(order_service._default_db) as session:
            order_dao = OrderDao(session)
            order = order_dao.get_by_uid_order_id(user_id, order_id)
            if order is None:
                raise HTTPError(404)
            biz_service = order_service.get_detail_service(order.order_type)
            biz_dao = biz_service.get_biz_dao(session)
            biz_obj = biz_dao.get_by_user_id_order_id(user_id, order_id)
            order.biz_detail = biz_obj
            order_service.session = session
            order_service.order = order
            order_service.operator = biz_service.operator.initialize(order, session)
            order_service.biz_service = biz_service
            result = method(order_service, user_id, order_id)
            if order_service.operator.is_modified:
                order_dao.update(order_service.order)
                biz_dao.update(order_service.order.biz_detail)
            return result
    return _wapper


class OrderService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.order = None
        self.session = None
        self.operator = None
        self.biz_service = None

    @staticmethod
    def get_detail_service(order_type):
        if order_type in ['mark_reg', 'collective_mark_reg', 'prove_mark_reg']:
            return MarkRegService()
        elif order_type in ['reissue_reg_credential', 'provide_mark_reg_proof', 'correct_mark_reg_items']:
            return MarkRegApplyService()
        elif order_type in ['reg_col_pro_applicant', 'age_rec_applicant', 'sub_service_applicant']:
            return MarkChangeOrderService()
        elif order_type in ['mark_transfer_apply', 'reissue_mark_transfer']:
            return MarkTransferService()
        elif order_type in ['word_copyright', 'art_copyright', 'other_copyright']:
            return CopyrightOpusOrderService()
        elif order_type in ['software_copyright']:
            return CopyrightSoftOrderService()
        else:
            raise ServiceException(20052, 'biz is not found')

    # @order_decorater
    # def test(self, user_id, order_id):
    #     # operate = OrderOperateService(self.order, self.session)
    #     self.operator.confirm_order()

    def get(self, order_id, user_id):
        """
        获取 orderBO
        """
        with self.create_session(self._default_db) as session:
            order = OrderDao(session).get_by_uid_order_id(user_id, order_id)
            if order is None:
                return None
            order_bo = self.deal_order(order)
            return order_bo

    @order_decorater
    def get_detail_by_id_user(self, order_id, user_id):
        order_bo = OrderBO(**self.order.fields)
        order_bo.tip_index = self.operator.get_tip_index()
        detail_bo = self.biz_service.deal_biz(self.order.biz_detail, self.session)
        return order_bo, detail_bo

    def count_gets_by_user_id(self, user_id, offset, count):
        """
        订单列表
        :param user_id:
        :return:
        """
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            orders = order_dao.gets_by_uid(user_id, offset, count)
            order_bos = []
            order_statuses = OrderStatusService.get_order_status()
            for order in orders:
                order_bo = self.deal_order(order)
                order_bo.status_name = order_statuses.get(order_bo.status, False)
                if not order_bo.status_name:
                    # 业务状态有些名字太长不适宜显示,统一使用办理中
                    order_bo.status_name = '办理中'
                    order_bo.status = OrderStatusMap.COMPLETED
                order_bos.append(order_bo)
            total_count = order_dao.count_by_uid(user_id)
            return dict(total_count=total_count,
                        order_bos=order_bos)

    @staticmethod
    def deal_order(order):
        order_bo = OrderBO(**order.fields)
        order_bo.created_date = dateutil.timestamp_to_string(order_bo.created_at)
        order_statuses = OrderStatusService.get_order_status()
        order_bo.status_name = order_statuses.get(order_bo.status, False)
        # order_bo.price = float(order_bo.price, 2)
        return order_bo

    @staticmethod
    def is_confirm_able(order):
        if order.is_confirm_able != 1:
            raise ServiceException(20055, 'this order can`t confirm')

    @order_decorater
    def confirm_order(self, order_id, user_id):
        self.operator.confirm_order()

    def add_order_apps(self, app_id_touples, order_id, order_type):
        with self.create_session(self._default_db) as session:
            return ApplicantService._add_order_apps(app_id_touples, order_id, order_type, session)

    def gets_by_ids_user(self, order_ids, user_id):
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            orders = order_dao.gets_by_ids_user(order_ids, user_id)
            return [OrderBO(**order.fields) for order in orders] if len(orders) > 0 else None

    def update_invoiced_by_ids(self, order_ids):
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            orders = order_dao.gets_by_ids(order_ids)
            for order in orders:
                order.is_invoiced = True
                order.is_invoice_able = False
            order_dao.update_all(orders)

    def move_to_trash(self, order_id, user_id):
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            order = order_dao.get_by_uid_order_id(user_id, order_id)
            order.is_in_trash = True
            order_dao.update(order)

    @order_decorater
    def apply_delegated(self, order_id, user_id):
        """
        代填 申请
        :param order_id:
        :return:
        """
        return self.operator.apply_delegate()

    def handle_csorder(self, order_id, treate_type, stuff_id, next_status):
        """
        客服处理订单， delegate/review/upload 的相关订单数据处理
        :param order_id:
        :type order_id:
        :param treate_type:delegate/review
        :type treate_type:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            self.initialize_operator_by_id(order_id, session)
            self.operator = self.biz_service.operator.initialize(self.order, session)
            self.operator.handle_csorder(treate_type, stuff_id, next_status)
            return True

    def pay_deal(self, order_id, payment, session):
        """
        处理 支付后的状态修改等操作
        :param order_id:
        :type order_id:
        :param session:  由payment_service 传入
        :type session:
        :return:
        :rtype:
        """
        self.initialize_operator_by_id(order_id, session)
        self.operator.pay_deal(payment)
        # 如果有打赏金额。更新打赏信息
        if payment.order_tip:
            OrderTipService.pay_tip(order_id, self.order.user_id, payment.order_tip, session)

    def get_status_by_order_user(self, order_id, user_id):
        with self.create_session(self._default_db) as session:
            order_dao = OrderDao(session)
            order = order_dao.get_by_uid_order_id(user_id, order_id)
            if order:
                statuses = []
                all_order_status = OrderStatusService.get_by_order_type(order.order_type)
                order_status = OrderStatusDao(session).gets_by_order(order_id)
                for status in order_status:
                    status_dict = status.fields
                    status_dict['remark'] = '状态变更为：' + all_order_status.get(status.status, '')
                    status_dict['created_at'] = dateutil.timestamp_to_string(status.created_at)
                    statuses.append(status_dict)
                statuses.append(dict(status='create',
                                     name='订单创建',
                                     remark='订单'+str(order.id)+'创建',
                                     created_at=dateutil.timestamp_to_string(order.created_at)))
                return statuses

    def reset_confirm(self, stuff_id, order_id):
        with self.create_session(self._default_db) as session:
            self.initialize_operator_by_id(order_id, session)
            self.operator.reset_status(stuff_id)
            ApplicantService.delete_order_applicants(order_id, session)

    def initialize_operator_by_id(self, order_id, session):
        """
        通过 order_id 查询order 、 biz_detail 、 初始化operator
        :param order_id:
        :type order_id:
        :param session:
        :type session:
        :return:
        :rtype:
        """
        order_dao = OrderDao(session)
        order = order_dao.get(order_id)
        if order is None:
            raise HTTPError(404)
        biz_service = self.get_detail_service(order.order_type)
        biz_dao = biz_service.get_biz_dao(session)
        biz_obj = biz_dao.get_by_order(order_id)
        order.biz_detail = biz_obj
        self.session = session
        self.order = order
        self.biz_service = biz_service
        self.operator = biz_service.operator.initialize(order, session)


# if __name__ == '__main__':
#     sevice = OrderService()
#     sevice.test('z_FZ', 14443)
