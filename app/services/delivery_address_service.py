#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.base_service import BaseService
from app.commons.biz_model import BizModel, Attribute
from app.daos.delivery_address_dao import DeliveryAddressDao, DeliveryAddress
from configs.database_builder import DatabaseBuilder


class DeliveryAddressBO(BizModel):
    id = Attribute(None)
    user_id = Attribute('')
    name = Attribute('')
    mobile = Attribute('')
    province_code = Attribute('')
    city_code = Attribute('')
    area_code = Attribute('')
    # town_code = Attribute('')
    address = Attribute('')
    # 邮政编码
    postalcode = Attribute('')


class DeliveryAddressService(BaseService):
    """收货地址服务类，封装与收货地址相关的业务逻辑"""

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def add(self, delivery_address_bo):
        """
        添加一个收货地址
        :param delivery_address_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            delivery_address = DeliveryAddress()
            delivery_address.update(delivery_address_bo.attributes)
            return DeliveryAddressBO(**(delivery_address_dao.add(delivery_address)).fields)

    def delete(self, delivery_address_bo):
        """
        删除一个收货地址
        :param delivery_address_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            delivery_address = DeliveryAddress()
            delivery_address.update(delivery_address_bo.attributes)
            return delivery_address_dao.delete(delivery_address)

    def delete_by_id(self, identity):
        """
        根据id删除一个收货地址
        :param delivery_address_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            return delivery_address_dao.delete_by_id(identity)

    def update(self, delivery_address_bo):
        """
        更新一个收货地址
        :param delivery_address_bo:
        :return:更新之后的对象
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            delivery_address = DeliveryAddress()
            delivery_address.update(delivery_address_bo.attributes)
            return delivery_address_dao.update(delivery_address)

    def get_by_id(self, identity):
        """
        根据id,查询用户的收货地址,is_deleted=1的记录无法获取
        :param identity:收货地址id
        :return:
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            delivery_address = delivery_address_dao.get(identity)
            return DeliveryAddressBO(**delivery_address.fields) if delivery_address else None

    def gets_by_user_id(self, user_id):
        """
        根据用户id,查询用户的收货地址
        :param user_id:
        :return:
        """
        with self.create_session(self._default_db) as session:
            delivery_address_dao = DeliveryAddressDao(session)
            delivery_addresses = delivery_address_dao.gets_by_user_id(user_id)
            return [DeliveryAddressBO(**delivery_address.fields) for delivery_address in delivery_addresses]
