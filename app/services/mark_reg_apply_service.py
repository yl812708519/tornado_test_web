#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from tornado.web import HTTPError
from app.services.base_service import ServiceException
from app.services.basebanservice import BaseBanService
from app.services.ban_bos.mark_bo.mark_apply_bo import MarkRegCorrectItemBO, MarkRegProvideProofBO, MarkRegReissueBO
from configs.database_builder import DatabaseBuilder
from app.daos.mark_reg_apply_dao import MarkRegApplyOrder, MarkRegApplyDao
from app.services.order_operate_service import MarkOperateService
from app.daos.applicant_dao import ApplicantDao
from app.services.applicant_service import ApplicantBO


class MarkRegApplyService(BaseBanService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.biz_dao = MarkRegApplyDao
        self.operator = MarkOperateService()

    @staticmethod
    def get_biz_bo(order_type):
        if order_type == 'reissue_reg_credential':
            mark_bo = MarkRegReissueBO(reissue_reason='')
        elif order_type == 'provide_mark_reg_proof':
            mark_bo = MarkRegProvideProofBO(category_codes='')
        elif order_type == 'correct_mark_reg_items':
            mark_bo = MarkRegCorrectItemBO(category_codes='', correct_items='')
        else:
            raise ServiceException(20052, 'we don`t have this service')
        return mark_bo

    def deal_biz(self, mark, session):
        return self._deal_mark_apply(mark, session)

    def get_apply_app(self, order_apps):
        return order_apps[0]

    @staticmethod
    def get_biz_dao(session):
        return MarkRegApplyDao(session)

    @staticmethod
    def get_data_obj(biz_type):
        data_obj = MarkRegApplyOrder()
        # if biz_type == 'correct_mark_reg_items':
        #     data_obj.is_confirm_able = 3
        return data_obj

    def update_apply_info(self, apply_bo, user_id):
        """
        更新 申请信息
        :param apply_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            apply_dao = MarkRegApplyDao(session)
            mark_apply = apply_dao.get_by_order_user(apply_bo.order_id, user_id)
            if mark_apply:
                if mark_apply.is_confirmed:
                    raise ServiceException(20070, 'has confirmed')
                self.update_confirm_able(mark_apply, 'applicant_id')

                mark_apply.applicant_id = apply_bo.applicant_id
                mark_apply.mark_reg_num = apply_bo.mark_reg_num

                apply_dao.update(mark_apply)
            else:
                raise HTTPError(404)

    def update_apply_main(self, apply_bo, user_id, biz):
        with self.create_session(self._default_db) as session:
            apply_dao = MarkRegApplyDao(session)
            mark_apply = apply_dao.get_by_order_user(apply_bo.order_id, user_id)
            if mark_apply and mark_apply.biz == biz:
                if mark_apply.is_confirmed:
                    raise ServiceException(20070, 'has confirmed')
                mark_apply.update(apply_bo.flat_attributes)

                apply_dao.update(mark_apply)
            else:
                raise HTTPError(404)

    @staticmethod
    def _deal_mark_apply(mark_apply, session, is_applicant=True):
        mark_apply_bo = MarkRegApplyService.get_biz_bo(mark_apply.biz)
        mark_apply_bo.update(mark_apply.fields)
        mark_apply_bo.correct_items = mark_apply.correct_items
        if is_applicant:
            applicant = ApplicantDao(session).get(mark_apply_bo.applicant_id)
            mark_apply_bo.applicant = ApplicantDao(session).get(mark_apply_bo.applicant_id).fields \
                if applicant is not None else ApplicantBO().attributes
        if mark_apply.biz != 'reissue_reg_credential':
            mark_apply_bo.category_code_list = mark_apply.category_codes.split(',')
        return mark_apply_bo
