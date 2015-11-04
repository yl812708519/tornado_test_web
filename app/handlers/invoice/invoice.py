#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import authenticated, HTTPError

from app.commons import dateutil
from app.commons.view_model import ViewModel
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.ban_bos.invoice import InvoiceAddReqBO, InvoiceReqBO
from app.services.delivery_address_service import DeliveryAddressService, DeliveryAddressBO
from app.services.invoice_basic_service import InvoiceBasicService
from app.services.invoice_order_service import InvoiceOrderService
from app.services.invoice_service import InvoiceService
from app.services.base_service import ServiceException


__author__ = 'zhaowenlei'


class InvoiceHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        # 获取总开票金额
        # 选取的条数

        user_id = self.current_user.user_id
        ids = self.get_arguments('id')
        if len(ids) <= 0:
            raise ServiceException(20090, 'You have no choice of order')
        ids = [int(id) for id in ids if len(ids) > 0]
        invoice_bo = InvoiceReqBO()
        invoice_service = InvoiceService()
        order_bos = invoice_service.gets_order_by_ids(ids)
        # 防止在发票确认页修改url的id，所以此处判如果没有取出数据，则抛出异常
        if len(order_bos) <= 0:
            raise ServiceException(20090, 'You have no choice of order')
        # 根据实际取出的条数为准
        invoice_bo.select_order_num = len(order_bos)
        for order_bo in order_bos:
            # 判断要开票的订单是否是属于该用户的订单
            if order_bo.user_id != user_id:
                raise ServiceException(20090, 'You have no choice of order')
            invoice_bo.invoice_price += order_bo.price

        # 重新取出有效的订单id，防止前端伪造数据
        ids = [order_bo.id for order_bo in order_bos]
        invoice_basic_service = InvoiceBasicService()
        # 此处得单独向页面写invoice_basic_bo基本信息，如果没有基本细心要提示他添加，页面给添加按钮
        invoice_basic_bo = invoice_basic_service.get_by_uid(user_id)
        if invoice_basic_bo:
            invoice_bo.invoice_type = invoice_basic_bo.invoice_type
            invoice_bo.invoice_type_name = invoice_basic_service.get_value_by_status_and_type('invoice_type',
                                                                                              invoice_basic_bo.invoice_type)
            invoice_bo.make_invoice_type = invoice_basic_bo.make_invoice_type
            invoice_bo.make_invoice_type_name = invoice_basic_service.get_value_by_status_and_type('make_invoice_type',
                                                                                                   invoice_basic_bo.make_invoice_type)
            invoice_bo.title = invoice_basic_bo.title
        delivery_address_service = DeliveryAddressService()
        delivery_address_bos = delivery_address_service.gets_by_user_id(user_id)

        result = dict(invoice=invoice_bo,
                      delivery_addresses=ViewModel.to_views(delivery_address_bos),
                      add_delivery_address=ViewModel.to_view(DeliveryAddressBO()),
                      order_nums=ids,
                      change_delivery_address=ViewModel.to_view(DeliveryAddressBO()))

        self.render('ban_views/invoice/invoice_confirmation.html', **result)

class InvoiceSubmitHandler(RestfulAPIHandler):

    @authenticated
    def post(self, *args, **kwargs):
        req_bo = self.get_req_bo(InvoiceAddReqBO, need_validate=True)
        # self.validate(req_bo, is_raise_all=True)
        req_bo.user_id = self.current_user.user_id
        invoice_service = InvoiceService()
        invoice_service.add_invoice(req_bo)
        self.write('1')


class InvoicesHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        user_id = self.current_user.user_id
        invoice_service = InvoiceService()
        start_time = self.get_argument('start_time', '')
        end_time = self.get_argument('end_time', '')
        mailing_status = self.get_argument('mailing_status', '')
        invoice_status = self.get_argument('invoice_status', '')
        current_page = int(self.get_argument('current_page', 1))
        page_size = self.get_argument('page_size', 5)
        offset = (int(current_page) - 1) * page_size

        start_time_temp = ''
        end_time_temp = ''
        if start_time:
            start_time_temp = dateutil.string_to_timestamp(start_time[0:10])
            start_time_temp += 86400 * 1000
            start_time = dateutil.timestamp_to_string(start_time_temp)
        if end_time:
            end_time_temp = dateutil.string_to_timestamp(end_time[0:10])
        data = invoice_service.count_by_user_id(user_id, start_time_temp, end_time_temp,
                                                mailing_status, invoice_status, offset, page_size)
        for invoice_bo in data['invoice_bos']:
            invoice_bo.created_at = dateutil.timestamp_to_string(invoice_bo.created_at, '%Y-%m-%d')
        result = dict(invoices=ViewModel.to_views(data['invoice_bos']),
                      total=data['total'],
                      current_page=current_page,
                      total_page=int((data['total']+page_size-1)/page_size),
                      active_id='invoices',
                      start_time=start_time[0:10],
                      end_time=end_time[0:10],
                      mailing_status=mailing_status,
                      invoice_status=invoice_status)

        self.render('ban_views/invoice/invoices.html', **result)


class InvoiceDetailHandler(BaseHandler):

    @authenticated
    def get(self, invoice_id):
        user_id = self.current_user.user_id
        invoice_service = InvoiceService()
        invoice_order_service = InvoiceOrderService()
        invoice_basic_service = InvoiceBasicService()
        invoice_bo = invoice_service.get_by_id(invoice_id, user_id)

        invoice_bo.created_at = dateutil.timestamp_to_string(invoice_bo.created_at, '%Y-%m-%d %H:%M:%S')
        try:
            invoice_bo.invoice_type_name = invoice_basic_service.get_value_by_status_and_type('invoice_type',
                                                                                          invoice_bo.invoice_type)
        except:
            invoice_bo.invoice_type_name = invoice_bo.invoice_type
        invoice_order_bos = invoice_order_service.gets_by_invoice_id(invoice_bo.id)
        for invoice_order_bo in invoice_order_bos:
            invoice_order_bo.created_at = dateutil.timestamp_to_string(invoice_order_bo.created_at, '%Y-%m-%d %H:%M:%S')
        order_ids = [int(invoice_basic_bo.order_id) for invoice_basic_bo in invoice_order_bos]
        order_bos = invoice_service.gets_order_by_ids(order_ids)
        order = dict()
        for order_id in order_ids:
            for order_bo in order_bos:
                if order_id == order_bo.id:
                    order[order_id] = order_bo.price
        result = dict(invoice=ViewModel.to_view(invoice_bo),
                      invoice_orders=ViewModel.to_views(invoice_order_bos),
                      order=order)
        self.render('ban_views/invoice/invoice_detail.html', **result)


class InvoiceDemandHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        user_id = self.current_user.user_id
        invoice_service = InvoiceService()
        invoice_basic_service = InvoiceBasicService()
        start_time = self.get_argument('start_time', '')
        end_time = self.get_argument('end_time', '')
        invoice_price_s = self.get_argument('invoice_price_s', '')
        invoice_price_e = self.get_argument('invoice_price_e', '')
        current_page = int(self.get_argument('current_page', 1))
        page_size = self.get_argument('page_size', 5)
        offset = (int(current_page) - 1) * page_size

        start_time_temp = ''
        end_time_temp = ''
        if start_time:
            start_time_temp = dateutil.string_to_timestamp(start_time[0:10])
            # 前端时间插件传过来的开始时间总是比选的少了一天，故要加一天
            start_time_temp += 86400 * 1000
            start_time = dateutil.timestamp_to_string(start_time_temp)
        if end_time:
            end_time_temp = dateutil.string_to_timestamp(end_time[0:10])
        data = invoice_service.gets_by_user_price_date_invoice_able(user_id, start_time_temp, end_time_temp,
                                                                    invoice_price_s, invoice_price_e, offset, page_size)
        total_price = 0
        for order in data['order_bos']:
            total_price += order.price
            order.created_at = dateutil.timestamp_to_string(order.created_at, '%Y-%m-%d')

        is_invoice_basic = 1 if invoice_basic_service.get_by_uid(user_id) else 0
        result = dict(orders=ViewModel.to_views(data['order_bos']),
                      total=data['total'],
                      total_price=total_price,
                      current_page=current_page,
                      total_page=int((data['total']+page_size-1)/page_size),
                      is_invoice_basic=is_invoice_basic,
                      active_id='invoice_demands',
                      s_time=start_time[0:10],
                      e_time=end_time[0:10],
                      price_s=invoice_price_s,
                      price_e=invoice_price_e)

        self.render('ban_views/invoice/invoice_demands.html', **result)


class InvoiceCancelHandler(RestfulAPIHandler):

    @authenticated
    def post(self, *args, **kwargs):
        user_id = self.current_user.user_id
        invoice_id = self.get_argument('invoice_id', '')
        invoice_service = InvoiceService()
        invoice = invoice_service.get_by_id(invoice_id, user_id)
        if invoice:
            if invoice.invoice_status:
                self.write_except(ServiceException('20403', '亲,发票状态为已开发票,不能作废!'))
            else:
                res = invoice_service.update_invoice_by_id(invoice_id, user_id)
                self.write_success() if res else self.write_except(ServiceException('20403', '亲,发票状态为已开发票,不能作废!'))
        else:
            raise HTTPError(404)