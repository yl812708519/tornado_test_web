#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'

from app.services.base_service import BaseService, ServiceException, ServiceError
from configs.order_status_map import OrderStatusMap
from app.services.order_status_service import OrderStatusService
from app.services.customer_service_order_service import CustomerServiceOrderService
from app.services.applicant_service import ApplicantService


class OrderOperateService(BaseService):

    def __init__(self):
        self.order = None
        self.is_initialize = False
        self.biz_detail = None
        self.db_session = None
        self.is_modified = 0

    def initialize(self, order, session=None):
        if not order:
            raise ServiceException(20051, 'not found this order')
        if session:
            self.db_session = session
        self.order = order
        self.biz_detail = order.biz_detail
        self.is_initialize = True
        return self

    def check_initialized(self):
        if self.is_initialize:
            raise ServiceError(10050, 'please initialize before use it')
        if self.order is None:
            self.is_initialize = True
            self.is_modified = 0

    def _recode_order_status_modify(self, stuff_id=0):
        OrderStatusService.recode_order_status(self.order,
                                               self.order.status,
                                               self.db_session,
                                               stuff_id)

    def apply_delegate(self):
        if self.biz_detail.is_confirm_able:
            self.biz_detail.is_delegated = 1
            self.biz_detail.is_confirm_able = 1
            self.order.status = OrderStatusMap.WAIT_DELEGATE
            self._recode_order_status_modify()
            self.is_modified = 1
            return CustomerServiceOrderService().\
                add_cs_order(self.order, 'delegate', self.order.csu_id, self.db_session)
        else:
            raise ServiceException(20056, 'has confirmed that can`t apply delegate')

    def move_to_trash(self):
        self.order.is_in_trash = True
        self.is_modified = 1

    def pay_deal(self, payment):
        self.order.status = OrderStatusMap.PAID
        self.order.is_paid = True
        if bool(payment.service_charge + payment.tax):
            self.order.is_invoice_able = True
        # 更新订单价格，确保再发票索取部分不会出现乌龙事件
        self.order.price = float(payment.pay_fee) - float(payment.order_tip)
        self.biz_detail.is_paid = True
        self._recode_order_status_modify()
        self.is_modified = 1

    def handle_csorder(self, treat_type, stuff_id, next_status):
        self.order.status = next_status
        self._recode_order_status_modify(stuff_id)
        CustomerServiceOrderService.update_csorder(self.order, self.db_session, treat_type)
        self.is_modified = 1

    def reset_status(self, stuff_id):
        self.order.status = OrderStatusMap.WRITE_INFO
        self.biz_detail.is_delegated = False
        self.biz_detail.is_delegate_confirmed = False
        self.biz_detail.is_reviewed = False
        self._recode_order_status_modify(stuff_id)
        # 清空 之前的order_app信息
        # 代填、确认订单（商标）、上传申请书（版权） 时添加order_app
        ApplicantService().delete_order_applicants(self.order.id, self.db_session)
        self.is_modified = 1

    def add_order_app(self):
        # 保存主体信息至order_applicant
        # 获取需要复制到order_applicants的 applicant_ids
        app_ids = self._get_order_apps()
        if not app_ids:
            raise ServiceException(20071, 'can`t find applicant_ids about this order')
        ApplicantService._add_order_apps(app_ids,
                                         self.order.id,
                                         self.order.order_type,
                                         self.db_session)

    def _get_order_apps(self):
        raise NotImplementedError


class MarkOperateService(OrderOperateService):
    """
    商标的业务订单操作类
    """
    def apply_delegate(self):
        self.biz_detail.is_confirmed = 1
        return super(MarkOperateService, self).apply_delegate()

    def confirm_order(self):
        """
        确认订单
        :return:
        :rtype:
        """
        if self.biz_detail.is_confirm_able:
            self.biz_detail.is_confirmed = True
            self.order.status = OrderStatusMap.WAIT_REVIEW
            self._recode_order_status_modify()
            CustomerServiceOrderService().\
                add_cs_order(self.order, 'review', self.order.csu_id, self.db_session)
            self.is_modified = 1
        else:
            raise ServiceException(20055, 'this order can`t confirm')

    def handle_csorder(self, treat_type, stuff_id, next_status):
        """
        后台 (代填/审核) 操作
        """
        if not self.biz_detail.is_confirmed:
            raise ServiceException(20070, 'this biz has not confirmed')
        if treat_type == 'delegate':
            self.biz_detail.is_delegate_confirmed = True
        self.biz_detail.is_reviewed = True
        super(MarkOperateService, self).handle_csorder(treat_type, stuff_id, next_status)
        self.add_order_app()

    def reset_status(self, stuff_id):
        self.biz_detail.is_confirmed = False
        super(MarkOperateService, self).reset_status(stuff_id)

    def get_tip_index(self):
        if self.biz_detail.is_paid:
            return 4
        if self.order.status == 'wait_payment':
            tip = 3
        elif self.order.status == 'wait_review':
            tip = 2
        elif self.order.status in ('wait_delegate', 'write_info'):
            tip = 1
        elif self.order.status == 'invalid':
            tip = 0
        return tip

    def _get_order_apps(self):
        """
        返回 需要记录的主体id和主体id的source_type后半截
        """
        if self.is_initialize:
            applicant_ids = []
            if hasattr(self.biz_detail, 'applicant_id'):
                applicant_ids.append(('app', [self.biz_detail.applicant_id]))
            if hasattr(self.biz_detail, 'is_co_app_changed') and self.biz_detail.is_commond_mark:
                applicant_ids += [('after', self.biz_detail.after_co_app_ids.split(','))]
                applicant_ids += [('before', self.biz_detail.before_co_app_ids.split(','))]

            if hasattr(self.biz_detail, 'is_co_applicants') and self.biz_detail.is_co_applicants:
                applicant_ids.append(('co_app', self.biz_detail.co_applicant_ids.split(',')))

            if hasattr(self.biz_detail, 'transfer_app_id'):
                applicant_ids += [('tra_app', [self.biz_detail.transfer_app_id]),
                                  ('acc_app', [self.biz_detail.acceptor_app_id])]
                if self.biz_detail.is_co_owner:
                    applicant_ids += [('tra_co', self.biz_detail.transfer_co_apps.split(',')),
                                      ('acc_co', self.biz_detail.acceptor_co_apps.split(','))]
            return applicant_ids


class CopyrightOperateService(OrderOperateService):
    """
        版权业务操作类
    """
    def pay_deal(self, payment, **kwargs):
        super(CopyrightOperateService, self).pay_deal(payment)
        self.order.status = OrderStatusMap.WAITE_UPLOAD
        self._recode_order_status_modify()

    def handle_csorder(self, treat_type, stuff_id, next_status):
        if treat_type == 'delegate':
            self.biz_detail.is_delegate_confirmed = True
        if treat_type == 'upload':
            self.add_order_app()
        super(CopyrightOperateService, self).handle_csorder(treat_type, stuff_id, next_status)

    def reset_status(self, stuff_id):
        super(CopyrightOperateService, self).reset_status(stuff_id)

    def get_tip_index(self):
        if self.order.is_paid and self.biz_detail.requisition:
            return 3
        elif self.biz_detail.is_paid:
            return 2
        elif self.order.status == 'wait_payment':
            return 1
        elif self.order.status in ('wait_delegate', 'write_info'):
            return 1

    def _get_order_apps(self):
        """
        返回 需要记录的主体id和主体id的source_type后半截
        """
        if self.is_initialize:
            applicant_ids = []
            if hasattr(self.biz_detail, 'applicant_id'):
                applicant_ids.append(('app', [self.biz_detail.applicant_id]))
            return applicant_ids