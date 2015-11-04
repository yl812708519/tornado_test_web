#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import urllib

from tornado.web import authenticated
from app.commons.view_model import ViewModel

from app.handlers.application import RestfulAPIHandler
from app.services.oss_upload_service import OssUploadService


class AttachmentUpload(RestfulAPIHandler):
    """
    ajax上传文件
    """
    def post(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        """
        oss_name = self.get_argument("ossName", 'yestar')
        file_metas = self.request.files.get('file')
        download_urls = []
        error_msgs = []
        status = []
        if not file_metas:
            result = dict(error_msg="请选择要上传的文件",
                          status=0
                          )
            self.write(result)
            return
        upload_file_service = OssUploadService(oss_name)
        for file_meta in file_metas:
            check_status, upload_message = upload_file_service.upload_file(file_meta, True)

            if check_status:
                # 下载连接
                download_url = upload_file_service.download_site(oss_name) + urllib.quote(str(upload_message))
                download_urls.append(download_url)
                status.append(1)
            else:
                error_msgs.append(upload_message)
                status.append(0)
        result = ViewModel(download_urls=download_urls,
                           error_msgs=error_msgs,
                           status=status)
        self.write(result)
