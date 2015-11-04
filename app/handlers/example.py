#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import authenticated

from app.handlers.application import BaseHandler


class ExampleHandler(BaseHandler):
    @authenticated
    def get(self, *args):
        self.render("example/index.html")
