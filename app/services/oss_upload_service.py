#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import tempfile
from PIL import Image

from app.commons.fileutil import get_write_file_name
from app.commons.oss_factory import OssFactory


class OssUploadService(object):
    """文件上传服务
    """

    run_mode = 'development'
    _download_site = None

    _image_upload_url_prefix = 'images/'
    """图片文件上传前缀. """
    _files_upload_url_prefix = 'files/'
    """非图片的文件上传前缀. """

    def download_site(self, name='yestar'):
        return OssFactory.download_site(name, self.run_mode)

    def download_image_site(self, name='yestar'):
        return OssFactory.download_image_site(name, self.run_mode)

    def __init__(self, oss_name='yestar'):
        self._oss_factory = OssFactory.get_instance(oss_name, self.run_mode)

    def upload_image(self, file_meta, content_type=None):
        """上传图片

        :param file_meta:获取的文件
        :return:上传状态
        """

        # 上传的文件名
        file_name = file_meta['filename']
        # 获取文件的扩展名
        file_extension = os.path.splitext(file_name)[1]
        file_data = file_meta['body']
        # 有文件，判断是否为我们需要的格式
        # 常用的图片格式有：image/jpeg，image/bmp，image/pjpeg，image/gif，image/x-png，image/png
        image_type_list = ['image/gif', 'image/jpeg', 'image/pjpeg', 'image/bmp', 'image/png', 'image/x-png']

        if file_meta['content_type'] not in image_type_list:
            return False, '仅支持jpg,jpeg,bmp,gif,png格式的图片！'
        # 限制上传文件的大小，通过len获取字节数
        if len(file_data) > 4 * 1024 * 1024:
            return False, '请上传4M以下的图片'
        # 创建临时文件，当文件关闭时自动删除
        tmp_file = tempfile.NamedTemporaryFile(delete=True)
        tmp_file.write(file_meta['body'])
        tmp_file.seek(0)
        # 名虽然是图片格式，但内容并非是图片。
        try:
            Image.open(tmp_file.name)
        except IOError, error:
            logging.info(error)   # 进行日志记录，因为这些操作大多数是破坏者的做法。
            tmp_file.close()
            return False, '图片不合法！'
        tmp_file.close()
        #   构造上传文件的路径
        file_path = get_write_file_name(len(file_data), file_extension[1:])
        upload_path = os.path.join(self._image_upload_url_prefix, file_path)
        return self._oss_factory.upload_file(file_data, upload_path, content_type)

    def upload_file(self, file_meta, real_file_name=None):
        """上传文件

        :param file_meta:获取的文件
        :return:
        """
        #判断文件大小
        if len(file_meta['body']) > 10 * 1024 * 1024:
            return False, '请上传10M以下的文件'
        if not real_file_name:
            #上传的文件名 自动生成的字符串
            file_name = file_meta['filename']
            #获取文件的扩展名
            file_extension = os.path.splitext(file_name)[1]
            file_data = file_meta['body']
            #构造上传文件的路径
            file_path = get_write_file_name(len(file_data), file_extension[1:])
            upload_path = os.path.join(self._files_upload_url_prefix, file_path)
            return self._oss_factory.upload_file(file_data, upload_path)
        else:
            #使用真实文件名进行上传
            file_name = file_meta['filename']
            file_data = file_meta['body']
            file_path = get_write_file_name(len(file_data))
            real_file_name = file_path+"/"+file_name
            upload_path = os.path.join(self._files_upload_url_prefix, real_file_name)
            return self._oss_factory.upload_file(file_data, upload_path)

    def delete_image(self, delete_path):
        """

        :param delete_path: 被删除文件路径
        """
        self._oss_factory.delete_file(delete_path)

    def delete_file(self, delete_path):
        """

        :param delete_path: 被删除文件路径
        """
        delete_path = os.path.join(delete_path)
        self._oss_factory.delete_file(delete_path)