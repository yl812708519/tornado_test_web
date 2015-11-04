#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, Float, String, Boolean, BigInteger, func, desc, or_
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, UpdatedAtMixin, IsDeletedMixin
from app.commons.database_mixin import CreatedAtMixin
from configs.order_status_map import OrderStatusMap

__author__ = 'freeway'


class OrderType(object):
    TRADEMARK_REGISTER = 'mark_reg'

class Order(IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin, BaseModel):

    user_id = Column(String(36), default=None)
    csu_id = Column(BigInteger)
    name = Column(String(200), default=None)
    order_type = Column(String(70), default=None)
    price = Column(Float, default=None)
    status = Column(String(50), default=OrderStatusMap.WRITE_INFO)
    is_paid = Column(Boolean, default=False)
    is_tiped = Column(Boolean, default=False)
    is_in_trash = Column(Boolean, default=False)
    is_invoiced = Column(Boolean, default=False)
    is_invoice_able = Column(Boolean, default=False)


@model(Order)
class OrderDao(DatabaseTemplate):
    """ 订单数据访问对象

    """

    def get_by_uid_order_id(self, uid, order_id):
        """ 根据uid和order_id获取订单实体

        :param uid:
        :param order_id:
        :return:
        """
        return self.get_first_by_criterion(Order.id == order_id,
                                           Order.user_id == uid,
                                           Order.is_in_trash == 0,
                                           Order.is_deleted == 0)

    def gets_by_uid(self, uid, offset=None, count=None):
        """ 根据uid查询数据

        :param uid:
        :param offset:
        :param count:
        :return:
        """
        return self.gets_by_uid_is_in_trash(uid, False, offset=offset, count=count)

    def count_by_uid(self, uid):
        return self.count(Order.user_id == uid, Order.is_in_trash == False, Order.is_deleted == False)

    def gets_by_uid_is_in_trash(self, uid, is_in_trash=False, offset=None, count=None):
        """ 根据uid和is_in_trash查询数据

        :param uid:
        :param is_in_trash:
        :param offset:
        :param count:
        :return:
        """
        return self.session.query(Order)\
            .filter(Order.user_id == uid,
                    Order.is_in_trash == is_in_trash,
                    Order.is_deleted == False)\
            .order_by(desc(Order.created_at)).offset(offset).limit(count)

    def count_by_uid_is_in_trash(self, uid, is_in_trash):
        return self.count(Order.user_id == uid, Order.is_in_trash == is_in_trash, Order.is_deleted == False)

    def gets_by_user_price_date_invoice_able(self, user_id, start_date='', end_date='', start_price='', end_price='',
                                             offset=0, page_size=10):
        criterion = [Order.is_deleted == 0,
                     Order.user_id == user_id,
                     Order.is_invoice_able == 1]
        criterion.append(Order.price >= start_price) if start_price else None
        criterion.append(Order.price <= end_price) if end_price else None
        criterion.append(Order.created_at >= start_date) if start_date else None
        criterion.append(Order.created_at <= end_date) if end_date else None

        total = self.count(*criterion)
        orders = self.session.query(self.model_cls).\
            filter(*criterion).\
            order_by(desc(self.model_cls.created_at)).\
            limit(page_size).offset(offset).all()

        return total, orders

    def gets_by_ids_user(self, order_ids, user_id):
        no_order_instances = self.session.query(self.model_cls).\
            filter(self.model_cls.user_id == user_id).\
            filter(self.model_cls.id.in_(order_ids)).all()
        inst_dict = dict()
        for instance in no_order_instances:
            inst_dict[instance.id] = instance
        instances = list()
        for identity in order_ids:
            instance = inst_dict.get(identity, None)
            if instance is not None:
                instances.append(instance)
        return instances

    def get_first_by_type_uid(self, order_type, user_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_type == order_type).filter(self.model_cls.user_id == user_id).\
            order_by(desc(self.model_cls.id)).first()