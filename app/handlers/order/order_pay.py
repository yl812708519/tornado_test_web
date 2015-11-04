#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'
import qrcode
import logging
import io
from tornado.web import authenticated
from configs.database_builder import DatabaseBuilder
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.business_service import BusinessService
from app.services.order_service import OrderService
from app.services.ban_bos.order_bo import OrderPaymentBO
from app.services.order_payment_service import OrderPaymentService
from app.commons.pay_factory import PayFactory
import tornado.gen
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler, HTTPError, urlparse


class OrderPayHandler(BaseHandler):
    """
    支付逻辑：
    拼接参数，根据order_type确认回调的路径(为了减少不同数据表的重复代码)
    -》支付后的本站逻辑在BaseBanHandler -> BaseBanService

    """

    @authenticated
    def post(self, pay_type):
        """
        支付跳转
        :return:
        """
        user = self.current_user
        order_id = self.get_argument('order_id')
        order_tip = float(self.get_argument('order_tip', False))
        is_invoice = self. get_argument('is_invoice', 0)

        if order_id:
            order_service = OrderService()
            order = order_service.get(order_id, user.user_id)
            if order is None:
                raise HTTPError(404)
            biz_service = BusinessService()
            biz = biz_service.get_by_name(order.order_type)
            price = self.get_total_price(biz, is_invoice, order_tip, order)
            payment_id = OrderPaymentService().add_payment(order, order_tip, biz, is_invoice)
            if DatabaseBuilder.run_mode == 'production':
                pay_instance = PayFactory.get_instance(pay_type)
                params = pay_instance.initialize_params(price, order.name, payment_id, order.id)
                url = pay_instance.get_request_url(params)
                self.redirect(url)
            else:
                self.redirect('/pay/test?trade_no=23132131231&seller_email=zhifubao@eking.mobi&buyer_email=test@eking.mobi&gmt_payment=156313615246&out_trade_no='+str(payment_id)+'&total_fee='+str(price))
        else:
            raise HTTPError(400, 'The lack of critical data')

    @staticmethod
    def get_total_price(biz, is_invoice, order_tip, order, biz_detail=None):
        price = biz.official_charge + biz.service_charge
        if order.order_type == 'mark_reg' and price != order.price:
            # 普通商标注册要增加 超过10个小项的费用
            if not biz_detail:
                biz_detail_service = OrderService.get_detail_service(order.order_type)
                biz_detail = biz_detail_service.get_by_user_id_order_id(order.user_id, order.id)
            length = len(biz_detail.item_names)
            if length > 9:
                price += (length - 10) * 80

        if int(is_invoice) and biz.service_charge == 0:
            price = float(price) + (float(price) * float(biz.tax))
        if order_tip and int(order_tip) > 0:
            # 叫你想坑我。。。
            price = float(price) + abs(int(order_tip))
        return price


class OrderPayNotifyHandler(BaseHandler):

    # 阻止_xsrf校验
    def check_xsrf_cookie(self):
        pass

    def get(self, *args, **kwargs):
        """
        同步回调，付款后跳转到这里
        :param args:
        :param kwargs:
        :return:
        """
        params = self._get_url_arg()
        if DatabaseBuilder.run_mode == 'production':
            self.redirect('/order/'+str(params['extra_common_param']))
        else:
            raise HTTPError(404)

    def post(self, notify_type, *args, **kwargs):
        """
        异步回调
        :param args:
        :param kwargs:
        :return:
        """
        params = self._get_url_arg()     # 支付宝带过来的参数
        order_id = self._pay_order(notify_type, **params)
        if DatabaseBuilder.run_mode == 'production':
            print 'success'
            self._write_buffer.append('success')
            self.finish()
        else:
            self.redirect('/order/'+str(order_id))

    @staticmethod
    def _pay_order(notify_type, **params):
        """
        真正修改订单状态
        :param order_id:
        :return:
        """
        # 修改订单状态
        payment_bo = OrderPaymentBO()
        pay_factory = PayFactory.get_pay_api(notify_type)
        pay_factory.parse_notify(payment_bo, params)
        return OrderPaymentService().pay_order(payment_bo)

    def _get_url_arg(self):
        params = dict()
        for k, v in self.request.arguments.iteritems():
            params[k] = self.get_argument(k)
        return params


class WxPayQRCodeHandler(RestfulAPIHandler):
    """
        请求 生成二维码ajax
    """

    @authenticated
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        user = self.current_user
        order_id = self.get_argument('order_id')
        order_tip = float(self.get_argument('order_tip', False))
        is_invoice = self. get_argument('is_invoice', 0)

        if order_id:
            order_service = OrderService()
            order = order_service.get(order_id, user.user_id)
            if order is None:
                raise HTTPError(404)
            biz_service = BusinessService()
            biz = biz_service.get_by_name(order.order_type)
            price = OrderPayHandler.get_total_price(biz, is_invoice, order_tip, order)
            payment_id = OrderPaymentService().add_payment(order, order_tip, biz, is_invoice)
            pay_factory = PayFactory.get_pay_api('wxpay')
            params = pay_factory.initialize_params(price, order.name, payment_id, order.id)
            params['trade_type'] = 'NATIVE'
            get_code_url = pay_factory.get_request_url(**params)
            try:
                response = yield tornado.gen.Task(AsyncHTTPClient().fetch, get_code_url)
                code_url = response.body
            except Exception, e:
                logging.error(e.message)
                raise HTTPError(403, e.message)
            else:
                # 创建 二维码
                qr = qrcode.QRCode(
                    version=4,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=8,
                    border=2,
                )
                qr.add_data(code_url)
                qr.make(fit=True)
                img = qr.make_image()
                io_stream = io.BytesIO()
                img.save(io_stream)
                self.set_header('Content-type', 'image/jpg')
                self.set_header('Content-length', len(io_stream.getvalue()))
                self.write(io_stream.getvalue())


class PayTestHandler(BaseHandler):
    """
     测试用的 支付
     页面上用来发送post请求
    """
    def get(self):
        kwargs = self.request.arguments
        self.render('ban_views/order/pay_test.html', result=kwargs)





