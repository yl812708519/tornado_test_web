#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger
from sqlalchemy import String
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, UpdatedAtMixin
from app.commons.database_mixin import CreatedAtMixin

__author__ = 'freeway'


class OrderApplicant(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):
    user_id = Column(String(36), default=None)
    applicant_id = Column(BigInteger)  # 原始主体id
    source_type = Column(String(40), default=None)  # 来源类型 申请主体:mark_reg_order_app/联合申请人主体:mark_reg_order_coapp
    source_id = Column(String(70), default=None)  # 来源id
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


@model(OrderApplicant)
class OrderApplicantDao(DatabaseTemplate):

    def get_by_uid_aid_source_type_source_id(self, user_id, applicant_id, source_type, source_id):
        self.get_first_by_criterion(OrderApplicant.user_id == user_id,
                                    OrderApplicant.applicant_id == applicant_id,
                                    OrderApplicant.source_type == source_type,
                                    OrderApplicant.source_id == source_id)

    def gets_by_uid_aid_source_type_source_id(self, user_id, applicant_id, source_type, source_id):
        return self.session.query(self.model_cls)\
            .filter(OrderApplicant.user_id == user_id,
                    OrderApplicant.applicant_id == applicant_id,
                    OrderApplicant.source_type == source_type,
                    OrderApplicant.source_id == source_id).all()

    def get_by_uid_source_type_source_id(self, user_id, source_type, source_id):
        return self.get_first_by_criterion(OrderApplicant.user_id == user_id,
                                           OrderApplicant.source_type == source_type,
                                           OrderApplicant.source_id == source_id)

    def gets_by_uid_source_type_source_id(self, user_id, source_type, source_id):
        """
        获取订单的 主体列表
        :param user_id:
        :param source_type:
        :param scource_id:
        :return:
        """
        return self.session.query(self.model_cls)\
            .filter(OrderApplicant.user_id == user_id,
                    OrderApplicant.source_type == source_type,
                    OrderApplicant.source_id == source_id).all()

    def gets_by_user_order_source(self, user_id, order_id):
        return self.session.query(self.model_cls)\
            .filter(OrderApplicant.source_id == order_id,
                    OrderApplicant.user_id == user_id).all()

    def delete_all_by_order_id(self, order_id):
        return self.session.query(self.model_cls).filter(self.model_cls.source_id == order_id).delete()