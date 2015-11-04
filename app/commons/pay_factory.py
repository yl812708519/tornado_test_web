#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   __author__ = 'yanglu'

import alipay
import os.path
import yaml
from urllib import urlencode
from hashlib import md5
from tornado.web import HTTPError
from configs.settings import Settings
from app.commons.stringutil import uuid4
from configs.database_builder import DatabaseBuilder


class PayFactory(object):

    @staticmethod
    def get_pay_api(pay_type):
        if pay_type == 'alipay':
            return AlipayFactory.get_instance()
        elif pay_type == 'weixin':
            return WexinPayFactory.get_instance()
        else:
            raise HTTPError(403)

    @staticmethod
    def check_params(params, names):
        if not all(k in params for k in names):
            raise AttributeError('missing parameters')
        return

    @staticmethod
    def get_instance(runmod):
        raise NotImplementedError

    @staticmethod
    def parse_notify(payment_bo, **kwargs):
        """
        处理回调信息，
        主要是筛选信息，返回一个payment_bo
        alipay 需要验证，
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        raise NotImplementedError

    def get_request_url(self, **kwargs):
        """
        alipay: 获取跳转的地址
        weixin_pay: 获取 请求code_url 的地址
        :return:
        :rtype:
        """
        raise NotImplementedError

    @staticmethod
    def initialize_params(total_fee, order_name, payment_id, order_id):
        """
        根据订单信息初始化参数列表
        """
        raise NotImplementedError


class AlipayFactory(alipay.Alipay, PayFactory):

    alipay_config = None
    instance = None

    @staticmethod
    def get_instance(runmod='production'):
        if not AlipayFactory.alipay_config:
            file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/pay.yaml'), 'r')
            yml = yaml.load(file_stream)
            AlipayFactory.alipay_config = yml['alipay'].get(runmod)
        if not AlipayFactory.instance:
            AlipayFactory.instance = AlipayFactory(pid=str(AlipayFactory.alipay_config['pid']),
                                                   key=str(AlipayFactory.alipay_config['key']),
                                                   seller_email=str(AlipayFactory.alipay_config['seller_email']))
        return AlipayFactory.instance

    @staticmethod
    def initialize_params(total_fee, order_name, payment_id, order_id):
        return {'total_fee': total_fee,  # 总价
                'subject': order_name,  # 商品名
                'out_trade_no': payment_id,  # 支付信息id
                'extra_common_param': order_id  # 订单id
                }

    def get_request_url(self, **params):
        params['return_url'] = self.alipay_config.return_url
        params['notify_url'] = self.alipay_config.notify_url
        direct_pay_url = self.create_direct_pay_by_user_url(**params)
        return direct_pay_url

    def parse_notify(self, payment_bo, **params):
        if DatabaseBuilder.run_mode == 'production' and not self.verify_notify(**params):
            # 验证失败。签名错误或者支付宝验证失败
            raise HTTPError(403)
        payment_bo.pay_mode = 'alipay'
        payment_bo.id = params['out_trade_no']
        payment_bo.pay_config = params['seller_email']
        payment_bo.out_trade_no = params['trade_no']
        payment_bo.buyer_account = params['buyer_email']
        payment_bo.pay_fee = params['total_fee']
        payment_bo.payment_time = params['gmt_payment']
        return payment_bo


class WexinPayFactory(PayFactory):
    """
    微信支付流程：
    根据商品数据 公众账号appid/企业号corpid 商户号 等 通过统一下单api 获取code_url
    通过code_url 生成二维码图片
    用户扫码支付
    异步回调，地址在微信公众号配置中
    """
    wxpay_config = None
    instance = None
    get_code_url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'

    def __init__(self, app_id, mch_id, spbill_create_ip):
        self.appid = app_id
        self.mch_id = mch_id
        self.spbill_create_ip = spbill_create_ip

    @staticmethod
    def get_instance(runmod='production'):
        if not WexinPayFactory.wxpay_config:
            file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/pay.yaml'), 'r')
            yml = yaml.load(file_stream)
            WexinPayFactory.wxpay_config = yml['wxpay'].get(runmod)
        if not WexinPayFactory.instance:
            WexinPayFactory.instance = WexinPayFactory(app_id=str(WexinPayFactory.wxpay_config['pid']),
                                                       mch_id=str(WexinPayFactory.wxpay_config['key']),
                                                       spbill_create_ip=str(WexinPayFactory.wxpay_config['seller_email']))
        return AlipayFactory.instance

    @staticmethod
    def generate_md5_sign(**kwargs):
        src = '&'.join(['%s=%s' % (key, value) for key,
                        value in sorted(kwargs.items())])
        return md5(src.encode('utf-8')).hexdigest()

    @staticmethod
    def initialize_params(total_fee, order_name, payment_id, order_id):
        params = {'total_fee': total_fee,  # 总价
                  'body': order_name,  # 商品名
                  'out_trade_no': payment_id,  # 支付信息id
                  'attach': order_id,  # 订单id （附加信息）
                  }
        return params

    def get_request_url(self, **kwargs):
        """
        获取code_url
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        md5_sign = self.generate_md5_sign(**kwargs)
        kwargs['sign'] = md5_sign
        kwargs['nonce_str'] = uuid4()
        self.check_params(kwargs, ('appid', 'mch_id', 'body', 'total_fee', 'treate_type'))
        return self.get_code_url + urlencode(kwargs)

