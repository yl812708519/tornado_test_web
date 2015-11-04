#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created_at: 2015-02-11 17:41:54
# created_by: generate script
from app.commons.biz_model import BizModel, Attribute
from app.commons.validator import Validators, Required, MaxLength


class ApplicantBO(BizModel):
    id = Attribute(None)
    user_id = Attribute('')  # 用户id
    name = Attribute('')  # 名称
    app_type = Attribute('')  # 主体类型：person:个人 com:公司
    region = Attribute('')  # 区域：cn（中国大陆）、hk（中国香港）、tw（中国台湾）、mo（中国澳门）、other（其他国籍）
    nationality_name = Attribute('')  # 国籍名称（只有在region选择other的时候出现）
    company_name = Attribute('')  # 公司名称/个体工商户名称
    company_en_name = Attribute('')  # 公司英文名称（只有在region非cn的时候出现）
    certificate_num = Attribute('')  # cn:营业执照号 tw:登记证编号 hk/mo/other:注册证书编号
    register_address = Attribute('')  # 注册地址/个体工商户执照地址
    register_en_address = Attribute('')  # 注册英文地址（只有在region非cn的时候出现）
    certificate_img1 = Attribute('')  # 证书/个体工商户执照 图1
    certificate_img2 = Attribute('')  # 证书 图2 （只有在region非cn的时候出现）
    certificate_img3 = Attribute('')  # 证书 图3 （只有在region非cn的时候出现）
    certificate_img4 = Attribute('')  # 证书 图4 （只有在region非cn的时候出现）
    person_name = Attribute('')  # 真实姓名
    person_en_name = Attribute('')  # 真实英文名
    passport_num = Attribute('')  # 护照号 (非cn出现)
    id_card_num = Attribute('')  # 身份证号 (cn出现)
    person_address = Attribute('')  # cn:身份证地址 非cn:中文地址
    person_en_address = Attribute('')  # 英文地址(非cn出现)
    passport_img = Attribute('')  # 护照图片
    id_card_front_img = Attribute('')  # 身份证正面照片
    id_card_back_img = Attribute('')  # 身份证背面照片
    created_at = Attribute('')
    temp_region = Attribute('')
    temp_app_type = Attribute('')


class ApplicantRepBO(BizModel):

    id = Attribute(None)
    user_id = Attribute('')  # 用户id
    name = Attribute('')  # 名称
    app_type = Attribute('')  # 主体类型：person:个人 com:公司
    region = Attribute('')  # 区域：cn（中国大陆）、hk（中国香港）、tw（中国台湾）、mo（中国澳门）、other（其他国籍）
    nationality_name = Attribute('')  # 国籍名称（只有在region选择other的时候出现）
    company_name = Attribute('')  # 公司名称/个体工商户名称
    company_en_name = Attribute('')  # 公司英文名称（只有在region非cn的时候出现）
    certificate_num = Attribute('')  # cn:营业执照号 tw:登记证编号 hk/mo/other:注册证书编号
    register_address = Attribute('')  # 注册地址/个体工商户执照地址
    register_en_address = Attribute('')  # 注册英文地址（只有在region非cn的时候出现）
    certificate_img1 = Attribute('')  # 证书/个体工商户执照 图1
    certificate_img2 = Attribute('')  # 证书 图2 （只有在region非cn的时候出现）
    certificate_img3 = Attribute('')  # 证书 图3 （只有在region非cn的时候出现）
    certificate_img4 = Attribute('')  # 证书 图4 （只有在region非cn的时候出现）
    person_name = Attribute('')  # 真实姓名
    person_en_name = Attribute('')  # 真实英文名
    passport_num = Attribute('')  # 护照号 (非cn出现)
    id_card_num = Attribute('')  # 身份证号 (cn出现)
    person_address = Attribute('')  # cn:身份证地址 非cn:中文地址
    person_en_address = Attribute('')  # 英文地址(非cn出现)
    passport_img = Attribute('')  # 护照图片
    id_card_front_img = Attribute('')  # 身份证正面照片
    id_card_back_img = Attribute('')  # 身份证背面照片
    created_at = Attribute('')
    temp_region = Attribute('')
    temp_app_type = Attribute('')


class ApplicantCommon(BizModel):

    id = Attribute(None)
    user_id = Attribute('')  # 用户id
    name = Attribute('')  # 名称
    region = Attribute('')
    app_type = Attribute('')

class ApplicantCnPerson(ApplicantCommon):
    person_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='真实姓名'))
    id_card_num = Attribute(default='',  validators=Validators([Required()], name='身份证号'))  # 身份证号 (cn出现)
    person_address = Attribute(default='',  validators=Validators([Required()], name='身份证地址'))  # cn:身份证地址 非cn:中文地址
    company_name = Attribute(default='',  validators=Validators([Required()], name='公司名称/个体工商户名称'))
    register_address = Attribute(default='',  validators=Validators([Required()], name='注册地址/个体工商户执照地址'))
    certificate_img1 = Attribute(default='',  validators=Validators([Required()], name='证书/个体工商户执照'))
    id_card_front_img = Attribute(default='',  validators=Validators([Required()], name='身份证正面照片'))
    id_card_back_img = Attribute(default='',  validators=Validators([Required()], name='身份证背面照片'))


class ApplicantHtmPerson(ApplicantCommon):
    person_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='税务登记证号'))
    person_en_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    passport_num = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    person_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    person_en_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    company_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    register_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    certificate_img1 = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    passport_img = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))


class ApplicantOtherPerson(ApplicantCommon):
    nationality_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    person_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='税务登记证号'))
    person_en_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    passport_num = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    person_en_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    passport_img = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))


class ApplicantCnCom(ApplicantCommon):

    company_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='税务登记证号'))
    register_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    certificate_img1 = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))


class ApplicantHtmCom(ApplicantCommon):

    company_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='税务登记证号'))
    certificate_num = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    register_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    register_en_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    certificate_img2 = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))


class ApplicantOtherCom(ApplicantCommon):

    nationality_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    company_name = Attribute(default='',  validators=Validators([Required(), MaxLength(100)], name='税务登记证号'))
    company_en_name = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    certificate_num = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    register_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    register_en_address = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))
    certificate_img2 = Attribute(default='',  validators=Validators([Required()], name='税务登记证号'))



