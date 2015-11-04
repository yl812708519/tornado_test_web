#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2011-6-20

@author: willian.huw
"""
from app.handlers.widgets.widget import Widget
from app.services.oss_upload_service import OssUploadService
from configs.settings import Settings


class UserDomainWidget(Widget):
    def render(self, user=None, domain=""):
        if len(domain) > 0:
            return domain
        if user:
            if user.get('domain'):
                return user.get('domain')
            else:
                return user.get('id')
        domain = self.handler.get_unicode_cookie('ut_domain')
        if not domain:
            return self.handler.get_unicode_cookie('ut_domain')
        else:
            return self.handler.get_secure_cookie("ut_user_id")


class UserAvatarWidget(Widget):
    def render(self, user=None, style='normal'):
        """docstring for """
        if user and user.avatar and len(user.avatar) > 0:
                return OssUploadService.download_image_site() + user.avatar
        return Settings.STATIC_SITE_ROOT + Settings.STATIC_URL_PREFIX + 'img/avatar-default.gif'


class UserAboutWidget(Widget):
    def render(self, username, bio):
        return self.render_string('widgets/userabout.html', username=username, bio=bio)
