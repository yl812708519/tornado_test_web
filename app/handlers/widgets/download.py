#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.handlers.widgets.widget import Widget
from app.services.oss_upload_service import OssUploadService


class DownloadWidget(Widget):

    def render(self, url_suffix):
        return OssUploadService.download_site + url_suffix