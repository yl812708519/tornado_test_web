#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.view_model import ViewModel

from app.handlers.application import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args):
        a = self.request
        self.render("home/index.html", title='哈哈哈哈')

