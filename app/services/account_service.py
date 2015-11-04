#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2014-11-07

@author: huwei
"""
import hashlib
from app.commons import stringutil, dateutil
from app.commons.biz_model import BizModel, Attribute
from app.daos.account_dao import AccountDao, AccountType, Account
from app.daos.password_dao import Password, PasswordDao
from app.daos.account_dao import AccountDao
from app.daos.sms_code_dao import SmsCodeDao
from app.daos.user_dao import UserDao,User
from app.daos.user_profile_dao import UserProfile, UserProfileDao
from app.services.base_service import ServiceException, BaseService

from app.services.user_service import UserBO, UserService
from app.services.captcha_service import CaptchaService
from app.services.sms_code_service import SmsCodeService, SmsValidType
from configs.database_builder import DatabaseBuilder

__author__ = 'freeway'


class AccountBO(BizModel):
    id = Attribute(None)
    user_id = Attribute(default='')
    account_type = Attribute(default=None)
    name = Attribute(default=None)
    account = Attribute('')


class AccountService(BaseService):
    # 多次输入用户名和密码失败后的锁定时间
    LOCKED_TIME = 3600*1000

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    @staticmethod
    def _get_account(account_name, account_type, session):
        account_dao = AccountDao(session)
        return account_dao.get_by_name_account_type(account_name, account_type)

    @staticmethod
    def _encrypted_password(password, salt):
        """
         * 密码加密
         * @param string password 密码
         * @param string salt 混淆码
         * @return string 加密后的密码
        """
        return hashlib.md5(hashlib.md5(password).hexdigest()+salt).hexdigest()

    @staticmethod
    def _create_new_salt():
        """创建一个新的混淆码。

        :return: string 混淆码
        """
        return stringutil.random_string(5)

    def is_exist_account(self, account_name, account_type):
        with self.create_session(self._default_db) as session:
            return self._get_account(account_name, account_type, session) is not None

    def is_exist_user(self, mobile, email):
        """
        验证是否有 手机帐号或邮箱帐号  已被使用
        :param mobile:
        :param email:
        :return:
        """
        with self._default_db.create_session() as session:
            mobile_account = self._get_account(mobile, AccountType.MOBILE, session)
            email_account = self._get_account(email, AccountType.EMAIL, session)
            return not(mobile_account is None and email_account is None)

    def authenticate(self, mobile, password, ip_address, captcha=''):
        """验证账号密码

        :param mobile: 手机号
        :param password: 密码
        :param ip_address: 验证的 ip 地址
        :return:
        """
        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_name_account_type(mobile, AccountType.MOBILE)
            if account is None:
                raise ServiceException(20002, 'mobile number or password is incorrect')
            if dateutil.timestamp() - account.locked_at < self.LOCKED_TIME:
                raise ServiceException(20005, 'incorrect more, the account is locked')
            if account.fail_count > 3:
                # 错误次数超过三次需要添加图像验证码
                if len(captcha.strip()) == 0:
                    raise ServiceException(20008, 'captcha is required')
                elif not CaptchaService.validate_captcha(mobile, captcha):
                        raise ServiceException(20009, 'captcha is incorrect')

            password_dao = PasswordDao(session)
            pwd = password_dao.get_by_account_id(account.id)
            if pwd is None:
                raise ServiceException(20002, 'mobile number or password is incorrect')
            expected_password = self._encrypted_password(password, pwd.salt)
            account.last_visit_ip = ip_address

            if pwd.hashed_password != expected_password:
                account.fail_count += 1
                if account.fail_count > 10:
                    account.locked_at = dateutil.timestamp()
                    account_dao.update(account)
                    raise ServiceException(20005, 'incorrect more, the account is locked')
                elif account.fail_count > 2:
                    account_dao.update(account)
                    raise ServiceException(20007, 'incorrect more, and need input captcha')
                else:
                    account_dao.update(account)
                    raise ServiceException(20002, 'mobile number or password is incorrect')
            user_dao = UserDao(session)

            user = user_dao.get(account.user_id)
            if user.is_locked:
                raise ServiceException(20003, 'the account is locked')
            # 登录成功，错误次数清0。
            account.fail_count = 0
            account.last_login_ip = ip_address
            account_dao.update(account)
            return UserBO(**user.fields)

    def get_account_by_mobile(self, mobile):
        """ 根据手机号检查这个账户存不存在
        :param country_code:
        :param mobile:
        """
        return self.get_account(mobile, AccountType.MOBILE)

    def get_account(self, account_name, account_type):
        """获取账号信息

        :param account_name:
        :param account_type:
        :return:
        """
        with self.create_session(self._default_db) as session:
            account = self._get_account(account_name, account_type, session)

            if account is not None and AccountType.MOBILE == account_type:
                # 之所以要这么做，目的是因为password和account不在同一张表。
                # 由于没有事务，有可能会导account保存了，但password没有保存，为健壮性考虑需要获取一次password
                password_dao = PasswordDao(session)
                pwd = password_dao.get_by_account_id(account.id)
                return AccountBO(**account.fields) if pwd is not None else None
            else:
                return AccountBO(**account.fields) if account is not None else None

    def add_account(self, accounts, password, remote_ip, nickname):
        """

        :param account_name:
        :param account_type:
        :param nick_name:
        :param password:
        :return: 返回 account 对象
        """
        with self._default_db.create_session() as session:
            acc = self.is_exist_user(accounts['mobile'], accounts['email'])
            if acc is True:
                # 两个帐号有已经创建的不能再创建
                raise ServiceException(20001, 'the account is exist')
            salt = self._create_new_salt()
            hashed_password = self._encrypted_password(password, salt)
            user = User()
            user_dao = UserDao(session)
            # id生成器
            from app.commons.database_sequence import DatabaseSequenceFactory
            user.user_id = DatabaseSequenceFactory().get_obfuscated_id('bingoip', 'users',
                                                                       has_random=True, random_length=1)
            user.name = nickname
            user.gender = 'N'
            user.is_locked = False
            user_dao.add(user)
            # 添加profile 信息
            profile = UserProfile()
            profile.user_id = user.user_id
            profile.nickname = nickname
            profile.mobile = accounts['mobile']
            profile_dao = UserProfileDao(session)
            profile_dao.add(profile)
            # 添加account信息
            # 建立帐号
            account = Account()
            account.account = accounts['mobile']
            account.user_id = user.user_id
            account.account_type = "mobile"
            account.locked_at = 0L
            account.fail_count = 0
            account_dao = AccountDao(session)
            account_dao.add(account)

            pwd = Password()
            password_dao = PasswordDao(session)
            pwd.account_id = account.id
            pwd.salt = salt
            pwd.hashed_password = hashed_password
            password_dao.add(pwd)

            return user.user_id

    def update_account(self, account_name, account_type):
        """
        :return: 返回 account 对象
        """
        with self.create_session(self._default_db) as session:
            acc = self._get_account(account_name, account_type, session)

            user = User()
            user.name = account_name
            user.user_id = stringutil.uuid4()
            user.gender = 'N'
            user.is_locked = False
            user_dao = UserDao(session)
            user_dao.update(user)

            acc = Account()
            acc.name = account_name
            acc.user_id = user.user_id
            acc.account_type = account_type
            acc.locked_at = 0L
            acc.fail_count = 0
            account_dao = AccountDao(session)
            account_dao.update(acc)
            return AccountBO(**acc.fields)

    def change_password_by_verification_token(self, mobile,
                                              verification_token, new_password, ip_address):
        """根据verification_token，修改密码
        """
        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_name_account_type(mobile, AccountType.MOBILE)
            if account is None:
                raise ServiceException(20004, 'the account is not existing.')
            sms_code_dao = SmsCodeDao(session)
            sms_code = sms_code_dao.get_by_mobile_valid_type_verification_token(mobile, SmsValidType.RESET_PASSWORD,
                                                                                verification_token)
            sms_code = sms_code is not None and sms_code.is_validated

            if not sms_code:
                raise ServiceException(20103, 'verification code is not valid.')
            password_dao = PasswordDao(session)
            print account.user_id
            password = password_dao.get_by_account_id(account.id)
            password.salt = self._create_new_salt()
            password.hashed_password = self._encrypted_password(new_password, password.salt)
            password_dao.update(password)
            # 删除验证,单拿出来写了，因为直接掉service层的会有一些问题
            sms_code_dao = SmsCodeDao(session)
            sms_code = sms_code_dao.get_by_mobile_valid_type_verification_token(mobile, SmsValidType.RESET_PASSWORD,
                                                                                verification_token)
            if sms_code is not None:
                sms_code_dao.delete(sms_code)

    def reset_password(self, new_password, new_password_confirm, mobile, remote_ip):
        """ 重置密码，用于忘记密码后找回密码

        :param reset_password_req_bo:
        :type reset_password_req_bo: app.services.bos.account.ResetPasswordReqBO
        :return:
        :rtype:
        """
        if new_password != new_password_confirm:
            raise ServiceException(20013, 'password and password confirm is not match.')

        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_name_account_type(mobile,
                                                           AccountType.MOBILE)
            user_id = account.user_id
            if account is None:
                raise ServiceException(20004, 'the account is not existing.')
            sms_service = SmsCodeService()

            password_dao = PasswordDao(session)
            password = password_dao.get_by_account_id(account.id)
            # 修改密码
            password.salt = self._create_new_salt()
            password.hashed_password = self._encrypted_password(new_password, password.salt)
            password_dao.update(password)
            sms_service.update_sms_code_is_validated(account.account, SmsValidType.RESET_PASSWORD,
                                                     remote_ip)

            return user_id

    def change_password(self, user_id, old_password, new_password):
        """ 修改密码

        :param user_id: 用户id
        :param old_password: 当前的密码
        :param new_password: 新密码
        :return:
        """
        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_user_id_account_type(user_id, AccountType.MOBILE)
            if account is None:
                raise ServiceException(20004, 'the account is not existing.')

            password_dao = PasswordDao(session)
            password = password_dao.get_by_account_id(account.id)

            encrypted_password = self._encrypted_password(old_password, password.salt)
            if password.hashed_password != encrypted_password:
                raise ServiceException(20010, 'current password is incorrect.')
            password.salt = self._create_new_salt()
            password.hashed_password = self._encrypted_password(new_password, password.salt)
            return password_dao.update(password)
            # TODO: 发送给这个客户的手机发送通知，告知当前账号的密码已被修改

    def get_verification_token(self, mobile, sms_valid_type, remote_ip):
        """获取验证码token

        :param mobile: 手机号
        :param sms_valid_type: 短信发送类型
        :param remote_ip: 远程IP
        :return: :raise ServiceException: 20004
        """
        with self.create_session(self._default_db) as session:
            if SmsValidType.RESET_PASSWORD == sms_valid_type:
                account_dao = AccountDao(session)
                account = account_dao.get_by_name_account_type(mobile, AccountType.MOBILE)
                if account is None:
                    raise ServiceException(20004, 'the account is not existing.')
        sms_code_service = SmsCodeService()
        verification_token = sms_code_service.get_verification_token(mobile,
                                                                     sms_valid_type,
                                                                     remote_ip)
        return verification_token

    def resend_verification_code(self, mobile,
                                 verification_token, sms_valid_type,
                                 remote_ip):
        """重新发送手机验证码
        :param country_code:
        :param mobile:
        :param verification_token:
        :param sms_valid_type: SmsValidType
        :param remote_ip: 远程调用的ip地址
        """
        with self.create_session(self._default_db) as session:
            if SmsValidType.RESET_PASSWORD == sms_valid_type:
                account_dao = AccountDao(session)
                account = account_dao.get_by_name_account_type(mobile, AccountType.MOBILE)
                if account is None:
                    raise ServiceException(20004, 'the account is not existing.')

        sms_code_service = SmsCodeService()
        sms_code_service.send_sms_code(mobile, sms_valid_type,
                                       remote_ip)

    def get_by_user_id(self, user_id):
        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            return AccountBO(**(account_dao.get_by_user_id(user_id)).fields)

    def is_correct_password(self, user_id, pwd):
        """
        验证用户密码是否正确
        :param pwd:
        :return: bool
        """
        with self._default_db.create_session() as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_user_id_account_type(user_id, AccountType.MOBILE)
            if account is None:
                raise ServiceException(20004, 'the account is not existing.')
            password_dao = PasswordDao(session)
            password = password_dao.get_by_account_id(account.id)
            encrypted_password = self._encrypted_password(pwd, password.salt)

            return password.hashed_password == encrypted_password

    def send_sms_code_for_signup(self, account_name, remote_ip):
        """ 发送注册的验证码

        :param send_sms_req_bo:
        :type send_sms_req_bo: app.services.bos.account.SendSmsReqBO
        :return:
        """
        with self.create_session(self._default_db) as session:
            account_dao = AccountDao(session)
            account = account_dao.get_by_name_account_type(account_name, AccountType.MOBILE)
            if account is not None:
                raise ServiceException(20000, 'the account is existing.')
            sms_code_service = SmsCodeService()
            sms_code_service.send_sms_code_for_account_name(account_name, SmsValidType.SIGNUP,
                                                            remote_ip)