#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.view_model import ViewModel

from app.handlers.application import RestfulAPIHandler
# from app.services.article_service import ArticleService
# from app.services.activity_service import ActivityService
from app.services.options_service import OptionsService


class OptionJsonHandler(RestfulAPIHandler):
    def get(self):
        opt_value = self.get_argument("opt_value", None)
        opt_type = self.get_argument("sub_type", None)
        option_service = OptionsService()
        options = option_service.gets_by_type(opt_type)
        options_vm = ViewModel.to_views(options)
        self.write(options_vm)