#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

import json
from tornado.web import HTTPError
from app.services.base_service import ServiceException
from app.services.basebanservice import BaseBanService
from app.services.ban_bos.mark_bo.mark_transfer_bo import MarkTransferApplyBO, MarkTransferReissueBO
from configs.database_builder import DatabaseBuilder
from app.services.applicant_service import ApplicantBO
from app.daos.mark_transfer_dao import MarkTransferOrderDao, MarkTransferOrder
from app.daos.applicant_dao import ApplicantDao
from app.services.order_operate_service import MarkOperateService


class MarkTransferService(BaseBanService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.biz_dao = MarkTransferOrderDao
        self.operator = MarkOperateService()

    @staticmethod
    def get_biz_obj(order_type):
        if order_type == 'mark_transfer_apply':
            return MarkTransferApplyBO(transfer_co_apps=[],
                                       acceptor_co_apps=[],
                                       transfer_app=ApplicantBO(),
                                       acceptor_app=ApplicantBO(),
                                       biz=order_type)
        elif order_type == 'reissue_mark_transfer':
            return MarkTransferReissueBO(apply_app=ApplicantBO(),
                                         biz=order_type)
        else:
            raise ServiceException(20052, 'we don`t have this biz')

    @staticmethod
    def get_biz_dao(session):
        return MarkTransferOrderDao(session)

    @staticmethod
    def get_data_obj(biz_type):
        return MarkTransferOrder()

    def get_apply_app(self, order_apps):
        tra_acc_app = dict()
        for order_app in order_apps:
            if order_app['source_type'] == 'reissue_mark_transfer_app':
                # 补发商标转让转移证明
                return order_app
            elif order_app['source_type'] == 'mark_transfer_apply_tra_app':
                tra_acc_app['transfer_app'] = order_app
            elif order_app['source_type'] == 'mark_transfer_apply_acc_app':
                tra_acc_app['acceptor_app'] = order_app
        return tra_acc_app

    @staticmethod
    def get_delegate_contract_names(order_apps, apply_app, biz_type):
        if biz_type == 'mark_transfer_apply':
            return [app['name'] for app in order_apps]
        else:
            return [apply_app['name']]

    def deal_biz(self, biz, session):
        mark_bo = self.get_biz_obj(biz.biz)
        mark_bo.update(biz.fields)
        if mark_bo.biz == 'mark_transfer_apply' and (mark_bo.transfer_app_id or mark_bo.transfer_co_apps):
            self._get_applicants(session, mark_bo)
        elif mark_bo.biz == 'reissue_mark_transfer' and mark_bo.applicant_id:
            mark_bo.apply_app_name = ApplicantDao(session).get(mark_bo.applicant_id).name
        return mark_bo

    @staticmethod
    def _get_applicants(session, mark_bo):
        apps = [mark_bo.transfer_app_id, mark_bo.acceptor_app_id]
        # 判断是否有共同申请人
        acceptor_co_apps = mark_bo.acceptor_co_apps
        transfer_co_apps = mark_bo.transfer_co_apps
        is_commen_app = all([acceptor_co_apps, transfer_co_apps])

        apps += transfer_co_apps
        apps += acceptor_co_apps
        #  去重
        apps = dict().fromkeys(apps).keys()
        applicants = ApplicantDao(session).get_dict_by_ids(apps)
        # 以下赋值
        mark_bo.acceptor_app = ApplicantBO(**applicants.get(mark_bo.acceptor_app_id).fields) \
            if mark_bo.acceptor_app_id else ApplicantBO()
        mark_bo.transfer_app = ApplicantBO(**applicants.get(mark_bo.transfer_app_id).fields) \
            if mark_bo.transfer_app_id else ApplicantBO()
        mark_bo.acceptor_co_apps = []
        mark_bo.transfer_co_apps = []
        if is_commen_app:
            for k, v in applicants.items():
                if str(k) in acceptor_co_apps:
                    mark_bo.acceptor_co_apps.append(ApplicantBO(**v.fields))
                if str(k) in transfer_co_apps:
                    mark_bo.transfer_co_apps.append(ApplicantBO(**v.fields))

    def update_applicant(self, user_id, mark_bo):
        """
        :param user_id:
        :param mark_bo:
        :return:
        """
        with self._default_db.create_session() as session:
            mark_dao = MarkTransferOrderDao(session)
            mark = mark_dao.get_by_user_order(user_id, mark_bo.order_id)
            if mark is None:
                raise HTTPError(404)
            if mark.biz != mark_bo.biz:
                raise HTTPError(404)
            mark.update(mark_bo.flat_attributes)
            mark_dao.update(mark)

    def update_biz_info(self, user_id, mark_bo):
        """
        更新
        :param mark_bo:
        :return:
        """
        with self._default_db.create_session() as session:
            mark_dao = MarkTransferOrderDao(session)
            mark = mark_dao.get_by_user_order(user_id, mark_bo.order_id)
            if mark is None:
                raise HTTPError(404)
            # 校验前台传回的biz有没有被修改
            if mark.biz != mark_bo.biz:
                raise HTTPError(404)
            self.update_confirm_able(mark, 'mark_reg_num')
            mark.update(mark_bo.flat_attributes)
            mark_dao.update(mark)

    def update_co_apps(self, user_id, mark_bo):
        """
        更新
        :param mark_bo:
        :return:
        """
        with self._default_db.create_session() as session:
            mark_dao = MarkTransferOrderDao(session)
            mark = mark_dao.get_by_user_order(user_id, mark_bo.order_id)
            if mark is None:
                raise HTTPError(404)
            if mark.biz != 'mark_transfer_apply':
                raise HTTPError(400)
            mark.update(mark_bo.flat_attributes)
            mark_dao.update(mark)