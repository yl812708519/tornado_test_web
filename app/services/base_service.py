#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contextlib import contextmanager
from decorated.base.dict import DefaultDict
import logging
__author__ = 'freeway'


class ServiceError(Exception):
    """服务错误
    一些无法解决的一些错误被称为系统错误，
    比如数据库访问失败，数据库插入失败等."""

    def __init__(self, code, msg, *args, **kwargs):
        """初始化

        :param code: 错误码
        :param msg:
        :param args:
        :param kwargs:
        """
        self.code = code
        self.msg = msg
        super(ServiceError, self).__init__(*args, **kwargs)


class ServiceException(Exception):
    """服务异常
    主要针对于一些逻辑异常，就抛出相关的错误。
    比如当前用户不存在，名称不能为空
    """

    def __init__(self, code, msg, *args, **kwargs):
        """初始化

        :param code: 错误码
        :param args:
        :param kwargs:
        """
        self.code = code
        self.msg = msg
        super(ServiceException, self).__init__(*args, **kwargs)


class ServiceValidationFailsException(Exception):
    """服务异常
    主要针对于一些逻辑异常，就抛出相关的错误。
    比如当前用户不存在，名称不能为空
    """

    def __init__(self, validate_errors, is_raise_all=False, *args, **kwargs):
        """初始化

        :param code: 错误码
        :param args:
        :param kwargs:
        """
        if isinstance(validate_errors, DefaultDict) and is_raise_all:
            # 服务化抛错 格式不同啊。。
            validate_errors = [dict(field=k, msg=v) for k, v in validate_errors.items()]
            validate_error = validate_errors[0]
        if isinstance(validate_errors, dict):
            validate_error = validate_errors
        elif isinstance(validate_errors, list):
            validate_error = validate_errors[0]
        self.code = 1000
        self.field = validate_error.keys()[0]
        self.msg = validate_error.values()[0]
        if is_raise_all:
            # 有可能会有需要所有校验错误的情况
            self.errors = validate_errors
        super(ServiceValidationFailsException, self).__init__(*args, **kwargs)


class BaseService(object):
    @contextmanager
    def create_session(self, db):
        """Provide a transactional scope around a series of operations.
        :param db: DatabaseFactory database factory
        """
        session = db.session_cls()
        try:
            yield session
            # print 'session close'
            session.commit()
        except Exception as e:
            if isinstance(e, ServiceException):
                session.commit()
                raise e
            else:
                session.rollback()
                logging.exception(e)
                raise e  # ServiceError(10001, 'system error')
        finally:
            session.close()
