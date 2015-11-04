#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from sqlalchemy import Column, String, Integer, BigInteger, Boolean
from app.commons.database import BaseModel, model, DatabaseTemplate
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin, IsDeletedMixin

__author__ = 'freeway'


class SmsCode(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 手机号格式(国家号)-(手机号)
    mobile = Column(String(30))

    # 校验类型
    valid_type = Column(String(30))

    # 手机验证码
    verification_code = Column(String(10))

    # 验证token
    verification_token = Column(String(36))

    # 允许的最大尝试校验的次数
    max_retry_count = Column(Integer, default=None)

    # 连续验证失败的次数
    continuous_failed_count = Column(Integer, default=None)

    # 校验验证码的总次数
    valid_count = Column(BigInteger, default=None)

    # 校验失败的总次数
    valid_failed_count = Column(BigInteger, default=None)

    # 发送验证码的总次数
    sent_count = Column(BigInteger, default=0)

    # 客户端的ip地址
    remote_ip_address = Column(String(50))

    # 最后一次发送验证码的时间
    last_sent_at = Column(BigInteger, default=None)

    # 已经校验通过，表示这个验证码已经不能再使用了，必须再重新生成新的验证码
    is_validated = Column(Boolean, default=False)

    # 过期时间，一旦过期就需要重新生成验证码
    expires_in = Column(BigInteger, default=None)

    # 在指定的时间点解锁
    unlock_in = Column(BigInteger, default=None)

    # 乐观锁版本号
    version_id = Column(String(36))

    __mapper_args__ = {
        'version_id_col': version_id,
        'version_id_generator': lambda version: uuid.uuid4()
    }


@model(SmsCode)
class SmsCodeDao(DatabaseTemplate):
    """SmsCode的数据访问对象
    """

    def get_by_mobile_valid_type_remote_ip_address(self, mobile, valid_type, remote_ip_address):
        """通过手机号，验证类型、验证token、ip获取信息

        :param mobile:
        :param valid_type:
        :param remote_ip_address:
        :return:
        """
        return self.get_first_by_criterion(SmsCode.mobile == mobile,
                                           SmsCode.remote_ip_address == remote_ip_address,
                                           SmsCode.valid_type == valid_type)

    def get_by_mobile_valid_type(self, mobile, valid_type):
        """
        查询某手机号是否已经验证通过(是否已注册)
        :param mobile:
        :return:
        """
        return self.session.query(self.model_cls).\
            filter(SmsCode.mobile == mobile,
                   SmsCode.valid_type == valid_type).first()