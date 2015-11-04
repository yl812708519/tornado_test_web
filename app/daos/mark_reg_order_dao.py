#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'freeway'

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, SmallInteger
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class MarkRegOrder(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 订单编号
    order_id = Column(BigInteger, default=None)

    # 业务类型
    biz = Column(String(40))

    # 用户id
    user_id = Column(String(36))

    # 商标名称
    name = Column(String(255), default='')

    # 商标描述
    description = Column(String(200), default='')

    # 商标类型
    mark_type = Column(String(200), default='')
    # 商标图片
    mark_img = Column(String(200), default='')
    # 是否指定颜色
    is_specify_color = Column(Boolean, default=0)

    # 集体商标 集体成员名单
    collective_list = Column(String(200), default='')

    # 申请主体id
    applicant_id = Column(BigInteger, default='')

    # 商标类别
    category = Column(String(10), default='')

    # 商标小项树结构(使用json数据结构)
    itemtree = Column(String(2000), default='')

    # 商标小项（以,进行分割，小项最多增加到100）
    items = Column(String(1000), default='')

    # 以3维方式注册
    is_three_d = Column(Boolean, default=False)

    # 3D 五面图片
    three_d_image = Column(String(200), default='')

    # 以颜色组合注册
    is_color = Column(Boolean, default=False)

    # 颜色组合图片
    color_image = Column(String(200), default='')

    # 以声音标志注册
    is_voice = Column(Boolean, default=False)

    # 声音文件
    voice_file = Column(String(200), default='')

    # 以肖像权注册
    is_portrait = Column(Boolean, default=False)

    # 肖像图片
    portrait_img = Column(String(200), default='')

    # 共同申请人
    is_co_applicants = Column(Boolean, default=False)

    # 共同申请人id json
    co_applicant_ids = Column(String(200), default='')

    # 优先权 no:否 before:在先优先权 exhibition:展会优先权
    is_prority = Column(String(200), default='no')

    # 优先权-申请/展出国家/地区
    prority_app_region = Column(String(200), default='')

    # 优先权-申请/展出日期 (yyyy-MM-dd)
    prority_app_date = Column(String(10), default='')

    # 优先权-申请号
    prority_app_serial_num = Column(String(50), default='')

    # 商标申请号
    app_serial_num = Column(String(50), default='')

    # 上传的管理规则文件(集体商标注册 和 证明商标注册有此项)
    regulation_file = Column(String(200), default='')

    # 是否可确认订单
    is_confirm_able = Column(SmallInteger, default=4)

    # 是否付款
    is_paid = Column(Boolean, default=False)

    # 是否已确认(确认后将不可修改，可以由后台客服修改当前的状态)
    is_confirmed = Column(Boolean, default=False)

    # 是否已复查(审查通过后就可以下载资料)
    is_reviewed = Column(Boolean, default=False)

    # 是否委托顾问帮助填写(一旦委托current_step就设置为5且不可修改)
    is_delegated = Column(Boolean, default=False)
    # 顾问填写完成确认提交
    is_delegate_confirmed = Column(Boolean, default=False)


@model(MarkRegOrder)
class MarkRegOrderDao(DatabaseTemplate):

    def get_first_by_order_user(self, order_id, user_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id,
                   self.model_cls.user_id == user_id).first()

    def get_by_user_id_order_id(self, user_id, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id,
                   self.model_cls.user_id == user_id).first()

    def get_by_order(self, order_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.order_id == order_id).first()
