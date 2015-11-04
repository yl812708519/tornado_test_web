#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__author__ = 'yanglu'

import alipay
import os.path
import yaml
from configs.settings import Settings


class AlipayFactory(alipay.Alipay):

    alipay_config = None
    instance = None

    @staticmethod
    def get_instance(runmod='production'):
        if not AlipayFactory.alipay_config:
            file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/alipay.yaml'), 'r')
            yml = yaml.load(file_stream)
            AlipayFactory.alipay_config = yml.get(runmod)
        if not AlipayFactory.instance:
            AlipayFactory.instance = AlipayFactory(pid=str(AlipayFactory.alipay_config['pid']),
                                                   key=str(AlipayFactory.alipay_config['key']),
                                                   seller_email=str(AlipayFactory.alipay_config['seller_email']))
        return AlipayFactory.instance

    def get_direct_pay_by_user_url(self, params, return_url, notify_url):
        params['return_url'] = return_url
        params['notify_url'] = notify_url
        direct_pay_url = self.create_direct_pay_by_user_url(**params)
        return direct_pay_url

