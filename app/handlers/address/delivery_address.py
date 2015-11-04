#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated

from app.commons.view_model import ViewModel
from app.handlers.application import BaseHandler
from app.services.delivery_address_service import DeliveryAddressService, DeliveryAddressBO


class DeliveryAddressHandler(BaseHandler):

    @authenticated
    def get(self, *args):

        """
        跳转到修改页面
        :param args:
        """
        delivery_address_id = self.get_argument("delivery_address_id", None)
        if delivery_address_id:
            delivery_address_service = DeliveryAddressService()
            delivery_address = delivery_address_service.get_by_id(delivery_address_id)
            current_user_id = self.current_user.user_id
            if delivery_address and delivery_address.user_id == current_user_id:
                # 判断收货地址是否是当前用户的地址
                # result = ViewModel(**delivery_address.attributes)

                # area_service = AreaService()
                # provinces = area_service.gets_province()
                # cities = area_service.gets_by_parent_code(delivery_address.province_code)
                # counties = area_service.gets_by_parent_code(delivery_address.city_code)
                # towns = area_service.gets_by_parent_code(delivery_address.county_code)
                #
                # result["provinces"] = [ViewModel(**pro.attributes) for pro in provinces]
                # result["cities"] = [ViewModel(**pro.attributes) for pro in cities]
                # result["counties"] = [ViewModel(**pro.attributes) for pro in counties]
                # result["towns"] = [ViewModel(**pro.attributes) for pro in towns]
                result = dict(change_delivery_address=ViewModel.to_view(delivery_address))
                self.write(result)

    @authenticated
    def post(self, *args, **kwargs):
        """
        保存收货地址
        :param args:
        :param kwargs:
        """
        current_user = self.get_current_user()
        current_user_id = current_user.user_id
        delivery_address = self.get_form("delivery_address")
        delivery_address_service = DeliveryAddressService()
        delivery_address_bo = DeliveryAddressBO(**delivery_address)
        delivery_address_bo.user_id = current_user_id
        delivery_address_bo = delivery_address_service.add(delivery_address_bo)
        self.write({'id': delivery_address_bo.id})
        # 获取上一步操作的地址
        # referer = self.request.headers['referer']
        # self.redirect(referer)

    @authenticated
    def put(self, *args, **kwargs):
        """
        修改收货地址
        :param args:
        :param kwargs:
        """
        current_user = self.get_current_user()
        current_user_id = current_user.user_id
        # 根据current_user_id 和 delivery_address_id 查询收货地址,然后再更新
        delivery_address = self.get_form("change_delivery_address")
        delivery_address_id = delivery_address["id"]
        delivery_address_service = DeliveryAddressService()

        delivery_address_bo = delivery_address_service.get_by_id(delivery_address_id)
        if delivery_address_bo.user_id == current_user_id:
            delivery_address_bo.name = delivery_address["name"]
            delivery_address_bo.mobile = delivery_address["mobile"]
            delivery_address_bo.province_code = delivery_address["province_code"]
            delivery_address_bo.city_code = delivery_address.get("city_code", None)
            delivery_address_bo.area_code = delivery_address.get("area_code", None)
            delivery_address_bo.address = delivery_address.get("address", None)
            delivery_address_bo.postalcode = delivery_address.get("postalcode", None)
            delivery_address_bo.created_at = delivery_address.get("created_at", None)
            delivery_address_service.update(delivery_address_bo)
        # 获取上一步操作的地址
        referer = self.request.headers['referer']
        self.redirect(referer)

    @authenticated
    def delete(self, *args, **kwargs):
        """
        删除收货地址
        :param args:
        :param kwargs:
        """
        current_user = self.get_current_user()
        current_user_id = current_user.user_id

        delivery_address_id = self.get_argument("address.id", None)

        if delivery_address_id:
            delivery_address_service = DeliveryAddressService()
            delivery_address_bo = delivery_address_service.get_by_id(delivery_address_id)
            if delivery_address_bo.user_id == current_user_id:
                delivery_address_service.delete(delivery_address_bo)

        self.write('1')


class DeliveryAddressesHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        user_id = self.current_user.user_id
        delivery_address_service = DeliveryAddressService()
        # current_page = int(self.get_argument('currentPage', 1))
        # page_size = self.get_argument('page_size', 5)
        # offset = (int(current_page) - 1) * page_size

        delivery_address_bos = delivery_address_service.gets_by_user_id(user_id)
        result = dict(delivery_addresses=ViewModel.to_views(delivery_address_bos),
                      add_delivery_address=ViewModel.to_view(DeliveryAddressBO()),
                      change_delivery_address=ViewModel.to_view(DeliveryAddressBO()),
                      active_id='addresses')
        self.render('ban_views/address/address_list.html', **result)