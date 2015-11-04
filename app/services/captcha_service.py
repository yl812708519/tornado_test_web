#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from app.commons.memcache_factory import MemCacheFactory
from app.services.base_service import BaseService

__author__ = 'freeway'


class CaptchaService(BaseService):

    # 小写字母，去除可能干扰的i，l，o，z
    _letter_cases = "abcdefghjkmnprstuvwxy"
    # 大写字母
    _upper_cases = _letter_cases.upper()
    # 数字
    _numbers = ''.join(map(str, range(3, 10)))
    _init_chars = ''.join((_letter_cases, _upper_cases, _numbers))
    _cache_session = 'captcha'

    @classmethod
    def _parse_to_key(cls, account_name):
        return "captcha:{0}".format(account_name)

    @classmethod
    def generate_captcha_by_mobile(cls, account_name):
        """生成验证码

        :param mobile: 帐号名
        :return:
        """
        return cls.generate_captcha(account_name)

    @classmethod
    def generate_captcha(cls, account_name):
        """ 生成验证吗

        :param account_name: 用户账号
        :return:
        """
        captcha = ''.join(random.sample(cls._init_chars, 4))
        cache_factory = MemCacheFactory.get_instance(cls._cache_session)
        key = cls._parse_to_key(account_name)
        cache_factory.set(key, captcha)
        return captcha

    @classmethod
    def validate_captcha_by_mobile(cls, account_name, captcha):
        """ 验证码验证

        :param account_name: 用户帐号
        :param captcha: str 需要校验的验证码
        :return:
        """
        return cls.validate_captcha(account_name, captcha)

    @classmethod
    def validate_captcha(cls, account_name, captcha):
        """ 验证码验证

        :param account_name: 用户账号
        :param captcha: 验证码
        :return:
        """
        cache_factory = MemCacheFactory.get_instance(cls._cache_session)
        key = cls._parse_to_key(account_name)
        cached_captcha = cache_factory.get(key)
        if cached_captcha is None:
            return False
        is_validate = str(captcha).upper() == str(cached_captcha).upper()
        # 一旦校验完成就将这个验证码删除掉
        cache_factory.delete(key)
        return is_validate