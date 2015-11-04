#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from app.commons import dateutil
from tornado.web import HTTPError
from app.services.base_service import BaseService, ServiceException
from app.commons.biz_model import BizModel, Attribute
from configs.database_builder import DatabaseBuilder
from app.daos.mark_forecast_dao import MarkForecast, MarkForecastDao


class MarkForecastBO(BizModel):
    id = Attribute()
    # 用户id
    user_id = Attribute('')
    # 商标名称
    name = Attribute('')
    # 商标描述
    description = Attribute('')
    # 商标图片
    mark_img = Attribute('')
    # 状态(may_apply:可申请; review:审核中; non_apply:不可申请; applied:已申请)
    status = Attribute('review')
    # 驳回理由
    reject_reason = Attribute('')
    # 反馈图片
    feedback_imgs = Attribute('')
    # 是否删除
    is_deleted = Attribute(0)
    created_at = Attribute('')
    updated_at = Attribute('')


class MarkForecastService(BaseService):
    """
    处理商标注册预判的相关逻辑
    """

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    # def _get_by_id_user(self, forecast_id, user_id, session):
    #     mark_reg_dao = MarkForecastDao(session)
    #     mark = mark_reg_dao.get_by_id_user(forecast_id, user_id)
    #     return mark

    def get_for_apply(self, forecast_id, user_id):
        with self.create_session(self._default_db) as session:
            mark_reg_dao = MarkForecastDao(session)
            mark = mark_reg_dao.get_by_id_user(forecast_id, user_id)
            if mark and mark.status == 'apply_able':
                mark.status = 'applied'
                return MarkForecastBO(**mark.fields) if mark is not None else None

    def add_forecast(self, mark_bo):
        """
        添加商标注册预判信息
        :param mark_bo:
        :return:
        """
        with self.create_session(self._default_db) as session:
            mark_reg = MarkForecast()
            mark_reg.update(mark_bo.attributes)
            mark_reg_dao = MarkForecastDao(session)
            mark_reg = mark_reg_dao.add(mark_reg)
            return mark_reg.id

    def count_gets_by_user(self, user_id, offset=0, count=15):
        """
        列表
        :param user_id:
        :return:
        """
        with self.create_session(self._default_db) as session:
            mark_forecast_dao = MarkForecastDao(session)
            forecast_marks = mark_forecast_dao.gets_by_user(user_id, offset, count)
            count = mark_forecast_dao.count_by_user(user_id)
            forecast_mark_bos = [self._deal_forecast(mark) for mark in forecast_marks]
            return count, forecast_mark_bos

    @staticmethod
    def _deal_forecast(mark):
        mark_bo = MarkForecastBO(**mark.fields)
        mark_bo.created_at = dateutil.timestamp_to_string(mark_bo.created_at)
        mark_bo.description = mark_bo.description[0:50]
        mark_bo.feedback_imgs = mark.feedback_imgs.split(',') if mark.feedback_imgs else []
        if '' in mark_bo.feedback_imgs:
            mark_bo.feedback_imgs.remove('')
        return mark_bo

    def delete(self, forecast_id):
        with self.create_session(self._default_db) as session:
            mark_forecast_dao = MarkForecastDao(session)
            mark_forecast_dao.delete_by_id(forecast_id)
