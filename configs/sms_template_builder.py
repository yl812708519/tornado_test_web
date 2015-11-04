#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import yaml
from configs.settings import Settings

__author__ = 'freeway'

class SmsTemplateBuilder(object):

    _sms_templates = None

    @classmethod
    def get_template_by_name(cls, name):
        if cls._sms_templates is None:
            with file(os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'sms_templates.yaml'), 'r') as file_stream:
                cls._sms_templates = yaml.load(file_stream)
        return cls._sms_templates.get(name, None)

if __name__ == "__main__":

   print(SmsTemplateBuilder.get_template_by_name("signup"))