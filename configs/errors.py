#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import yaml
from configs.settings import Settings

__author__ = 'freeway'


class Errors(object):

    _errors = None

    @classmethod
    def error_message(cls, code, *args, **kwargs):
        if cls._errors is None:
            with file(os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'errors.yaml'), 'r') as file_stream:
                cls._errors = yaml.load(file_stream)
        msg = cls._errors.get(code)
        if len(args) > 0:
            return msg.format(*args)
        elif len(kwargs) > 0:
            return msg.format(**kwargs)
        else:
            return msg