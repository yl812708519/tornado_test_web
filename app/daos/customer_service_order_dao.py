#! /usr/bin/env python
# coding=utf-8

from sqlalchemy import Column, BigInteger, String, func, desc
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import UpdatedAtMixin, CreatedAtMixin, IdMixin

__author__ = 'zhaowenlei'

class CustomerServiceOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 客服id
    csu_id = Column(BigInteger)
    # 订单
    order_id = Column(BigInteger)
    # 处理类型(待填订单，确认订单)
    treat_type = Column(String(20))
    # 完成状态(未处理、已确认)
    is_finished = Column(BigInteger, default=0)

class CustomerServiceBiz(IdMixin, BaseModel):

    # 后台客服用户id
    csu_id = Column(BigInteger)
    # 负责业务名
    biz_name = Column(String(50))


@model(CustomerServiceOrder)
class CustomerServiceOrderDao(DatabaseTemplate):

    def gets_by_csu_id(self, csu_id):
        return self.session.query(self.model_cls).filter(CustomerServiceOrder.csu_id == csu_id).all()

    def gets_for_workbench(self, offset, count, *condition):
        return self.session.query(self.model_cls).\
            filter(*condition).order_by(desc(self.model_cls.created_at))\
            .offset(offset).limit(count).all()

    def get_by_csu_order_treat_type(self, csu_id, order_id, treat_type):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).\
            filter(self.model_cls.csu_id == csu_id).\
            filter(self.model_cls.treat_type == treat_type).\
            filter(self.model_cls.is_finished == False).first()

    def get_by_order(self, order_id):
        return self.session.query(self.model_cls).filter(self.model_cls.order_id == order_id).first()

    def get_by_order_treat_type(self, order_id, treat_type):
        return self.session.query(self.model_cls).filter(self.model_cls.order_id == order_id,
                                                         self.model_cls.treat_type == treat_type).first()

@model(CustomerServiceBiz)
class CustomerServiceBizDao(DatabaseTemplate):

    def get_by_csu_id(self, csu_id):
        return self.session.query(self.model_cls).filter(CustomerServiceBiz.csu_id == csu_id).all()

    def update_customer_service_biz(self, customer_service_user):
        return self.session.query(self.model_cls).filter(CustomerServiceBiz.csu_id == customer_service_user['id']).\
            update({CustomerServiceBiz.biz_name: customer_service_user['biz_name']})

    def gets_by_type(self, order_type):
        return self.session.query(self.model_cls).filter(CustomerServiceBiz.biz_name == order_type).all()

