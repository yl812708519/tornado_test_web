#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.handlers.index import IndexHandler
from app.handlers.photo import PhotoHandler


class Routes(object):
    """url路由配置信息.
    for example::
        HANDLERS = [
            (r"/", HomeHandler),
            (r"/archive", ArchiveHandler),
            (r"/feed", FeedHandler),
            (r"/entry/([^/]+)", EntryHandler),
            (r"/compose", ComposeHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
        ]
    """

    _handlers = None

    @classmethod
    def get_handlers(cls):
        if cls._handlers is None:
            cls._handlers = \
                [
                    (r"/", IndexHandler),
                    (r"/photos", PhotoHandler),
                    (r"/photos/new", PhotoHandler),
                    (r"/photos", PhotoHandler),
                    (r"/photos/(\w)", PhotoHandler),
                    (r"/photos/(\w)/edit", PhotoHandler)
                ]
        return cls._handlers


# HTTP方法 	    路径 	         控制器#动作 	         作用
# GET 	        /photos 	     photos#index 	    显示所有图片
# GET 	        /photos/new 	 photos#new 	    显示新建图片的表单
# GET 	        /photos/:id 	 photos#show 	    显示指定的图片
# GET 	        /photos/:id/edit photos#edit 	    显示编辑图片的表单
# PATCH/PUT 	/photos/:id 	 photos#update 	    更新指定的图片
# DELETE 	    /photos/:id 	 photos#destroy 	删除指定的图片
# POST 	        /photos 	     photos#create 	    新建图片


