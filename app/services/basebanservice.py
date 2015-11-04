#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.services.customer_service_order_service import CustomerServiceOrderService

__author__ = 'yanglu'

from json import loads
from tornado.web import HTTPError
from app.services.base_service import BaseService
from app.commons.biz_model import BizModel, Attribute
from app.daos.order_dao import Order, OrderDao
from app.services.business_service import BusinessService
from app.daos.order_applicant_dao import OrderApplicantDao
from app.services.base_service import ServiceException
from app.services.applicant_service import ApplicantService


class ContextBO(BizModel):
    current_user_id = Attribute(None)
    remote_ip = Attribute(None)


class ReqBO(BizModel):
    context = Attribute(None, attri_type=ContextBO)


class BaseBanService(BaseService):
    """
        为了统一订单部分功能例如 确认订单，合同列表
        以上功能需要调用不同的数据表，这里把他们重构到一起
        因为不同订单在不同数据库中
    """

    @staticmethod
    def get_biz_dao(session):
        raise NotImplementedError

    @staticmethod
    def get_data_obj(biz_type):
        """
        获得一个空的数据库对象，具体那个表要看子类
        由于更改，出现了同表的业务但是确认步数不一样的情况
        所以有一些要单独判断下,biz_type 用于确认is_confirm_able 的值

        """
        raise NotImplementedError

    def deal_biz(self, biz, session):
        """
        处理数据库对象为bo对象
        :param session:
        :type session:
        :param biz:
        :type biz:
        :return:
        :rtype:
        """
        raise NotImplementedError

    def get_apply_app(self, order_apps):
        """
        获取 申请主体，用于填写公共表单 的甲方
        :param order_apps: 该订单所有的order_applicants bo 对象
        :type order_apps: bos
        :return:
        :rtype:
        """
        raise NotImplementedError

    def detail_pay(self, order, session):
        """
        付款后做业务单独的处理
        版权业务需要再付款后更改两次状态
        :param order: 订单对象
        :type order: Order
        :return:
        :rtype:
        """
        pass


    @staticmethod
    def get_delegate_contract_names(order_apps, apply_app, biz_type):
        """
        获得代理委托书的 委托人list， 用于循环代理委托书
        """
        return [app['name'] for app in order_apps]

    @staticmethod
    def update_confirm_able(biz, field):
        if not getattr(biz, field) and biz.is_confirm_able > 1:
            biz.is_confirm_able -= 1

    def add(self, user_id, biz_type):
        # 业务信息和订单的添加
        # 目前业务订单的添加逻辑都一样。添加的只有user_id，order_id
        # 所以放到基类中处理,s
        with self.create_session(self._default_db) as session:
            order = Order()
            cs_oder_service = CustomerServiceOrderService()
            order.order_type = biz_type
            produce_info = BusinessService().get_by_name(biz_type)
            if produce_info is None:
                raise ServiceException
            order.name = produce_info.produce
            order.user_id = user_id
            order.price = produce_info.service_charge + produce_info.official_charge
            order.csu_id = cs_oder_service.get_biz_csu_id(session, biz_type, user_id)
            order = OrderDao(session).add(order)
            # 添加业务信息
            biz_dao = self.get_biz_dao(session)
            data_obj = self.get_data_obj(biz_type)
            data_obj.user_id = user_id
            data_obj.order_id = order.id
            if hasattr(data_obj, 'biz'):
                data_obj.biz = biz_type
            if hasattr(data_obj, 'service_category'):
                data_obj.service_category = biz_type
            biz_dao.add(data_obj)

            return order.id

    def get_for_contract(self, order_id, user_id):
        """
            为合同获取 业务信息和order_applicants
        """
        with self.create_session(self._default_db) as session:
            biz_dao = self.get_biz_dao(session)
            biz = biz_dao.get_by_user_id_order_id(user_id, order_id)
            biz_bo = self.deal_biz(biz, session)

            order_apps = OrderApplicantDao(session).gets_by_user_order_source(user_id, order_id)
            if not order_apps:
                # 防止程序错误， 导致下载合同时没有order_app
                app_ids = self.get_order_apps(order_id, biz_bo.user_id, session)
                if app_ids:
                    ApplicantService._add_order_apps(app_ids, order_id, biz.biz, session)
                order_apps = OrderApplicantDao(session).gets_by_user_order_source(user_id, order_id)

            order_app_dicts = [order_app.fields for order_app in order_apps]
            apply_app = self.get_apply_app(order_app_dicts)
            return biz_bo, order_app_dicts, apply_app
    #
    # def order_confirm(self, order_id, user_id):
    #     with self.create_session(self._default_db) as session:
    #         biz_dao = self.get_biz_dao(session)
    #         biz_obj = biz_dao.get_by_user_id_order_id(user_id, order_id)
    #         if biz_obj:
    #             if biz_obj.is_confirm_able == 1:
    #                 biz_obj.is_confirmed = True
    #                 biz_dao.update(biz_obj)
    #                 order = OrderDao(session).get(order_id)
    #                 CustomerServiceOrderService().add_cs_order(order, 'review', order.csu_id, session)
    #             else:
    #                 raise ServiceException(20055, 'this order can`t confirm')
    #         else:
    #             raise HTTPError(404)

    def get_order_apps(self, order_id, user_id, session):
        """
        返回 需要记录的主体id和主体id的source_type后半截
        """
        biz_dao = self.get_biz_dao(session)
        biz_obj = biz_dao.get_by_user_id_order_id(user_id, order_id)
        if biz_obj:
            applicant_ids = []
            if hasattr(biz_obj, 'applicant_id'):
                applicant_ids.append(('app', [biz_obj.applicant_id]))
            if hasattr(biz_obj, 'is_commond_mark') and biz_obj.is_commond_mark:
                    if biz_obj.mark_common_aft_ids:
                        applicant_ids += [('cha_aft', loads(biz_obj.mark_common_aft_ids))]
                    if biz_obj.mark_common_bef_ids:
                        applicant_ids += [('cha_bef', loads(biz_obj.mark_common_bef_ids))]
            if hasattr(biz_obj, 'is_co_applicants') and biz_obj.is_co_applicants:
                applicant_ids.append(('co_app', loads(biz_obj.co_applicant_ids)))

            if hasattr(biz_obj, 'transfer_app_id'):
                applicant_ids += [('tra_app', [biz_obj.transfer_app_id]),
                                  ('acc_app', [biz_obj.acceptor_app_id])]
                if biz_obj.is_co_owner:
                    applicant_ids += [('tra_co', loads(biz_obj.transfer_co_apps)),
                                      ('acc_co', loads(biz_obj.acceptor_co_apps))]
            return applicant_ids
        else:
            raise HTTPError(404)

    def handle_csorder(self, order_id, treat_type, session):
        """
        根据处理类型。更新业务信息
        :param order_id:
        :type order_id:
        :param treat_type:
        :type treat_type:
        :param session:
        :type session:
        :return:
        :rtype:
        """
        biz_dao = self.get_biz_dao(session)
        biz = biz_dao.get_by_order(order_id)
        if not biz:
            raise ServiceException(20075, 'not found')
        if treat_type == 'review':
            if not biz.is_confirmed:
                raise ServiceException(20070, 'this biz has not confirmed')
        elif treat_type == 'delegate':
            biz.is_delegate_confirmed = True
        biz.is_reviewed = True
        biz_dao.update(biz)

    def reset_confirm(self, session, order_id):
        biz_dao = self.get_biz_dao(session)
        biz = biz_dao.get_by_order(order_id)
        if not biz:
            raise ServiceException(20075, 'not found')
        biz.is_confirmed = False
        biz.is_delegated = False
        biz.is_delegate_confirmed = False
        biz.is_reviewed = False
        biz_dao.update(biz)

