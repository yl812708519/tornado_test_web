#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from requests import HTTPError

from app.services.ban_bos.mark_bo.mark_change_bo import MarkChangeOrderBO
from app.commons.view_model import ViewModel
from app.daos.applicant_dao import ApplicantDao
from app.daos.mark_category_item_dao import MarkCategoryItemDao
from app.daos.mark_change_dao import MarkChangeOrder, MarkChangeOrderDao
from app.daos.order_dao import Order, OrderDao
from app.services.applicant_service import ApplicantBO, ApplicantService
from app.services.order_operate_service import MarkOperateService
from app.services.basebanservice import BaseBanService
from configs.database_builder import DatabaseBuilder


__author__ = 'zhaowenlei'


class MarkChangeOrderService(BaseBanService):
    permission = None

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.operator = MarkOperateService()
        if self.permission is None:
            self.permission = self.is_permission()

    @staticmethod
    def is_permission():
        def _is_permission(user_id, curr_user_id):
            if user_id != curr_user_id:
                raise HTTPError(404)
            return True
        return _is_permission

    @staticmethod
    def get_biz_dao(session):
        return MarkChangeOrderDao(session)

    def get_apply_app(self, order_apps):
        for order_app in order_apps:
            if order_app['source_type'] in ('reg_col_pro_applicant_app', 'age_rec_applicant_app', 'sub_service_applicant_app'):
                return order_app

    @staticmethod
    def get_data_obj(biz_type):
        return MarkChangeOrder()
    
    def deal_biz(self, biz, session):
        mark_change_bo = MarkChangeOrderBO(**biz.fields)
        app_ids = [unicode(mark_change_bo.applicant_id)]
        if mark_change_bo.is_co_applicant:
            app_ids += mark_change_bo.co_app_ids
        if mark_change_bo.is_co_app_changed:
            app_ids += mark_change_bo.before_co_app_ids
            app_ids += mark_change_bo.after_co_app_ids
        app_ids = [a for a in app_ids if a and int(a)]
        if app_ids:
            applicant_dao = ApplicantDao(session)
            applicant_dict = applicant_dao.get_dict_by_ids(app_ids)
            co_apps, after_co_apps, before_co_apps = [], [], []
            for app_id in app_ids:
                app_bo = ApplicantBO(**applicant_dict.get(long(app_id)).fields)
                if app_id in mark_change_bo.co_app_ids:
                    co_apps.append(app_bo)
                if app_id in mark_change_bo.after_co_app_ids:
                    after_co_apps.append(app_bo)
                if app_id in mark_change_bo.before_co_app_ids:
                    before_co_apps.append(app_bo)
                if app_id == str(mark_change_bo.applicant_id):
                    mark_change_bo.applicant = app_bo
            mark_change_bo.co_apps, mark_change_bo.before_co_apps, mark_change_bo.after_co_apps = \
                co_apps, before_co_apps, after_co_apps
        return mark_change_bo

    @staticmethod
    def get_data_obj(biz_type):
        data_obj = MarkChangeOrder()
        if biz_type in ['reg_col_pro_applicant', 'age_rec_applicant']:
            data_obj.is_confirm_able = 3
        return data_obj

    def update_mark_cha(self, mark_change_bo):
        with self.create_session(self._default_db) as session:
            mark_change_dao = MarkChangeOrderDao(session)
            mark_change = mark_change_dao.get(mark_change_bo.id)
            if mark_change.user_id == mark_change_bo.user_id:
                # 取出值，以防被修改
                mark_change_bo.order_id = mark_change.order_id
                mark_change_bo.created_at = mark_change.created_at
                # 更新
                mark_change = MarkChangeOrder()
                mark_change.update(mark_change_bo.attributes)

                mark_change_dao.update(mark_change)
            else:
                # 报错
                pass

    # def get_by_id(self, mark_change_id, user_id):
    #     with self.create_session(self._default_db) as session:
    #         mark_change_dao = MarkChangeOrderDao(session)
    #         applicant_dao = ApplicantDao(session)
    #         mark_change = mark_change_dao.get(mark_change_id)
    #         mark_change_bo = MarkChangeOrderBO(**mark_change.fields)
    #         if mark_change_bo.common_ids:
    #             mark_change_bo.common_ids = json.loads(mark_change_bo.common_ids)
    #             common_bos = self.gets_applicant_by_ids(session, user_id, mark_change_bo.common_ids)
    #             mark_change_bo.common_marks = ViewModel.to_views(common_bos)
    #
    #         if mark_change_bo.cha_common_ids:
    #             mark_change_bo.cha_common_ids = json.loads(mark_change_bo.cha_common_ids)
    #             cha_common_marks = []
    #             for cha_common_id in mark_change_bo.cha_common_ids:
    #                 source = applicant_dao.get_by_id(user_id, cha_common_id['source_id'])
    #                 target = applicant_dao.get_by_id(user_id, cha_common_id['target_id'])
    #                 cha_common_mark = dict()
    #                 cha_common_mark['source_id'] = ApplicantBO(**source.fields)
    #                 cha_common_mark['target_id'] = ApplicantBO(**target.fields)
    #                 cha_common_marks.append(cha_common_mark)
    #             mark_change_bo.cha_common_marks = cha_common_marks
    #             # cha_common_mark_bos = self.gets_applicant_by_cha_common_ids(session, user_id, mark_change_bo.cha_common_ids)
    #             # mark_change_bo.cha_common_marks = ViewModel.to_views(cha_common_mark_bos)
    #
    #         if mark_change_bo.category_codes:
    #             mark_change_bo.category_codes = json.loads(mark_change_bo.category_codes)
    #
    #         return mark_change_bo

    def update_applicant(self, mark_bo, user_id):
        with self.create_session(self._default_db) as session:
            mark_change_dao = MarkChangeOrderDao(session)
            mark_change = mark_change_dao.get_by_order_user(mark_bo.order_id, user_id)
            if mark_change:
                mark_change.update(mark_bo.flat_attributes)
                mark_change_dao.update(mark_change)
                self.update_confirm_able(mark_change, 'applicant_id')
            else:
                raise HTTPError(404)

    def update_info(self, user_id, mark_bo):
        with self.create_session(self._default_db) as session:
            mark_change_dao = MarkChangeOrderDao(session)
            mark_change = mark_change_dao.get_by_order_user(mark_bo.order_id, user_id)
            if mark_change:
                mark_change.update(mark_bo.flat_attributes)
                mark_change_dao.update(mark_change)
                self.update_confirm_able(mark_change, 'mark_reg_num')
            else:
                raise HTTPError(404)

    def update_attach(self, user_id, mark_bo):
        with self.create_session(self._default_db) as session:
            mark_change_dao = MarkChangeOrderDao(session)
            mark_change = mark_change_dao.get_by_order_user(mark_bo.order_id, user_id)
            if mark_change:
                mark_change.update(mark_bo.flat_attributes)
                mark_change_dao.update(mark_change)
            else:
                raise HTTPError(404)

    def gets_applicant_by_cha_common_ids(self, session, user_id, cha_common_ids):

        c_ids = []
        for cha_common_id in cha_common_ids:
            c_ids.append(cha_common_id['source_id'])
            c_ids.append(cha_common_id['target_id'])

        return self.gets_applicant_by_ids(session, user_id, c_ids)

    @staticmethod
    def get_applicant(user_id, applicant_id):
        applicant_service = ApplicantService()
        return applicant_service.get_by_id(user_id, applicant_id)

    @staticmethod
    def gets_applicant_by_ids(session, user_id, ids):
        applicant_dao = ApplicantDao(session)
        applicants = applicant_dao.gets_applicant_by_ids(user_id, [int(i) for i in ids])
        return [ApplicantBO(**applicant.fields) for applicant in applicants] if applicants else []