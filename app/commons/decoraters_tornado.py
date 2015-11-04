#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import functools
from app.commons.validators import Validators
from app.commons.view_model import ViewModel

from app.services.base_service import ServiceValidationFailsException
__author__ = 'freeway'


def validators(rules=None, messages=None, raise_except=False):
    """validators decorater
    just for tornado
    会给self.对象加入
    :param rules: 校验规则
    :param messages: 出错信息
    :param raise_except: 为True时将会直接将错误抛出，不需要在 被校验函数中做判断了
    """
    def _validators(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if rules is None or len(rules) == 0:
                return method(self, *args, **kwargs)
            validate = Validators()
            # 设置验证规则
            validate.rules = copy.deepcopy(rules)
            # 设置验证失败的文案
            if messages is not None:
                validate.messages = messages
            valid_data = ViewModel()
            for field_name, validator in validate.rules.iteritems():
                # 将用与判断的 字段的值取出
                if 'condition' in validator:
                    condition_value = self.get_argument(validator['condition'][0])
                    # 判断前提是否和rules中的相等, TRUE 的会被校验
                    if type(validator['condition'][1]) in (list, tuple):
                        if str(condition_value) in validator['condition'][1]:
                            validator['condition'] = True
                        else:
                            validator['condition'] = False
                    else:
                        # 这里有可能会绕过校验，需要后端开发取页面数据时对校验的值做个判断
                        validator['condition'] = str(condition_value) == str(validator['condition'][1])
                valid_data[field_name] = self.get_argument(field_name, '')
                for validate_type, validate_value in validator.iteritems():
                    if isinstance(validate_value, str) or isinstance(validate_value, unicode):
                        if '#' == validate_value[:1]:
                            validator[validate_type] = self.get_argument(validate_value[1:], '')
            self.validation_success = validate.validates(valid_data)
            self.validation_errors = validate.errors
            self.validation_data = valid_data
            if len(self.validation_errors) > 0 and raise_except:
                raise ServiceValidationFailsException(self.validation_errors)
            return method(self, *args, **kwargs)
        return wrapper
    return _validators
