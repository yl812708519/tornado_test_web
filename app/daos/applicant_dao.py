#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import String, func, desc
from sqlalchemy import Column
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, UpdatedAtMixin
from app.commons.database_mixin import CreatedAtMixin

__author__ = 'freeway'


class ApplicantType(object):
    PERSON = 'person'  # 个人
    COM = 'com'  # 公司


class ApplicantRegion(object):
    CN = 'cn'  # 中国大陆
    HK = 'hk'  # 中国香港
    TW = 'tw'  # 中国澳门
    OTHER = 'other'  # 其他国籍


class Applicant(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    user_id = Column(String(36), default=None)
    name = Column(String(200), default=None)
    app_type = Column(String(40), default=None)
    region = Column(String(20), default='cn')  # 区域：cn（中国大陆）、hk（中国香港）、tw（中国台湾）、mo（中国澳门）、other（其他国籍）
    nationality_name = Column(String(100), default='')  # 国籍名称（只有在region选择other的时候出现）
    company_name = Column(String(100), default='')  # 公司名称/个体工商户名称
    company_en_name = Column(String(200), default='')  # 公司英文名称（只有在region非cn的时候出现）
    certificate_num = Column(String(100), default='')  # cn:营业执照号 tw:登记证编号 hk/mo/other:注册证书编号
    register_address = Column(String(100), default='')  # 注册地址/个体工商户执照地址
    register_en_address = Column(String(200), default='')  # 注册英文地址（只有在region非cn的时候出现）
    certificate_img1 = Column(String(200), default='')  # 证书/个体工商户执照 图1
    certificate_img2 = Column(String(200), default='')  # 证书 图2 （只有在region非cn的时候出现）
    certificate_img3 = Column(String(200), default='')  # 证书 图3 （只有在region非cn的时候出现）
    certificate_img4 = Column(String(200), default='')  # 证书 图4 （只有在region非cn的时候出现）
    person_name = Column(String(50), default='')  # 真实姓名
    person_en_name = Column(String(200), default='')  # 真实英文名
    passport_num = Column(String(50), default='')  # 护照号 (非cn出现)
    id_card_num = Column(String(18), default='')  # 身份证号 (cn出现)
    person_address = Column(String(100), default='')  # cn:身份证地址 非cn:中文地址
    person_en_address = Column(String(200), default='')  # 英文地址(非cn出现)
    passport_img = Column(String(200), default='')  # 护照图片
    id_card_front_img = Column(String(200), default='')  # 身份证正面照片
    id_card_back_img = Column(String(200), default='')  # 身份证背面照片


@model(Applicant)
class ApplicantDao(DatabaseTemplate):

    def gets_by_uid(self, uid):
        query = self.session.query(Applicant)\
            .filter(Applicant.user_id == uid)\
            .order_by(Applicant.created_at)
        return query.all()

    def count_gets_by_user_id(self, user_id, offset=0, page_size=10):

        total = self.session.query(func.count('*')).select_from(self.model_cls).\
            filter(Applicant.user_id == user_id).scalar()
        applicants = self.session.query(self.model_cls).filter(Applicant.user_id == user_id).\
            order_by(desc(self.model_cls.created_at)).limit(page_size).offset(offset).all()

        return total, applicants

    def gets_applicant_by_ids(self, user_id, ids):
        no_order_instances = self.session.query(self.model_cls).filter(self.model_cls.id.in_(ids),
                                                                       self.model_cls.user_id == user_id).all()
        inst_dict = dict()
        for instance in no_order_instances:
            inst_dict[instance.id] = instance
        instances = list()
        for identity in ids:
            instance = inst_dict.get(identity, None)
            if instance is not None:
                instances.append(instance)
        return instances

    def get_by_id(self, user_id, applicant_id):
        return self.session.query(self.model_cls).filter(Applicant.id == applicant_id,
                                                         Applicant.user_id == user_id).first()