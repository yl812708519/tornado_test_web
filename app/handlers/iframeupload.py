#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from app.handlers.application import RestfulAPIHandler, BaseHandler
from app.services.oss_upload_service import OssUploadService


class IFrameUploadHandler(BaseHandler):
    def post(self, *args):

        """配合w-ajax-upload.js插件实现图片/文件ajax上传

        :param args:
        """
        # 点击按钮的id，用来调用父级的插件方法。
        ele_id = self.get_argument("eleId")
        oss_name = self.get_argument("ossName")  # oss服务器名称，yaml中的配置
        file_metas = self.request.files.get('fileData')
        file_first = file_metas[0]
        file_name = file_first['filename']
        file_size = len(file_first['body'])
        result = dict()

        content_type = file_first['content_type']
        if str(content_type).startswith("image"):
            image_type_list = ['image/jpeg', 'image/pjpeg', 'image/bmp', 'image/png', 'image/x-png']
            if content_type in image_type_list:
                # 图片
                upload_file_service = OssUploadService(oss_name)
                check_status, upload_message = upload_file_service.upload_image(file_first, content_type)
                if check_status:
                    # oss上路径
                    oss_url = upload_message
                    # 下载连接
                    download_url = upload_file_service.download_image_site() + oss_url
                    result["status"] = 1
                    result["message"] = "图片上传成功!"
                    result["ossUrl"] = oss_url
                    result["downloadUrl"] = download_url
                    result["fileName"] = file_name
                    result["fileSize"] = file_size
                else:
                    result["status"] = 0
                    result["message"] = "图片上传失败!"
            else:
                result["status"] = 0
                result["message"] = "图片格式错误!只支持jpeg,bmp,png格式的图片"
        else:
            # 文件
            upload_file_service = OssUploadService(oss_name)
            check_status, upload_message = upload_file_service.upload_file(file_first, True)
            if check_status:
                # oss上路径
                oss_url = upload_message
                # 下载连接
                download_url = upload_file_service.download_site(oss_name) + oss_url
                result["status"] = 1
                result["message"] = "文件上传成功!"
                result["ossUrl"] = oss_url
                result["downloadUrl"] = download_url
                result["fileName"] = file_name
                result["fileSize"] = file_size
            else:
                result["status"] = 0
                result["message"] = upload_message or "文件上传失败!"
        self.write('<script>parent.$("#' + ele_id + '").wIFrameUpload("success",'+json.dumps(result)+');</script>')

