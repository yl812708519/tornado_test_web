#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from urllib import urlencode
from tornado.web import authenticated
from app.handlers.application import BaseHandler
from app.commons.decoraters_tornado import validators
from app.commons.validators import REQUIRED
from app.commons.view_model import ViewModel
from app.services.base_service import ServiceException
from app.services.mark_reg_forecast_service import MarkForecastService, MarkForecastBO
from app.services.mark_reg_service import MarkRegService, MarkRegOrderBO
from app.services.static_option_service import StaticOptionService


class MarkForecastHandler(BaseHandler):
    """
    商标预判
    """

    @authenticated
    def get(self):
        """

        :return:
        """
        self.render('ban_views/mark_reg/forecast_mark.html', mark=MarkForecastBO())

    @authenticated
    @validators(rules=
                {
                    'mark_name': {REQUIRED: True},
                    'mark_desc': {REQUIRED: True},
                    'mark_img': {REQUIRED: True}
                },
                messages=
                {
                    'mark_name': {REQUIRED: u'商标名称不能为空'},
                    'mark_desc': {REQUIRED: u'商标描述不能为空'},
                    'mark_img': {REQUIRED: u'商标图片不能为空'}
                })
    def post(self, *args, **kwargs):
        mark = dict(name=self.get_argument('mark_name', ''),
                    description=self.get_argument('mark_desc', ''),
                    mark_img=self.get_argument('mark_img', ''))
        mark_bo = MarkForecastBO(**mark)
        mark_bo.user_id = self.current_user.user_id
        if MarkForecastService().add_forecast(mark_bo):
            self.redirect('/user/forecast')


class UserForecastHandler(BaseHandler):
    """
        用户的预判订单
    """
    @authenticated
    def get(self, *args, **kwargs):

        user_id = self.current_user.user_id
        current_page = self.get_argument('current_page', 1)
        page_size = self.get_argument('page_size', 15)
        offset = (current_page - 1) * page_size

        count, marks = MarkForecastService().count_gets_by_user(user_id, offset=offset, count=page_size)
        result = dict(marks=ViewModel.to_views(marks),
                      count=count,
                      forecast_status=StaticOptionService.mark_forecast_status,
                      active_id='forecasts')
        self.render('ban_views/mark_reg/forecast_marks.html', **result)

    @authenticated
    def post(self, *args, **kwargs):
        """
        去申请
        :param args:
        :param kwargs:
        :return:
        """
        forecast_id = self.get_argument('forecast_id')
        user_id = self.current_user.user_id

        forecast_mark = MarkForecastService().get_for_apply(forecast_id, user_id)
        if forecast_mark:
            mark_reg_bo = MarkRegOrderBO(**{k: v for k, v in forecast_mark.attributes.items()
                                            if k in['user_id', 'name', 'description', 'mark_img']})
            # mark_reg_bo.is_info_step = True
            # mark_reg_bo.is_confirme_able -= 1
            mark_reg_service = MarkRegService()
            mark_reg_order_id = mark_reg_service.mark_forecast_add(mark_reg_bo, user_id)
            if mark_reg_order_id:
                self.redirect('/order/'+str(mark_reg_order_id))
            else:
                raise ServiceException(20070, 'error')
        else:
            raise ServiceException(20095, 'status error')

    @authenticated
    def delete(self):
        forecast_id = self.get_argument('forecast_id')
        MarkForecastService().delete(forecast_id)
        self.write({'result': 1})