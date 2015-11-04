#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.application import BaseHandler
from app.services.article_service import ArticleService
from app.services.category_service import CategoryService

__author__ = 'wanglei'


class RegistrationHandler(BaseHandler):
    def get(self, *args):
        self.render("seminar/registration.html")


class Project_applicationHandler(BaseHandler):
    def get(self, *args):
        self.render("seminar/project_application.html")


class PatentHandler(BaseHandler):
    def get(self, *args):
        self.render("seminar/patent.html")


class TrademarkHandler(BaseHandler):
    def get(self, *args):
        self.render("seminar/trademark.html")