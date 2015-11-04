#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created_at: 2015-02-11 17:43:13
# created_by: generate script
from tornado.web import authenticated

from app.services.ban_bos.applicant import ApplicantCnPerson, ApplicantHtmPerson, \
    ApplicantOtherPerson, ApplicantCnCom, ApplicantHtmCom, ApplicantOtherCom

__author__ = 'zhaowenlei'

from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.services.applicant_service import ApplicantService, ApplicantBO
from app.commons.view_model import ViewModel


class ApplicantNewHandler(BaseHandler):

    @authenticated
    def get(self, applicant_id=None, *args, **kwargs):
        """获取主体添加页面

        :param args:
        :param kwargs:
        :param applicant_id:主体id
        """
        if applicant_id is None:
            applicant_bo = ApplicantBO()
        else:
            user = self.current_user
            applicant_service = ApplicantService()
            applicant_bo = applicant_service.get_by_id(user.user_id, applicant_id)
        referer = self.request.headers.get('Referer')
        result = dict(applicant=applicant_bo,
                      next_url=referer)
        self.render("ban_views/applicant/applicant_new.html", **result)


class ApplicantSubmitHandler(RestfulAPIHandler):

    def get_bo(self, region, app_type):
        if region == 'cn' and app_type == 'person':
            req_bo = self.get_req_bo(ApplicantCnPerson, need_validate=False)
        elif (region == 'hk' or region == 'tw' or
                region == 'mo') and app_type == 'person':
            req_bo = self.get_req_bo(ApplicantHtmPerson, need_validate=False)
        elif region == 'other' and app_type == 'person':
            req_bo = self.get_req_bo(ApplicantOtherPerson, need_validate=False)
        elif region == 'cn' and app_type == 'com':
            req_bo = self.get_req_bo(ApplicantCnCom, need_validate=False)
        elif (region == 'hk' or region == 'tw' or
                region == 'mo') and app_type == 'com':
            req_bo = self.get_req_bo(ApplicantHtmCom, need_validate=False)
        elif region == 'other' and app_type == 'com':
            req_bo = self.get_req_bo(ApplicantOtherCom, need_validate=False)

        if req_bo.app_type == 'person':
            req_bo.name = req_bo.person_name
        else:
            req_bo.name = req_bo.company_name
        self.validate(req_bo, is_raise_all=True)
        return req_bo

    @authenticated
    def post(self, *args, **kwargs):
        region = self.get_argument('region', '')
        app_type = self.get_argument('app_type', '')
        req_bo = self.get_bo(region, app_type)
        user_id = self.current_user.user_id
        req_bo.user_id = user_id
        applicant_service = ApplicantService()
        applicant_service.add(req_bo)

    @authenticated
    def put(self, *args, **kwargs):
        region = self.get_argument('region', '')
        app_type = self.get_argument('app_type', '')
        req_bo = self.get_bo(region, app_type)
        user_id = self.current_user.user_id
        req_bo.user_id = user_id
        applicant_service = ApplicantService()
        applicant_service.update(req_bo)


class ApplicantHandler(BaseHandler):

    @authenticated
    def get(self, applicant_id=None):
        """获取主体详情

        :param applicant_id: 主体id
        """
        user_id = self.current_user.user_id
        applicant_service = ApplicantService()
        applicant_bo = applicant_service.get_by_id(user_id, applicant_id)
        applicant_bo.temp_region = applicant_service.get_value_by_type('region', applicant_bo.region)
        applicant_bo.temp_app_type = applicant_service.get_value_by_type('app_type', applicant_bo.app_type)
        applicant = ViewModel.to_view(applicant_bo)
        result = ViewModel(applicant=applicant)
        self.render('ban_views/applicant/applicant.html', **result)


class ApplicantsHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        """获取主体列表

        :param args:
        :param kwargs:
        """
        user_id = self.current_user.user_id
        applicant_service = ApplicantService()
        current_page = int(self.get_argument('currentPage', 1))
        page_size = self.get_argument('page_size', 10)
        offset = (int(current_page) - 1) * page_size

        app_dict = applicant_service.count_gets_by_user_id(user_id, offset, page_size)
        applicants = ViewModel.to_views(app_dict['applicant_bos'])
        result = ViewModel(applicants=applicants,
                           current_page=current_page,
                           total_page=int((app_dict['total']+page_size-1)/page_size))
        self.render('ban_views/applicant/applicants.html', **result)

    def delete(self, *args, **kwargs):
        """删除主体

        :param args:
        :param kwargs:
        """
        pass

