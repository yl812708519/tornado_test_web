#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, desc
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class MarkForecast(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(32), default='')

    # 商标名称
    name = Column(String(100), default='')

    # 商标描述
    description = Column(String(200), default='')

    # 商标图片
    mark_img = Column(String(200), default='')

    # 状态(apply_able:可申请; review:审核中; non_apply:不可申请)
    status = Column(String(45), default='')

    # 反馈图片
    feedback_imgs = Column(String(255), default='')

    # 驳回理由
    reject_reason = Column(String(255), default='')

    # 是否删除
    is_deleted = Column(Boolean, default=False)


@model(MarkForecast)
class MarkForecastDao(DatabaseTemplate):
    """
    商标注册预判。信息表
    """
    def get_by_id_user(self, forecast_id, user_id):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.user_id == user_id,
                   self.model_cls.id == forecast_id).first()

    def gets_by_user(self, user_id, offset, count):
        return self.session.query(self.model_cls).\
            filter(self.model_cls.user_id == user_id,
                   self.model_cls.is_deleted == 0).order_by(desc(self.model_cls.created_at))\
            .offset(offset).limit(count).all()

    def count_by_user(self, user_id):
        return self.count(MarkForecast.user_id == user_id)