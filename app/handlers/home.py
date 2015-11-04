#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.view_model import ViewModel

from app.handlers.application import BaseHandler
# from app.services.article_service import ArticleService
# from app.services.activity_service import ActivityService
# from app.services.banner_service import BannerService
# from app.services.provide_service import ProvideService
# from app.services.recommend_service import RecommendService


class HomeHandler(BaseHandler):
    def get(self, *args):
        # banner_service = BannerService()
        # banner_bos = banner_service.gets_by_count()
        # banners = ViewModel.to_views(banner_bos)
        #
        # recommend_service = RecommendService()
        # recommend_bos = recommend_service.gets_by_count(4)
        # recommends = ViewModel.to_views(recommend_bos)
        #
        # provide_service = ProvideService()
        # provide_bos = provide_service.gets_by_count()
        # provides = ViewModel.to_views(provide_bos)
        #
        # category_id = self.get_argument('category_id', 1)
        # article_service = ArticleService()
        # news_temp = article_service.gets_by_category_id_limit(category_id)
        # news = [ViewModel(**new.attributes) for new in news_temp]
        #
        # activity_service = ActivityService()
        # activities_temp = activity_service.gets_for_home(count=3)
        # activities = [ViewModel(**activity.attributes) for activity in activities_temp]
        # result = ViewModel(news=news,
        #                    activities=activities,
        #                    banners=banners,
        #                    recommends=recommends,
        #                    provides=provides,
        #                    title='国内首家O2O模式中小微企业知识产权管理运营平台')
        self.render("home/index.html", title='国内首家O2O模式中小微企业知识产权管理运营平台')


class AboutHandler(BaseHandler):
    def get(self, *args):
        self.render("home/about.html")


class AgreementHandler(BaseHandler):
    def get(self, *args):
        self.render("home/agreement.html")


class LawHandler(BaseHandler):
    def get(self, *args):
        self.render("home/law.html")


class SecretHandler(BaseHandler):
    def get(self, *args):
        self.render("home/secret.html")


class FeedbackHandler(BaseHandler):
    def get(self, *args):
        self.render("home/feedback.html")


class StaticHomeHandler(BaseHandler):

    def get(self, static_html, *args):
        """ 通用的跳转静态文章的页面

        :param args:
        """
        if static_html == 'about':
            self.render('home/' + static_html + '.html', title='关于我们')
        else:
            self.render('home/' + static_html + '.html')


class MarkServiceHandler(BaseHandler):
    def get(self, *args):
        self.render("home/mark_service.html")


class AppServiceHandler(BaseHandler):
    def get(self, *args):
        self.render("home/app_service.html")