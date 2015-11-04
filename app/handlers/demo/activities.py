#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.application import BaseHandler
from app.services.article_service import ArticleService
from app.services.category_service import CategoryService

__author__ = 'wanglei'


class ActivitiesHandler(BaseHandler):
    def get(self, *args):
        self.render("activities/index.html")


class DetailsPageHandler(BaseHandler):
    def get(self, *args):
        self.render("activities/detailsPage.html")