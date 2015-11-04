#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String, Text, func, desc
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import CreatedAtMixin, UpdatedAtMixin, IdMixin

__author__ = 'zhaowenlei'


class Copyright(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    user_id = Column(String(45))
    copyright_type = Column(String(100), default='')
    copyright_name = Column(String(100), default='')
    applicant_name = Column(String(100), default='')
    status = Column(BigInteger, default=0)
    applicant_email = Column(String(50), default='')
    applicant_mobile = Column(String(20), default='')
    remark = Column(Text, default='')
    is_deleted = Column(BigInteger, default=0)


@model(Copyright)
class CopyrightDao(DatabaseTemplate):

    def count_gets_by_user_id(self, user_id, offset=0, page_size=10):
        """获取版权申请的列表,必须是当前用户才可以获取
        :return:
        """
        total = self.session.query(func.count('*')).select_from(self.model_cls).\
            filter(Copyright.is_deleted != 1, Copyright.user_id == user_id).scalar()
        copyrights = self.session.query(self.model_cls).\
            filter(Copyright.is_deleted != 1, Copyright.user_id == user_id).\
            order_by(desc(self.model_cls.created_at)).\
            limit(page_size).offset(offset).all()

        return total, copyrights

    def get_by_id(self, copyright_id, user_id):
        return self.session.query(self.model_cls).filter(Copyright.id == copyright_id, Copyright.user_id == user_id).first()

    def delete_by_copyright_id(self, copyright_applicant_id, user_id):
        return self.session.query(self.model_cls).\
            filter(Copyright.id == copyright_applicant_id,
                   Copyright.user_id == user_id).update({Copyright.is_deleted: 1})