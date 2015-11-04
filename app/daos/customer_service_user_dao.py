#! /usr/bin/env python
# coding=utf-8
from sqlalchemy import Column, BigInteger, String, func
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import UpdatedAtMixin, CreatedAtMixin, IdMixin

__author__ = 'zhaowenlei'


class CustomerServiceUser(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 后台客服用户id
    staff_user_id = Column(BigInteger)
    # 客服名称
    name = Column(String(20))
    # 客服昵称
    nickname = Column(String(20))
    # QQ号码
    qq = Column(String(20))
    # 固定电话
    phone = Column(String(20))
    # 手机号
    mobile = Column(String(20))
    # 邮箱
    email = Column(String(30))
    # 客服简介
    introduction = Column(String(200))


class CustomerServiceStat(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 后台客服用户id
    csu_id = Column(BigInteger)
    # 未处理订单
    untreated_order_num = Column(BigInteger)
    # 已确认订单
    confirm_order_num = Column(BigInteger)


@model(CustomerServiceUser)
class CustomerServiceUserDao(DatabaseTemplate):

    def gets(self, offset=None, page_size=None):
        return self.session.query(self.model_cls).filter().limit(page_size).offset(offset).all()

    def get_count(self):
        return self.session.query(func.count('*')).select_from(self.model_cls).filter().scalar()

    def gets_by_csu_id(self, user_id):
        return self.session.query(self.model_cls).filter(self.model_cls.staff_user_id == user_id).all()

    def get_by_csu_id(self, csu_id):
        return self.session.query(self.model_cls).filter(self.model_cls.id == csu_id).first()


@model(CustomerServiceStat)
class CustomerServicestatsDao(DatabaseTemplate):
    def get_by_csu_id(self, csu_id):
        return self.session.query(self.model_cls).filter(self.model_cls.csu_id == csu_id).first()

    def update_untreated_order_num(self, csu_id, untreated_order_num):
        return self.session.query(self.model_cls).filter(self.model_cls.csu_id == csu_id).\
            update({self.model_cls.untreated_order_num: untreated_order_num})



