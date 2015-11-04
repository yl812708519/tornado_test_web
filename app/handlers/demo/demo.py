#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.web import authenticated
from app.handlers.application import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args):
        self.render("home/index.html")


class ApplicantBuysHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/patent_applicant_buys.html")



class ApplicantSalesHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/patent_applicant_sales.html")


class TrademarkBuyHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/trademark_applicant_buy.html")


class TrademarkBuysHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/trademark_applicant_buys.html")


class TrademarkSaleHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/trademark_applicant_sale.html")


class TrademarkSalesHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/trademark_applicant_sales.html")


class SettingsHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/personalSet.html")

class ChangePwdHandler(BaseHandler):
    def get(self, *args):
        self.render("demo/change_word.html")

class DemoHandler(BaseHandler):
    def post(self, *args):
        demo_input = self.get_argument("demo_input", None)
        demo_inputs = self.get_arguments("demo_input", None)
        user = self.get_form("user")
        print user
        print demo_inputs
        type = self.get_argument("type", None)
        if type == "1":
            pass
        elif type is not"2":
            pass
        elif not type:
            pass
        elif type != 3:
            pass
        elif type is "4":
            pass
        else:
            pass

        if demo_input:  # 0 None "" [] {} is False
            demo_input += "取到了"
        else:
            demo_input = "没取到"

        data_list = list()
        data_list.append("1")
        data_list.append(1)
        data_list.append("hao")

        user = dict()
        user["name"] = "张山"
        user["age"] = 22
        user["job"] = "web前端"
        user["like"] = ["篮球", "唱歌", "跑步"]
        print demo_input

        result = dict()
        result["ok"] = "成功了！！！！"  #
        result["error"] = "失败了！！！"
        result["data_list"] = data_list
        result["user"] = user
        self.render("demo/demo_result.html", **result)

    def get(self, *args):
        self.render("demo/demo.html")






