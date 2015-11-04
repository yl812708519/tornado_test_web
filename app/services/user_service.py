#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons.biz_model import BizModel, Attribute
from app.commons import stringutil
from app.daos.user_dao import UserDao, User
from app.daos.user_profile_dao import UserProfileDao, UserProfile
from app.services.base_service import BaseService, ServiceException

import hashlib
from configs.database_builder import DatabaseBuilder


class UserBO(BizModel):
    user_id = Attribute('')
    name = Attribute('')
    avatar = Attribute('')
    gender = Attribute('')


class UserProfileBO(BizModel):
    id = Attribute(None)
    user_id = Attribute(0)
    nickname = Attribute('')
    email = Attribute('')
    mobile = Attribute('')
    # avatar = Attribute('')
    province = Attribute('')
    city = Attribute('')
    area = Attribute('')
    company = Attribute('')
    company_desc = Attribute('')
    address = Attribute('')


class UserService(BaseService):
    """用户服务类，封装与用户相关的业务逻辑"""

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def get(self, user_id):
        with self._default_db.create_session() as session:
            user_dao = UserDao(session)
            user = user_dao.get(user_id)
            user_bo = UserBO(**user.fields) if user is not None else None
            return user_bo if user_bo is not None else None

    def get_for_settings(self, user_id):
        with self._default_db.create_session() as session:
            user_dao = UserDao(session)
            user = user_dao.get(user_id)
            if user:
                return UserBO(**user.fields)

    # def is_exist_nickname(self, name, user_id=None):
    #     """判断是否是一个存在的用户名，可用于远程验证
    #
    #     :param user_id: user_id
    #     :param name: 用户名
    #     :return: 返回True表示这个用户名已被占用
    #     """
    #
    #     with self._default_db.create_session() as session:
    #         user_dao = UserDao(session)
    #         user = user_dao.get_by_name(name)
    #         return user is not None and user.user_id != user_id

    def update(self, user_id, name, avatar):
        """ 更新用户信息

        :param user_id: 需要更新的user_id
        :param name:  用户名
        :param avatar: 头像
        :return: 更新成功的用户对象
        """
        with self._default_db.create_session() as session:
            user_dao = UserDao(session)

            user = user_dao.get(user_id)
            if user is not None:
                user.name = name
                user.avatar = avatar
                user_dao.update(user)
            return UserBO(**user.fields)

    def add_profile(self, user_profile_bo):
        """添加用户个人设置的基本信息
        :param user_profile_bo: 个人设置的基本信息
        """
        with self._default_db.create_session() as session:
            user_profile_dao = UserProfileDao(session)
            user_profile = UserProfile()
            user_profile.update(user_profile_bo.attributes)
            return user_profile_dao.add(user_profile)

    def add(self, user_bo, login=True):
        """添加一个用户信息。

        :param user_bo: UserBO 用户业务对象
        :param login: Bool True代表这个用户保存并记录登录时间
        :return: user id
        """
        with self._default_db.create_session() as session:
            user_dao = UserDao(session)
            user = User().update(user_bo.attributes)
            return user_dao.add(user)

    def get_profile(self, user_id):
        """
        获取用户profle数据
        :param user_id:
        :return:
        """
        with self._default_db.create_session() as session:
            profile_dao = UserProfileDao(session)
            profile = profile_dao.get_by_user(user_id)
            return UserProfileBO(**profile.fields) if profile is not None else UserProfileBO()

    def update_profile(self, profile_bo):
        """
        更新用户profile信息 和 user表中的nickname
        :param profile:
        :return:
        """
        with self._default_db.create_session() as session:
            profile_dao = UserProfileDao(session)
            user_dao = UserDao(session)

            profile = profile_dao.get_by_user(profile_bo.user_id)
            cur_user = user_dao.get(profile_bo.user_id)
            cur_user.name = profile_bo.nickname
            user_dao.update(cur_user)

            profile.update(profile_bo.attributes)
