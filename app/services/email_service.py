#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'
import hashlib
import smtplib
from configs.settings import Settings
from email.mime.text import MIMEText
from app.commons import dateutil
from app.commons.biz_model import BizModel, Attribute
from app.services.base_service import ServiceException
from app.commons.stringutil import random_number, uuid4
from app.services.base_service import BaseService
from app.services.account_service import AccountService, AccountType
from configs.database_builder import DatabaseBuilder


class EmailType(object):
    RESET_PASSWORD = 'reset_password'
    FEED_BACK = 'feed_back'


class EmailTemplate(object):

    RESET_PASSWORD = '<div id="mailContentContainer" class="qmbox qm_con_body_content" style="">\
                        <h3 class="title">【冰狗网】密码修改确认</h3>\
                        <p>\
                        <span>\
                        <strong>请点击以下链接，以确认是您本人申请修改您的密码：</strong>\
                        </span>\
                        </p>\
                        <p>\
                        <a class="link" target="_blank" href="{params[url]}">{params[url]}</a>\
                        </p>\
                        <p>如果以上链接不能点击，你可以复制网址URL，然后粘贴到浏览器地址栏打开，完成确认。</p>\
                        <p>- 冰狗网</p>\
                        <p class="info">（这是一封自动发送的邮件，请不要直接回复）</p>\
                        <li></li>\
                        </div>'
    ORDER_NOTICE = '{0}, 您有一条新订单等待处理，{1}，类型为{2}'


class EmailBO(BizModel):
    receiver = Attribute(None)
    expired_at = Attribute(None)


class EmailService(BaseService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        # 设置服务器名称、用户名、密码以及邮件后缀
        self.mail_name = "冰狗知识产权"
        self.mail_host = "smtp.163.com"
        self.mail_user = "bingoip@163.com"
        self.mail_pass = "eking123"
        self.mail_postfix = "163.com"
        self.mail_user = "bingoip@163.com"

    def _send_email(self, to_list, sub, context):
        """
        to_list: 发送给谁
        sub: 主题
        context: 内容
        """
        sender = self.mail_name.encode('utf-8') + '<'+self.mail_user+'>'  # 发件人
        msg = MIMEText(context, _subtype='html', _charset='utf-8')  # 内容
        msg['Subject'] = sub  # 主标题
        msg['From'] = sender
        # msg['To'] = ";".join(to_list) #收件人列表
        try:
            send_smtp = smtplib.SMTP()
            send_smtp.connect(self.mail_host)
            send_smtp.login(self.mail_user, self.mail_pass)
            send_smtp.sendmail(sender, to_list, msg.as_string())
            send_smtp.close()
            return True
        except Exception, e:
            raise e

    def _create_token(self):
        token_str = uuid4()
        token_str1 = token_str+str(dateutil.timestamp())
        return hashlib.md5(token_str1).hexdigest()

    def get_by_token(self, token, is_valid=False):
        """
        通过token获取 邮件信息
        :param token:
        :param is_valid: 是否更新is_validated状态
        :return:
        """
        with self._default_db.create_session() as session:
            email_dao = PasswordResetEmailDao(session)
            email = email_dao.get_first_by_criterion(*[PasswordResetEmail.reset_token == token,
                                                       PasswordResetEmail.is_validated == 0])
            return EmailBO(**email.fields) if email is not None else None

    def create_email(self, email_address, sub='', content=None):
                try:
                    self._send_email(email_address,
                                     sub=sub,
                                     context=content)
                except Exception, e:
                    raise e

    def _create_cs_notice_email(self, treat_type, email, order_name):
        self.create_email(email,
                          EmailTemplate.ORDER_NOTICE.format(dateutil.timestamp_to_string(dateutil.timestamp(), '%H:%M'),
                                                            order_name,
                                                            '代填' if treat_type == 'delegate' else '审核'))
