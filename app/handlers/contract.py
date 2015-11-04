#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.contract import Create_PDF_into_buffer, get_cn_price
from app.commons.dateutil import today_timestamp, timestamp_to_string
from configs.settings import Settings
import os
import yaml
from app.services.contract_service import ContractService
from app.services.oss_upload_service import OssUploadService
from app.services.user_service import UserService, UserProfileBO
from app.services.business_service import BusinessService
from tornado.web import authenticated
from app.handlers.application import BaseHandler, HTTPError
from app.services.order_service import OrderService, ServiceException
from app.services.order_payment_service import OrderPaymentService


class BaseContractHandler(BaseHandler):

    mark_delegate = None
    copyright_delegate = None
    font = None
    seal = None

    def __init__(self, application, request, **kwargs):
        super(BaseContractHandler, self).__init__(application, request, **kwargs)
        self.order_cn_price = ''
        order_id = self.get_argument('order')
        self.contract = contract = self.get_argument('con')
        order_service = OrderService()
        user = self.current_user
        self.result = result = dict(img_site=OssUploadService().download_image_site(),
                                    contract=contract)
        result['order'] = order = order_service.get(order_id, user.user_id)
        if order is None:
            raise HTTPError(404)
        if order.is_paid:
            # 订单已支付
            biz_service = order_service.get_detail_service(order.order_type)
            result['detail'], result['order_apps'], apply_app = \
                biz_service.get_for_contract(order_id, user.user_id)
            biz_bo = BusinessService().get_by_name(order.order_type)
            biz_contracts = ContractService().get_dict_by_biz_name(order.order_type, biz_bo.type, result['detail'].base_type)
            contract_fields = biz_contracts.get(contract, None)
            if contract in ('business', 'copyright_business'):
                # 三方合同需要当前用户的信息
                result['user_profile'] = UserService().get_profile(user.user_id)
                result['order_payment'] = OrderPaymentService().get_by_order(order_id)
                result['order_cn_price'] = get_cn_price(result['order'].price)
            if contract_fields:
                # 业务信息处理
                result['delegate'] = self.get_delegate(result['detail'].base_type)

                result['apply_app'] = apply_app if order.order_type != 'mark_transfer_apply' \
                    else apply_app['transfer_app']

                result['delegate_names'] = biz_service.get_delegate_contract_names(result['order_apps'],
                                                                                   result['apply_app'],
                                                                                   order.order_type)
                result['agency_delegate'] = self.get_delegate(result['detail'].base_type)
                self.contract_name = contract_fields['contract_name']
                result['font'] = self.get_font()
                result['seal'] = self.get_seal()
                result['today'] = timestamp_to_string(today_timestamp())
            else:
                raise ServiceException(20080, 'contract error')
        else:
            raise ServiceException(20091, 'not paid')

    @classmethod
    def get_font(cls):
        if not cls.font:
            cls.font = os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'fonts', 'Microsoft_vista_yahei.ttf')
        return cls.font

    @classmethod
    def get_seal(cls):
        if not cls.seal:
            cls.seal = dict(eking=os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'zhang', 'eking_zhang.png'),
                            yestar=os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'zhang', 'yestar_zhang.png'))
        return cls.seal

    @classmethod
    def get_delegate(cls, base_type):
        # 通过yaml获取代理信息
        if base_type not in ('mark', 'copyright'):
            raise SystemError()
        if not getattr(cls, base_type+'_delegate'):
            file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/agency_delegate_config.yaml'), 'r')
            yml = yaml.load(file_stream)
            setattr(cls, base_type+'delegate', yml.get(base_type))
        return getattr(cls, base_type+'delegate')



class ContractHandler(BaseContractHandler):
    """
        合同 预览。详情页
    """

    @authenticated
    def get(self):
        if self.contract == 'business':
            if not all([self.result['user_profile'].address,
                        self.result['user_profile'].mobile,
                        self.result['user_profile'].nickname]):
                self.redirect('/user/profile')
        self.render('ban_views/contract/'+self.result['detail'].base_type+'/'+self.contract+'.html', render_type='view', **self.result)

class ContractDownloadHandler(BaseContractHandler):

    @authenticated
    def get(self):
        """
        生成合同提供下载
        :return:
        """
        pdf_buffer = self.created_contract()
        self.set_header('Content-Type', 'file')
        self.set_header("Content-type", "application/octet-stream;charset=utf-8")
        self.set_header("Accept-Ranges", "bytes")
        self.set_header("Content-Disposition", "attachment; filename="+self.contract_name+".pdf")
        self.write(pdf_buffer.dest.getvalue())

    def created_contract(self):

        if self.contract == 'business':
            if not all([self.result['user_profile'].address,
                        self.result['user_profile'].mobile,
                        self.result['user_profile'].nickname]):
                self.redirect('/user/profile')
        html = self.render_string('ban_views/contract/'+self.result['detail'].base_type+'/'+self.contract+'.html',  render_type='download', **self.result)
        return Create_PDF_into_buffer(html, self.font)

