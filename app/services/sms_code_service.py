#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2014-11-07

@author: huwei
"""
import datetime
import logging
import requests
import json
from app.commons import dateutil
from app.commons.biz_model import BizModel, Attribute
from app.services.base_service import ServiceException
from app.commons.stringutil import random_number, gen_id, uuid4
from app.daos.sms_code_dao import SmsCodeDao, SmsCode
from app.services.base_service import BaseService
from configs.database_builder import DatabaseBuilder
from configs.settings import Settings
from configs.sms_template_builder import SmsTemplateBuilder

__author__ = 'freeway'


class SmsSendStatus(object):
    SUCCESS = 1
    NOT_EXIST = 2
    TOO_OFTEN = 3


class SmsValidType(object):
    SIGNUP = 'signup'
    RESET_PASSWORD = 'reset_password'
    ACCOUNT_CHANGE = 'account_change'


class SmsValidateResult(BizModel):
    status = Attribute(None)
    token = Attribute(None)


class SmsCodeService(BaseService):
    """ 短信验证码服务
    每次获取verification_code就给这个验证码生成一个verification_token，verification_token发送到前端界面，verification_code发送到用户的手机，
    用户通过提交verification_token和verification_code到服务端进行校验。
    实现逻辑：
    1、避免用户频繁提交获取验证码，控制用户提交时间，每60秒才允许提交一次
    2、每个用户账号+valid_type+ip 构成一个唯一sms_code对象
    3、每验证错误一次failed_count+1，如果连续验证错误10次，则将这个用户账号+valid_type+ip的sms_code的记录封禁1小时，既将locked_at设置为 当前时间+1小时
    4、locked_at>当前时间提示前端，错误次数超出限制，隔一段时间登录
    5、当is_validated为True的时候表示上次验证通过，表明这个用户还没有获取verification_code就开始验证了，提示用户重新获取验证码
    6、expired_at<当前时间表示验证码已过期，提示用户重新获取
    7、每发送一次verification_code就sent_count+1
    8、retry_count可以删除掉了
    9、每验证一次valid_count+1，纯粹做统计用，表明这个ip用这个账号验证过多少次
    10、
    """

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        # key 来自 www.luosimao.com 管理中心 ， 触发发送。
        # 修改时保留  key- 只修改之后的部分
        self.sms_api_key = 'key-e7251111be4438658ffedaa5ce4d5e64'

    def _send_sms_template_message(self, mobile, template_name, *args):
        template = SmsTemplateBuilder.get_template_by_name(template_name)
        # message = '{0}(验证码){1}客服绝不会索取此验证码，请勿将此验证码告知他人【{1}】'.format(*args)
        s = (u'冰狗网',)
        args = args + s

        message = template.format(*args)
        mobile_parts = mobile.split("-")
        if len(mobile_parts) == 2:
            country_code, real_mobile = mobile_parts
        elif len(mobile_parts) == 1:
            country_code, real_mobile = "86", mobile_parts[0]
        else:
            logging.error("mobile:%s, message:%s" % (mobile, message))
            return dict({'error': 0})

        if DatabaseBuilder.run_mode == 'production':
            # 线上版本才发送验证码
            result = self._send_message_on_production(real_mobile, message)
            logging.info("country_code: %s mobile:%s, message:%s" % (country_code, mobile, message))
            if result['error'] < 0:
                if result['msg'] == 'SENSITIVE_WORDS':
                    # 敏感词 报错。将触发敏感词的单词 记录
                    logging.info("sms_code sensitive words error-word: %s,msg:%s" % (result['hit'], result['msg']))
                    # 尝试替换敏感词
                    if len(result['hit']) > 1:
                        message = message.replace(result['hit'], result['hit'][0]+' '+result['hit'][1:])
                        result = self._send_message_on_production(real_mobile, message)
                        if result.get('msg', '') == 'SENSITIVE_WORDS':
                            logging.info("sms_code sensitive words error-twice: %s,msg:%s" % (result['hit'], result['msg']))

                else:
                    logging.info("sms_code error: %s,msg:%s" % (result['error'], result['msg']))
        else:
            result = dict({'error': 0})
            # logging.info("country_code: %s mobile:%s, message:%s" % (country_code, mobile, message))
        return result

    def _send_message_on_production(self, real_mobile, message):
        # 真正发送短信请求
        resp = requests.post("https://sms-api.luosimao.com/v1/send.json",
                             auth=("api", self.sms_api_key),
                             data={
                                 "mobile": real_mobile,
                                 "message": message
                             }, timeout=3, verify=False)
        return json.loads(resp.content)


    def _update_and_send_sms_code(self, mobile, valid_type, sms_code, sms_code_dao):
        now = dateutil.timestamp()
        if sms_code.unlock_in > now:
            # 在锁定的时间内，不允许发送sms code
            raise ServiceException(20106, 'amounts of send times')

        if (not sms_code.is_validated) and sms_code.last_sent_at + 60000 > now:
            # 最后一次发送的时间在一分钟内，表明发送太过频繁，不允许调用
            raise ServiceException(20104, 'send too frequently')

        if sms_code.is_validated or now > sms_code.expires_in:
            # 先前验证成功过或过期，重新更换验证码
            verification_code = random_number()
            sms_code.verification_code = verification_code
            verification_token = uuid4()
            sms_code.verification_token = verification_token
            sms_code.expires_in = now + 300000  # 5分钟后超时
            sms_code.is_validated = False
        sms_code.sent_count += 1
        sms_code.last_sent_at = now
        sms_code_dao.update(sms_code)
        send_status = self._send_sms_template_message(mobile,valid_type,
                                                      *[str(sms_code.verification_code),
                                                        str(Settings.SITE_NAME)])
        if send_status.get('error', 1) != 0:
            logging.error(send_status)
            raise ServiceException(1003, 'sms service error')

    def _add_and_send_sms_code(self, mobile, valid_type, ip_address, sms_code_dao):
        sms_code = SmsCode()
        sms_code.mobile = mobile
        sms_code.valid_type = valid_type
        verification_code = random_number()
        sms_code.verification_code = verification_code
        verification_token = uuid4()
        sms_code.verification_token = verification_token
        sms_code.max_retry_count = 10
        sms_code.continuous_failed_count = 0
        sms_code.valid_failed_count = 0
        sms_code.valid_count = 0
        sms_code.sent_count = 0
        sms_code.remote_ip_address = ip_address
        sms_code.last_sent_at = dateutil.timestamp()
        sms_code.is_validated = False
        sms_code.expires_in = dateutil.timestamp() + 300000  # 5分钟后超时
        sms_code.unlock_in = 0
        sms_code_dao.add(sms_code)
        send_status = self._send_sms_template_message(mobile, valid_type,
                                                      *[str(sms_code.verification_code),
                                                        str(Settings.SITE_NAME)])
        if send_status.get('error', 1) != 0:
            logging.error(send_status)
            raise ServiceException(1003, 'sms service error')

    def send_password_change_message(self, mobile):
        # password_changed_notice: 您的账号{0}所关联的密码在{1}被修改，如不是本人操作请及时与客服联系【{2}】
        return self._send_sms_template_message(mobile, "password_changed_notice",
                                               *[mobile,
                                                 dateutil.datetime_to_string(datetime.datetime.now(),
                                                                              "%Y-%m-%d %H:%M:%S"),
                                                 Settings.SITE_NAME])

    def send_order_status_change_msg(self, mobile, args):
        args.append(Settings.SITE_NAME)
        return self._send_sms_template_message(mobile, "order_status_changed", *args)

    def send_notify_msg(self, mobile, temp_name, args):
        # 审核，商标预判 的驳回通知 thrift 调用
        # args.append(Settings.SITE_NAME)
        return self._send_sms_template_message(mobile, temp_name, *args)

    def send_sms_code_for_account_name(self, name, valid_type, ip_address):
        with self.create_session(self._default_db) as session:
            sms_code_dao = SmsCodeDao(session)
            sms_code = sms_code_dao.get_by_mobile_valid_type_remote_ip_address(name, valid_type, ip_address)
            if sms_code is not None:
                self._update_and_send_sms_code(name, valid_type, sms_code, sms_code_dao)
            else:
                self._add_and_send_sms_code(name, valid_type, ip_address, sms_code_dao)

    def send_sms_code(self, mobile, valid_type, ip_address):
        """发送短信验证码

        :param mobile: 手机号
        :param valid_type: 验证码类型
        :param verification_token:
        :param ip_address: ip地址
        :return: 参看 SmsSendStatus
        """
        self.send_sms_code_for_account_name(mobile, valid_type, ip_address)

    def update_sms_code_is_validated(self, account_name, valid_type, ip_address):
        with self.create_session(self._default_db) as session:
            sms_code_dao = SmsCodeDao(session)
            sms_code = sms_code_dao.get_by_mobile_valid_type_remote_ip_address(account_name, valid_type, ip_address)
            if sms_code is not None:
                sms_code.is_validated = True
                # 验证成功
                sms_code_dao.update(sms_code)

    def validate_sms_code_for_account_name(self, account_name, valid_type, verification_code, ip_address):
        """ 校验手机验证码是否正确，在校验成功后，做完后续的处理工作必须再调用
        update_sms_code_is_validated方法以释放掉验证成功的验证码

        :param account_name:
        :param valid_type:
        :param verification_code:
        :param ip_address:
        :return:
        """
        with self.create_session(self._default_db) as session:
            sms_code_dao = SmsCodeDao(session)
            sms_code = sms_code_dao.get_by_mobile_valid_type_remote_ip_address(account_name, valid_type, ip_address)
            if sms_code is not None:
                now = dateutil.timestamp()
                if sms_code.is_validated:
                    raise ServiceException(20103, 'verification code is no exist')

                sms_code.valid_count += 1
                if now > sms_code.unlock_in:
                    # 用户没有被锁定
                    if now < sms_code.expires_in:
                        # 没有过期
                        sms_code.valid_count += 1
                        if sms_code.verification_code == verification_code:
                            # 验证成功
                            sms_code_dao.update(sms_code)
                            return
                        else:
                            sms_code.continuous_failed_count += 1
                            sms_code.valid_failed_count += 1

                            if sms_code.continuous_failed_count >= sms_code.max_retry_count:
                                sms_code.unlock_in = now + 60*60*1000  # 锁定一小时
                                sms_code.continuous_failed_count = 0
                                sms_code_dao.update(sms_code)
                                raise ServiceException(20106, 'amounts of input incorrect')
                            # 还没超出错误的频次，累加错误次数
                            sms_code_dao.update(sms_code)
                            raise ServiceException(20102, 'verification code is incorrect')
                    else:
                        # 验证码发送已被锁定
                        sms_code_dao.update(sms_code)
                        raise ServiceException(20103, 'verification code is no exist')
                else:
                    # 验证码发送已被锁定
                    sms_code_dao.update(sms_code)
                    raise ServiceException(20106, 'amounts of input incorrect')
            else:
                raise ServiceException(20103, 'verification code is no exist')

    def validate_sms_code(self, account_name, valid_type, verification_code, ip_address):
        """验证短信

        :param mobile:
        :param valid_type: 校验类型
        :param valid_code:
        :return SmsValidateResult
        """
        self.validate_sms_code_for_account_name(account_name, valid_type, verification_code, ip_address)

    def validate_mobile(self, mobile):
        with self._default_db.create_session() as session:
            sms_code_dao = SmsCodeDao(session)
            is_register = sms_code_dao.get_by_mobile_valid_type(mobile=mobile, valid_type=SmsValidType.SIGNUP)
            return is_register.fields['is_validated'] if is_register is not None else None