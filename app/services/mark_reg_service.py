#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

import json
from app.commons.contract import multiple_replace
from tornado.web import HTTPError
from app.services.base_service import ServiceException
from app.services.basebanservice import BaseBanService, CustomerServiceOrderService
from app.services.business_service import BusinessService
from app.services.ban_bos.mark_bo.mark_reg_bo import MarkRegOrderBO
from configs.database_builder import DatabaseBuilder
from app.daos.business_dao import BusinessDao
from app.daos.mark_reg_order_dao import MarkRegOrder, MarkRegOrderDao
from app.services.mark_category_item_service import MarkCategoryBO, MarkCategoryItemDao, MarkCategoryItem
from app.services.oss_upload_service import OssUploadService
from app.daos.order_dao import OrderDao, Order
from app.daos.applicant_dao import ApplicantDao
from app.services.order_operate_service import MarkOperateService


mark_type_map = dict(english='英文',
                     chinese='中文',
                     graph='图形',
                     number='数字')


class MarkRegService(BaseBanService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.mark_type_re = multiple_replace(mark_type_map)
        self.operator = MarkOperateService()

    @staticmethod
    def _is_permission(mark_reg, user):
        """
        验证商标的修改权限
        :param mark_reg:
        :param user:
        :return:
        """
        if mark_reg is None:
            raise HTTPError(404)
        if mark_reg.user_id != user.user_id:
            raise HTTPError(404)
            # raise ServiceException(20050, 'no permission')
        if mark_reg.is_confirmed is True:
            raise ServiceException(20051, 'confirmed mark can`t edit')
        return True

    @staticmethod
    def get_biz_dao(session):
        return MarkRegOrderDao(session)

    @staticmethod
    def get_data_obj(biz_type):
        return MarkRegOrder()

    @staticmethod
    def _get_file_url(mark_bo):
        upload_file_service = OssUploadService()
        if mark_bo.voice_file:
            mark_bo.voice_file_url = upload_file_service.download_site("yestar") + mark_bo.voice_file

        if mark_bo.collective_list:
            mark_bo.collective_list_url = upload_file_service.download_site("yestar") + mark_bo.collective_list

    def deal_biz(self, mark_reg, session):
        mark_reg_bo = MarkRegOrderBO()
        mark_reg_bo.update(mark_reg.fields)
        mark_reg_bo.mark_type = self.mark_type_re(mark_reg_bo.mark_type)
        self._get_applicant(session, mark_reg_bo)
        self._get_category(session, mark_reg_bo)
        return mark_reg_bo

    def get_apply_app(self, order_apps):
        for order_app in order_apps:
            if order_app['source_type'] in ('mark_reg_app', 'collective_mark_reg_app', 'prove_mark_reg_app'):
                return order_app

    @staticmethod
    def _get_category(session, mark_reg_bo):
        """
        处理商标对象的分类
        :param session:
        :param mark_reg_bo:

        """
        if mark_reg_bo.category:
            items = mark_reg_bo.items
            itemtrees = mark_reg_bo.itemtree
            category_ids = items + itemtrees
            category_ids.append(mark_reg_bo.category)
            c_dict = MarkCategoryItemDao(session).get_dict_by_ids(category_ids)
            item_names = []
            itemtree_names = []
            for cid in category_ids:
                c_obj = c_dict[long(cid)]
                if not isinstance(c_obj, MarkCategoryItem):
                    continue
                if cid in items:
                    item_names.append(MarkCategoryBO(**c_obj.fields))
                elif cid in itemtrees:
                    itemtree_names.append(MarkCategoryBO(**c_obj.fields))
                elif cid == mark_reg_bo.category:
                    category_bo = MarkCategoryBO(**c_obj.fields)
            mark_reg_bo.category_name = category_bo.name
            mark_reg_bo.category = category_bo
            mark_reg_bo.itemtree_names = itemtree_names
            mark_reg_bo.item_names = item_names

    @staticmethod
    def _get_applicant(session, mark_reg_bo):
        """
        获取 主体和共同申请人主体信息
        :param session:
        :param mark_reg_bo:
        :return:
        """
        if mark_reg_bo.applicant_id:
            app_dao = ApplicantDao(session)
            applicant_ids = [mark_reg_bo.applicant_id]

            applicant_ids += mark_reg_bo.co_applicant_ids

            applicants = app_dao.get_dict_by_ids(applicant_ids)
            mark_reg_bo.applicant = dict(name=applicants[mark_reg_bo.applicant_id].name,
                                         app_type=applicants[mark_reg_bo.applicant_id].app_type)
            if mark_reg_bo.is_co_applicants:
                del applicants[mark_reg_bo.applicant_id]

                if not applicants:
                    mark_reg_bo.co_applicant_ids = []

                mark_reg_bo.co_applicants = [dict(name=co_applicant.name, app_type=co_applicant.app_type)
                                             for co_applicant in applicants.values()]

        else:
            mark_reg_bo.applicant = dict(name='',
                                         app_type='')


    def mark_forecast_add(self, mark_bo, user_id):
        with self.create_session(self._default_db) as session:
            order = Order()
            cs_oder_service = CustomerServiceOrderService()
            order.order_type = 'mark_reg'
            produce_info = BusinessService().get_by_name('mark_reg')
            if produce_info is None:
                raise ServiceException
            order.name = produce_info.produce
            order.user_id = user_id
            order.price = produce_info.service_charge + produce_info.official_charge
            order.csu_id = cs_oder_service.get_biz_csu_id(session, 'mark_reg', user_id)
            order = OrderDao(session).add(order)
            # 添加业务信息
            biz_dao = MarkRegOrderDao(session)
            data_obj = MarkRegOrder()
            data_obj.update(mark_bo.attributes)
            data_obj.user_id = user_id
            data_obj.order_id = order.id
            # if mark_bo.name and mark_bo.mark_img and mark_bo.description:
            data_obj.is_confirm_able = 3
            if hasattr(data_obj, 'biz'):
                data_obj.biz = 'mark_reg'
            biz_dao.add(data_obj)

            return order.id

    def update_applicant(self, user, mark_bo):
        """
        更新主题信息
        :param user:
        :type user:
        :param mark_bo:
        :type mark_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            mark_order_dao = MarkRegOrderDao(session)
            mark_reg = mark_order_dao.get_by_user_id_order_id(user.user_id, mark_bo.order_id)
            if self._is_permission(mark_reg, user):
                self.update_confirm_able(mark_reg, 'applicant_id')
                mark_reg.update(mark_bo.flat_attributes)
                if mark_bo.is_co_applicants:
                    # 拼接json
                    mark_reg.co_applicant_ids = ','.join(mark_bo.co_applicant_ids)
                mark_order_dao.update(mark_reg)

    def update_mark_info(self, mark_reg_bo, user):
        """
        更新 商标信息
        :param mark_reg_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            mark_order_dao = MarkRegOrderDao(session)
            mark_reg = mark_order_dao.get_first_by_order_user(mark_reg_bo.order_id, user.user_id)
            if mark_reg.biz != mark_reg_bo.biz:
                raise ServiceException(20075, 'biz type is error')

            if self._is_permission(mark_reg, user):
                self.update_confirm_able(mark_reg, 'name')
                mark_reg.update(mark_reg_bo.flat_attributes)

                mark_order_dao.update(mark_reg)

    def update_category(self, mark_reg_bo, user):
        """
        更新商标注册 分类信息
        :param mark_reg_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            mark_order_dao = MarkRegOrderDao(session)
            mark_reg = mark_order_dao.get_first_by_order_user(mark_reg_bo.order_id, user.user_id)

            if self._is_permission(mark_reg, user):
                self.update_confirm_able(mark_reg, 'category')
                items = mark_reg_bo.items

                mark_reg.update(mark_reg_bo.flat_attributes)

                mark_order_dao.update(mark_reg)
                if mark_reg.biz == 'mark_reg':
                    length = len(items)
                    business = BusinessDao(session).get_by_name('mark_reg')
                    price = business.service_charge + business.official_charge
                    if length > 9:
                        price += (length - 10) * 80
                    order_dao = OrderDao(session)
                    order = order_dao.get(mark_reg.order_id)
                    # 计算订单的价钱
                    if order.price != price:
                        order.price = price
                        order_dao.update(order)
                    return price

    def update_attach(self, mark_reg_bo, user):
        """
        更新 商标附加信息 部分
        :param mark_reg_bo:
        :return: 订单编号(用以跳转至订单页面)
        """
        with self.create_session(self._default_db) as session:
            mark_order_dao = MarkRegOrderDao(session)
            mark_reg = mark_order_dao.get_first_by_order_user(mark_reg_bo.order_id, user.user_id)

            mark_reg.update(mark_reg_bo.flat_attributes)

            mark_order_dao.update(mark_reg)
            return mark_reg.order_id

