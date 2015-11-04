#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created_at: 2015-02-11 17:41:54
# created_by: generate script
from tornado.web import HTTPError
from app.commons import dateutil

__author__ = 'zhaowenlei'

from app.services.ban_bos.applicant import ApplicantBO
from app.daos.applicant_dao import ApplicantDao, Applicant
from app.services.base_service import BaseService, ServiceException
from configs.database_builder import DatabaseBuilder
from app.daos.order_applicant_dao import OrderApplicant, OrderApplicantDao


class ApplicantService(BaseService):
    """applicants表服务类，封装与applicants表相关的业务逻辑

    """

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def get_value_by_type(get_type, value):
        d = {'region': {'cn': '中国大陆', 'hk': '中国香港',
                        'tw': '中国台湾', 'mo': '中国澳门','other': '其他国籍'},
             'app_type': {'person': "个人主体", 'com': "企业主体"}}

        return d[get_type][value]

    def get_by_id(self, user_id, applicant_id):
        """根据 applicant_id 查询单条记录

        :param applicant_id:applicant表 id
        :return: applicants 表中单条记录
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            applicant = applicant_dao.get_by_id(user_id, applicant_id)

            if applicant is not None:
                applicant_bo = ApplicantBO(**applicant.fields)
                applicant_bo.temp_region = self.get_value_by_type('region', applicant_bo.region)
                applicant_bo.temp_app_type = self.get_value_by_type('app_type', applicant_bo.app_type)
                applicant_bo.created_at = dateutil.timestamp_to_string(applicant_bo.created_at, '%Y-%m-%d %H:%M:%S')
                return applicant_bo
            else:
                raise HTTPError(404)

    def add(self, applicant_bo):
        """添加方法

        :param applicant_bo:applicant表 BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            applicant = Applicant()
            applicant.update(applicant_bo.attributes)
            return applicant_dao.add(applicant)

    def delete(self, applicant_bo):
        """根据对象删除applicants表中对应数据

        :param applicant_bo:applicant表 BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            applicant = applicant_dao.get(applicant_bo.id)
            if applicant is not None:
                return applicant_dao.delete(applicant)
            else:
                raise ServiceException(20404, "data is not exist")

    def delete_by_id(self, applicant_id):
        """根据id删除applicants表中对应数据

        :param applicant_id:applicant表 id
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            applicant = applicant_dao.get(applicant_id)
            if applicant is not None:
                return applicant_dao.delete_by_id(applicant_id)
            else:
                raise ServiceException(20404, "data is not exist")

    @staticmethod
    def _add_order_apps(app_id_touples, order_id, order_type, session):
        """
        复制主体信息 到 order_applicants表
        :param app_id_touples:
        :param order_id:
        :return:
        """
        app_ids = []
        for app in app_id_touples:
            app_ids += (app[1])
        # 去重
        app_ids = dict().fromkeys(app_ids).keys()
        applicants = ApplicantDao(session).get_dict_by_ids(app_ids)
        order_applicants = []
        for app_touple in app_id_touples:
            for app_id in app_touple[1]:
                applicant = applicants.get(long(app_id), '')
                if applicant:
                    order_applicant = OrderApplicant()
                    # order_applicant.update(**applicant.fields)
                    for k, v in applicant.fields.iteritems():
                        if hasattr(order_applicant, k):
                            setattr(order_applicant, k, v)
                    order_applicant.applicant_id = applicant.id
                    order_applicant.id = None
                    order_applicant.source_id = order_id
                    order_applicant.source_type = order_type + '_' + app_touple[0]
                    order_applicants.append(order_applicant)

        if not order_applicants:
            raise ServiceException(20090, '该订单未关联任何主体信息，请联系客服人员')
        OrderApplicantDao(session).add_all(order_applicants)

    @staticmethod
    def delete_order_applicants(order_id, session):
        """
        重置确认状态时，删除已生成的order_applicant
        :param order_id:
        :type order_id:
        :return:
        :rtype:
        """
        OrderApplicantDao(session).delete_all_by_order_id(order_id)

    def update(self, applicant_bo):
        """更新方法

        :param applicant_bo:applicant表 BO对象
        :return: 操作结果
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            applicant = applicant_dao.get(applicant_bo.id)
            if applicant is not None:
                applicant = Applicant()
                applicant.update(applicant_bo.attributes)
                return applicant_dao.update(applicant)
            else:
                raise ServiceException(20404, "data exist")

    def count_gets_by_user_id(self, user_id, offset=0, page_size=10):
        """获取列表和数据条数

        :param user_id:
        """
        with self.create_session(self._default_db) as session:
            applicant_dao = ApplicantDao(session)
            total, applicants = applicant_dao.count_gets_by_user_id(user_id, offset, page_size)
            applicant_bos = [ApplicantBO(**applicant.fields) for applicant in applicants]
            for applicant_bo in applicant_bos:
                # applicant_bo.region = self.get_value_by_type('region', applicant_bo.region)
                applicant_bo.temp_region = self.get_value_by_type('region', applicant_bo.region)
                applicant_bo.temp_app_type = self.get_value_by_type('app_type', applicant_bo.app_type)
                applicant_bo.created_at = dateutil.timestamp_to_string(applicant_bo.created_at, '%Y-%m-%d %H:%M:%S')

            return dict(total=total,
                        applicant_bos=applicant_bos)

    @staticmethod
    def _gets_by_ids(session, ids):
        applicants = ApplicantDao(session).gets_by_ids(ids)
        return applicants

    def gets_applicant_by_ids(self, user_id, applicant_ids):
        with self.create_session(self._default_db) as session:
            if applicant_ids:
                applicant_dao = ApplicantDao(session)
                applicants = applicant_dao.gets_applicant_by_ids(user_id, applicant_ids)

                return [ApplicantBO(**applicant.fields) for applicant in applicants] if applicants else None
            else:
                return list()