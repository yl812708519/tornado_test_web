#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons import dateutil
from app.commons.biz_model import Attribute, BizModel
from app.daos.customer_service_user_dao import CustomerServiceUserDao
from app.daos.customer_service_order_dao import CustomerServiceOrderDao
from app.services.base_service import BaseService
from app.services.email_service import EmailService, EmailTemplate
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'


class CustomerServiceUserBO(BizModel):

    id = Attribute(None)
    # 后台客服用户id
    staff_user_id = Attribute(None)
    # 客服名称
    name = Attribute('')
    # 客服昵称
    nickname = Attribute('')
    # QQ号码
    qq = Attribute('')
    # 固定电话
    phone = Attribute('')
    # 手机号
    mobile = Attribute('')
    # 邮箱
    email = Attribute('')
    # 客服简介
    introduction = Attribute('')


class CustomerServiceStatsBO(BizModel):

    # 后台客服用户id
    csu_id = Attribute('')
    # 未处理订单
    untreated_order_num = Attribute(default=0)
    # 已确认订单
    confirm_order_num = Attribute(default=0)


class CustomerServiceUserService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get_by_csu_id(self, csu_id):
        with self._default_db.create_session() as session:
            customer_service_user_dao = CustomerServiceUserDao(session)
            cs_user = customer_service_user_dao.get_by_csu_id(csu_id)
            return CustomerServiceUserBO(**cs_user.fields) \
                if cs_user else CustomerServiceUserBO()

    def get_by_order_id(self, order_id):
        """
        先拿 csorder表中的csu_id, 再取代填人员得信息
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """
        with self._default_db.create_session() as session:
            cs_order = CustomerServiceOrderDao(session).get_by_order(order_id)
            if cs_order:
                cs_user = CustomerServiceUserDao(session).get_by_csu_id(cs_order.csu_id)
                if cs_user:
                    return CustomerServiceUserBO(**cs_user.fields)

    def create_cs_notice_email(self, treat_type, order_name, email):
        EmailService().create_email(email,
                                    EmailTemplate.ORDER_NOTICE.format(dateutil.timestamp_to_string(dateutil.timestamp(), '%H:%M'),
                                                                      order_name,
                                                                      '代填' if treat_type == 'delegate' else '审核'))