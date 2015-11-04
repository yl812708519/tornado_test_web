#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.daos.copyright_owner_dao import CopyrightOwnerDao, CopyrightOwner
from app.services.base_service import BaseService
from app.commons.biz_model import BizModel, Attribute
from configs.database_builder import DatabaseBuilder


__author__ = 'zhaowenlei'

class CopyrightOwnerBO(BizModel):
    biz_id = Attribute(None)
    name = Attribute(default='')
    type = Attribute(default='')
    region = Attribute(default='')
    province = Attribute(default='')
    city = Attribute(default='')
    certi_type = Attribute(default='')
    certi_num = Attribute(default='')
    com_type = Attribute(default='')
    park = Attribute(default='')
    sign_situation = Attribute(default='')

class CopyrightOwnerService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def update(self, req_bo):
        with self.create_session(self._default_db) as session:
            copyright_owner_dao = CopyrightOwnerDao(session)
            copyright_owner = copyright_owner_dao.get_by_biz_id(req_bo.biz_id)
            if copyright_owner:
                copyright_owner.update(req_bo.attributes)
                copyright_owner_dao.update(copyright_owner)
            else:
                copyright_o = CopyrightOwner()
                copyright_o.update(req_bo.attributes)
                copyright_owner_dao.add(copyright_o)

    def get_by_biz(self, biz_id):
        with self.create_session(self._default_db) as session:
            copyright_owner_dao = CopyrightOwnerDao(session)
            copyright_owner = copyright_owner_dao.get_by_biz_id(biz_id)
            if copyright_owner:
                return CopyrightOwnerBO(**copyright_owner.fields)
            else:
                return CopyrightOwnerBO()