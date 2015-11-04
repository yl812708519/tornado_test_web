#!/usr/bin/env python
#coding=utf-8


# 二期需求 ，当前未使用 2015.08.21

from app.commons.biz_model import BizModel, Attribute
from app.commons import dateutil
from app.daos.copyright_dao import CopyrightDao, Copyright
from app.daos.user_profile_dao import UserProfileDao
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder

__author__ = 'zhaowenlei'

class CopyrightBO(BizModel):

    id = Attribute(default=None)
    user_id = Attribute('')
    copyright_name = Attribute(default='')
    copyright_type = Attribute('')
    applicant_name = Attribute(default='')
    status = Attribute(default=0)
    applicant_email = Attribute(default='')
    applicant_mobile = Attribute(default='')
    remark = Attribute(default='')
    is_deleted = Attribute(default=0)
    created_at = Attribute('')


class CopyrightService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def add_copyright(self, copyright_bo):
        with self._default_db.create_session() as session:
            copyright_dao = CopyrightDao(session)
            copyright = Copyright()
            copyright.update(copyright_bo.attributes)
            return copyright_dao.add(copyright)

    def count_gets_by_user_id(self, user_id, offset=0, page_size=10):
        with self._default_db.create_session() as session:
            copyright_dao = CopyrightDao(session)
            total, copyrights = copyright_dao.count_gets_by_user_id(user_id, offset, page_size)
            copyright_bos = [CopyrightBO(**copyright.fields) for copyright in copyrights]
            profile_dao = UserProfileDao(session)
            profile = profile_dao.get_by_user(user_id)
            for copyright_bo in copyright_bos:
                copyright_bo.created_at = dateutil.timestamp_to_string(copyright_bo.created_at)
                if profile:
                    copyright_bo.applicant_name = profile.nickname

            return total, copyright_bos

    def get_by_id(self, copyright_id, user_id):
        with self._default_db.create_session() as session:
            copyright_dao = CopyrightDao(session)
            copyright = copyright_dao.get_by_id(copyright_id, user_id)
            return CopyrightBO(**copyright.fields) if copyright else None

    def update_copyright(self, copyright_bo):
        with self._default_db.create_session() as session:
            copyright_dao = CopyrightDao(session)
            copyright = copyright_dao.get(copyright_bo.id)
            copyright.update(copyright_bo.attributes)
            copyright_dao.update(copyright)

    def delete_by_id(self, copyright_applicant_id, user_id):
        with self._default_db.create_session() as session:
            copyright_dao = CopyrightDao(session)
            return copyright_dao.delete_by_copyright_id(copyright_applicant_id, user_id)