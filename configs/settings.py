#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2011-6-13

@author: freeway
"""
import os.path
from tornado.options import options
import yaml


class Settings(object):
    """设置类，用于定义一些系统的常量.
    """

    WEBSITE = None
    """网站网址."""
    SITE_ROOT = None
    """网站的根路径."""
    STATIC_SITE_ROOT = None
    """静态网站的根路径."""
    SITE_NAME = None
    """网站名称"""
    SITE_ROOT_PATH = os.path.dirname(__file__)[0:-8]
    """网站的物理根路径."""
    TEMPLATE_PATH = os.path.join(SITE_ROOT_PATH, u"app/views")
    """模板路径."""
    STATIC_PATH = os.path.join(SITE_ROOT_PATH, u"public")
    """静态文件路径. """
    STATIC_URL_PREFIX = "/s/"
    """静态文件前缀. """
    LOGIN_URL = u"/session/new"
    """登录URL. """

    @staticmethod
    def settings():
        """执行设置，静态方法.
        ::
            return dict(
                site_name=Settings.SITE_NAME,
                site_root=Settings.SITE_ROOT,
                static_site_root=Settings.STATIC_SITE_ROOT,
                website=Settings.WEBSITE,
                site_root_path=Settings.SITE_ROOT_PATH,
                template_path=Settings.TEMPLATE_PATH,
                public_path=Settings.PUBLIC_PATH,
                login_url=Settings.LOGIN_URL,
                debug=True,
                xsrf_cookies=True,
                cookie_secret="11oETzKXQAGKhnsnd23NCkjd972342kMKJhd2u352d7koinp2XdTP1oVo="
            )

        :return: dict类型的配置信息.

        """
        file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'settings.yaml'), 'r')
        yml = yaml.load(file_stream)
        yml_settings = yml.get(options.runmod)
        Settings.WEBSITE = yml_settings['wetsite']
        Settings.SITE_NAME = yml_settings['sitename']
        Settings.STATIC_URL_PREFIX = yml_settings['static_url_prefix']
        Settings.SITE_ROOT = u'http://' + Settings.WEBSITE
        Settings.STATIC_SITE_ROOT = u'http://' + Settings.WEBSITE
        cookie_secret = yml_settings['cookie_secret']
        xsrf_cookies = yml_settings['xsrf_cookies']

        port = options.port
        if port != 80 and options.runmod == 'development':
            Settings.SITE_ROOT += ':' + str(port)
            Settings.STATIC_SITE_ROOT += ':' + str(port)

        from app.handlers.application import ErrorHandler

        setting_dict = dict(site_name=Settings.SITE_NAME,
                            site_root=Settings.SITE_ROOT,
                            static_site_root=Settings.STATIC_SITE_ROOT,
                            website=Settings.WEBSITE,
                            site_root_path=Settings.SITE_ROOT_PATH,
                            template_path=Settings.TEMPLATE_PATH,
                            static_path=Settings.STATIC_PATH,
                            static_url_prefix=Settings.STATIC_URL_PREFIX,
                            login_url=Settings.LOGIN_URL,
                            xsrf_cookies=xsrf_cookies,
                            cookie_secret=cookie_secret,
                            default_handler_class=ErrorHandler,
                            default_handler_args=dict(status_code=404))
        if options.runmod == 'production':
            return setting_dict
        elif options.runmod == 'test':
            setting_dict['debug'] = True
            return setting_dict
        else:
            setting_dict['debug'] = True
            return setting_dict

if __name__ == "__main__":
    print(os.path.dirname(__file__)[0:-8])
