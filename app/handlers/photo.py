#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.commons.view_model import ViewModel

from app.handlers.application import BaseHandler


class PhotoHandler(BaseHandler):

    def get(self, *args, **kwargs):
        a = self.request.path
        self.write(a)

    def index(self):
        self.write('列表展示')

    def show(self, *args):
        self.write('这个是展示啊啊啊啊')

    def new(self, *args):
        self.write('创建的页面加载')

    def create(self, *args):
        self.write('创建了数据啊')

    def edit(self, *args):
        self.write('编辑页面get')

    def update(self, *args):
        self.write('编辑post')

    def destroy(self, *args):
        self.write('删除post')

    def _execute(self, transforms, *args, **kwargs):
        post_url_map = dict(post='create', patch='update', put='update', delete='destory')

        if self.request.method.upper() == 'POST':
            self.request.method = self.get_argument('_method', 'POST').upper()
        super(PhotoHandler, self)._execute(self, transforms, *args, **kwargs)
        # RequestHandler._execute(self, transforms, *args, **kwargs)