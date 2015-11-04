#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging
import functools

from tornado.web import RequestHandler, utf8, HTTPError, StaticFileHandler
from app.services.base_service import ServiceError, ServiceException, ServiceValidationFailsException
from app.services.oss_upload_service import OssUploadService
from app.services.user_service import UserService
from app.services.basebanservice import ContextBO
from app.commons import jsonutil
from configs.database_builder import DatabaseBuilder
from configs.settings import Settings
from configs.errors import Errors


class ErrorHandler(RequestHandler):
    """Generates an error response with ``status_code`` for all requests."""

    def initialize(self, status_code):
        self.set_status(status_code)

    def prepare(self):
        raise HTTPError(self._status_code)

    def check_xsrf_cookie(self):
        # POSTs to an ErrorHandler don't actually have side effects,
        # so we don't need to check the xsrf token.  This allows POSTs
        # to the wrong url to return a 404 instead of 403.
        pass

    @property
    def is_ie(self):
        agent = self.request.headers.get('User-Agent', [])
        return 'MSIE' in agent and 'Windows NT' in agent

    @classmethod
    def static_url_on_ie(cls, path):
        version_hash = StaticFileHandler.get_version(Settings.settings(), path)
        return '%s?v=%s' % ('/s/'+path, version_hash)

    def write_error(self, status_code, **kwargs):
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            RequestHandler.write_error(self, status_code, **kwargs)
        else:
            if status_code == 404 or status_code == 500:
                kwargs['is_order'] = kwargs.get('is_order', False)
                self.render('home/' + str(status_code) + '.html', **kwargs)
            else:
                self.finish("<html><title>%(code)d: %(message)s</title>"
                            "<body>%(code)d: %(message)s</body></html>" % {
                                "code": status_code,
                                "message": self._reason,
                            })


class ParentHandler(RequestHandler):
    def get_context_bo(self):
        context_bo = ContextBO()
        context_bo.remote_ip = self.request.remote_ip
        if self.current_user:
            context_bo.current_user_id = self.current_user.user_id
        return context_bo

    def get_req_bo(self, req_bo_class, need_validate=True):
        """

        :param req_bo_class:
        :type req_bo_class: ReqBO
        :return:
        :rtype:
        """
        req_bo = req_bo_class()

        for name, obj in req_bo.class_attributes:
            if name == 'context':
                continue
            condition = obj.v_condition
            if condition is not None and not condition(self.get_argument(condition.c_field, None)):
                setattr(req_bo, name, obj.default)
                continue
            if obj.attri_type in (list, tuple):
                value = tuple(self.get_arguments(name)) if obj.attri_type is tuple else self.get_arguments(name)
                setattr(req_bo, name, req_bo.value_converter(obj, value))
            else:
                setattr(req_bo, name, req_bo.value_converter(obj, self.get_argument(name, obj.default)))

        req_bo.context = self.get_context_bo()

        if need_validate:
            errors = req_bo.validate()
            if len(errors) > 0:
                raise ServiceValidationFailsException(errors)

        return req_bo

    def validate(self, bo, is_raise_all=False):
        """

        :param bo: 业务
        :type bo: app.commons.biz_model.BizModel
        :param is_raise_all: 是否获取所有的报错
        :type is_raise_all: bool
        :return:
        :rtype:
        """
        errors = bo.validate(is_validate_all=is_raise_all)
        if len(errors) > 0:
            raise ServiceValidationFailsException(errors, is_raise_all)


class BaseHandler(ParentHandler):
    """基础Handler

    """
    COOKIE_DOMAIN = None
    EXPIRES_DAYS = 365

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.validation_success = True
        self.validation_errors = {}
        self.validation_data = {}
        if BaseHandler.COOKIE_DOMAIN is None:
            BaseHandler.COOKIE_DOMAIN = '.' + Settings.WEBSITE

    @property
    def is_ie(self):
        agent = self.request.headers.get('User-Agent', [])
        return 'MSIE' in agent and 'Windows NT' in agent

    @classmethod
    def static_url_on_ie(cls, path):
        version_hash = StaticFileHandler.get_version(Settings.settings(), path)
        return '%s?v=%s' % ('/s/'+path, version_hash)

    def render(self, template_name, **kwargs):
        # 将当前登陆用户统一传给页面
        kwargs["current_user"] = self.current_user
        kwargs["run_mod"] = DatabaseBuilder.run_mode
        kwargs['is_order'] = kwargs.get('is_order', False)
        RequestHandler.render(self, template_name, **kwargs)

    def set_default_headers(self):
        """Override this to set HTTP headers at the beginning of the request.

        For example, this is the place to set a custom ``Server`` header.
        Note that setting such headers in the normal flow of request
        processing may not do what you want, since headers may be reset
        during error handling.
        """
        self.clear_header("Server")

    def _execute(self, transforms, *args, **kwargs):
        if self.request.method.upper() == 'POST':
            self.request.method = self.get_argument('_method', 'POST').upper()

        RequestHandler._execute(self, transforms, *args, **kwargs)

    def write_error(self, status_code, **kwargs):
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            RequestHandler.write_error(self, status_code, **kwargs)
        else:
            if status_code == 404 or status_code == 500:
                self.render('home/' + str(status_code) + '.html', **kwargs)
            else:
                self.finish("<html><title>%(code)d: %(message)s</title>"
                            "<body>%(code)d: %(message)s</body></html>" % {
                                "code": status_code,
                                "message": self._reason,
                            })

    # def static_url(self, path):
    # self.require_setting("static_path", "static_url")
    # if not hasattr(RequestHandler, "_static_hashes"):
    #         RequestHandler._static_hashes = {}
    #     hashes = RequestHandler._static_hashes
    #     if len(path) > 0 and path[0] == "/":
    #         file_path = path[1:]
    #     else:
    #         file_path = path
    #     abs_path = os.path.join(self.application.settings["static_path"],
    #                             file_path)
    #     if abs_path not in hashes:
    #         try:
    #             f = open(abs_path)
    #             hashes[abs_path] = hashlib.md5(f.read()).hexdigest()
    #             f.close()
    #         except:
    #             logging.error("Could not open static file %r", path)
    #             hashes[abs_path] = None
    #     base = self.request.protocol + "://" + self.request.host \
    #         if getattr(self, "include_host", False) else ""
    #     static_url_prefix = self.settings.get('static_url_prefix', '/static/')
    #     if hashes.get(abs_path):
    #         return base + static_url_prefix + path + "?v=" + hashes[abs_path][:5]
    #     else:
    #         return base + static_url_prefix + path

    # def set_unicode_cookie(self, name, value, domain=None, expires=None, path="/",
    #                        expires_days=None, **kwargs):
    #     """Sets the given cookie name/value with the given options.
    #
    #     Additional keyword arguments are set on the Cookie.Morsel
    #     directly.
    #     See http://docs.python.org/library/cookie.html#morsel-objects
    #     for available attributes.
    #     """
    #     name = utf8(name)
    #     value = utf8(value)
    #     if re.search(r"[\x00-\x20]", name + value):
    #         # Don't let us accidentally inject bad stuff
    #         raise ValueError("Invalid cookie %r: %r" % (name, value))
    #     if not hasattr(self, "_new_cookies"):
    #         self._new_cookies = Cookie.SimpleCookie()
    #
    #     if name in self._new_cookie:
    #         del self._new_cookie[name]
    #     self._new_cookie[name] = value
    #     morsel = self._new_cookie[name]
    #
    #     if domain:
    #         morsel["domain"] = domain
    #     if expires_days is not None and not expires:
    #         expires = datetime.datetime.utcnow() + datetime.timedelta(
    #             days=expires_days)
    #     if expires:
    #         morsel["expires"] = httputil.format_timestamp(expires)
    #     if path:
    #         morsel["path"] = path
    #     for k, v in kwargs.items():
    #         if k == 'max_age':
    #             k = 'max-age'
    #         morsel[k] = v
    #
    #     new_cookie = Cookie.BaseCookie()
    #     self._new_cookies.append(new_cookie)
    #     new_cookie[name] = urllib.quote(value)
    #     if domain:
    #         new_cookie[name]["domain"] = domain
    #     if expires_days is not None and not expires:
    #         expires = datetime.datetime.utcnow() + datetime.timedelta(
    #             days=expires_days)
    #     if expires:
    #         timestamp = calendar.timegm(expires.utctimetuple())
    #         new_cookie[name]["expires"] = email.utils.formatdate(
    #             timestamp, localtime=False, usegmt=True)
    #     if path:
    #         new_cookie[name]["path"] = path
    #     for k, v in kwargs.iteritems():
    #         new_cookie[name][k] = v

    # def get_unicode_cookie(self, name, default=None):
    #     """Gets the value of the cookie with the given name, else default."""
    #     if name in self.cookies:
    #         return _unicode(urllib.unquote(self.cookies[name].value))
    #     return _unicode(urllib.unquote(default))

    def get_current_user(self):
        user_id = self.get_secure_cookie("ut_user_id")
        if not user_id:
            return None
        else:
            user = UserService().get_for_settings(user_id)
            if user:
                return user
            else:
                return None

    def set_login_token(self, user, remember_me=True):
        self.clear_all_cookies()
        if remember_me:
            expires = datetime.datetime.utcnow() + datetime.timedelta(days=BaseHandler.EXPIRES_DAYS)
        else:
            expires = None
        if expires:
            self.set_secure_cookie('ut_user_id',
                                   str(user.user_id),
                                   expires_days=BaseHandler.EXPIRES_DAYS,
                                   path="/",
                                   domain=BaseHandler.COOKIE_DOMAIN)
        else:
            self.set_secure_cookie('ut_user_id',
                                   str(user.user_id),
                                   expires_days=None, path="/",
                                   domain=BaseHandler.COOKIE_DOMAIN)

    def logout(self):
        """退出登录
        """
        self.clear_all_cookies()
        self.clear_all_cookies(path="/", domain=BaseHandler.COOKIE_DOMAIN)

    def upload_url(self, path, include_host=None, **kwargs):
        self.require_setting("image_upload_path", "upload_url")

        url = self.settings.get('image_upload_url_prefix', '/iu/') + path

        if include_host is None:
            include_host = getattr(self, "include_host", False)

        if include_host:
            base = self.settings.get('upload_site_root', '')
        else:
            base = ""
        return base + url

    def oss_file_url(self, path):
        upload_file_service = OssUploadService()
        download_url = upload_file_service.download_site() + path
        return download_url

    def oss_img_url(self, path, suffix=None):
        if path is None or len(path.split()) == 0:
            # 因为jqery不兼容，空字符串不替换默认的。所以只能把空字符串改成这个了！！！
            return Settings.STATIC_URL_PREFIX + 'img/default_img.jpg'
        upload_file_service = OssUploadService()
        download_url = upload_file_service.download_image_site() + path
        if suffix is not None:
            download_url = download_url + suffix
        return download_url

    def get_template_namespace(self):
        custom_namespace = dict(
            upload_url=self.upload_url,
            oss_img_url=self.oss_img_url,
            oss_file_url=self.oss_file_url
        )
        namespace = RequestHandler.get_template_namespace(self)
        namespace.update(custom_namespace)
        return namespace

    def get_form(self, name, strip=True):
        """获取一个表单
        比如提交的参数存在 user.id、user.name 这样的表单，那么可以通过如下方式提取出user对象::

        user = self.get_form('user')

        :param name: 表单名
        :param strip: 参数
        :return: dict 表单对象
        """
        return self._get_form(name, self.request.arguments, strip)
        pass

    def _get_form(self, name, source, strip=True):
        form = {}
        prefix = name + '.'
        for key, value in source.items():
            if key.startswith(prefix):
                form[key[key.index(".") + 1:]] = self.get_argument(key, strip=strip)
        return form

        # 用于提示页面，参数：跳转路径，多久之后跳转，提示的信息
        # def alter(self, nexturl, time, message):
        #     res = dict(nexturl= nexturl,
        #                 time = time,
        #                 message = message
        #     )
        #     self.render("activities/alter.html", **res)


class RestfulAPIHandler(ParentHandler):
    def __init__(self, application, request, **kwargs):
        super(RestfulAPIHandler, self).__init__(application, request, **kwargs)
        self.validation_success = True
        self.validation_errors = {}
        self.validation_data = {}

    def _execute(self, transforms, *args, **kwargs):
        if self.request.method.upper() == 'POST':
            self.request.method = self.get_argument('_method', 'POST').upper()

        RequestHandler._execute(self, transforms, *args, **kwargs)

    # def get_current_user(self):
    # user_id = self.get_secure_cookie("ut_user_id")
    #     if not user_id:
    #         return None
    #     else:
    #         user = UserService().get(user_id)
    #         if user:
    #             return user
    #         else:
    #             return None

    @property
    def is_ie(self):
        agent = self.request.headers.get('User-Agent', None)
        return 'MSIE' in agent and 'Windows NT' in agent

    @classmethod
    def static_url_on_ie(cls, path):
        version_hash = StaticFileHandler.get_version(Settings.settings(), path)
        return '%s?v=%s' % ('/s/'+path, version_hash)

    def get_current_user(self):
        user_id = self.get_secure_cookie("ut_user_id")
        if not user_id:
            return None
        else:
            user = UserService().get_for_settings(user_id)
            if user:
                return user
            else:
                return None

    def write_success(self):
        self.write(1)

    def write_except(self, e):
        if isinstance(e, ServiceException):
            self.write(dict(code=e.code, msg=Errors.error_message(e.code)), 400)
        elif isinstance(e, ServiceError):
            logging.exception(e)
            self.write(dict(code=e.code, msg=Errors.error_message(e.code)), 500)
        elif isinstance(e, ServiceValidationFailsException):
            self.write(dict(code=e.code, field=e.field, msg=e.msg, errors=getattr(e, 'errors', '')), 400)
        else:
            pass
            # raise e

    def write_error(self, status_code, **kwargs):
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.write_except(kwargs['exc_info'][1])
            self.finish()
        else:
            if "exc_info" in kwargs:
                self.set_header("Content-Type", "application/json; charset=UTF-8")
                try:
                    self.write_except(kwargs['exc_info'][1])
                except Exception:
                    self.write(dict(code=1000, msg=Errors.error_message(1000)), 500)
                self.finish()
            else:
                self.write(dict(code=status_code, msg=self._reason), status_code)
                self.finish()

    def log_exception(self, typ, value, tb):
        if isinstance(value, (ServiceException, ServiceValidationFailsException)):
            return
        RequestHandler.log_exception(self, typ, value, tb)

    def get_form(self, name, strip=True):
        """获取一个表单
        比如提交的参数存在 user.id、user.name 这样的表单，那么可以通过如下方式提取出user对象::

        user = self.get_form('user')

        :param name: 表单名
        :param strip: 参数
        :return: dict 表单对象
        """
        return self._get_form(name, self.request.arguments, strip)
        pass

    def _get_form(self, name, source, strip=True):
        form = {}
        prefix = name + '.'
        for key, value in source.items():
            if key.startswith(prefix):
                form[key[key.index(".") + 1:]] = self.get_argument(key, strip=strip)
        return form

        # 用于提示页面，参数：跳转路径，多久之后跳转，提示的信息
        # def alter(self, nexturl, time, message):
        #     res = dict(nexturl= nexturl,
        #                 time = time,
        #                 message = message
        #     )
        #     self.render("activities/alter.html", **res)


    def write(self, chunk, status=None):
        """Writes the given chunk to the output buffer.

        To write the output to the network, use the flush() method below.

        If the given chunk is a dictionary, we write it as JSON and set
        the Content-Type of the response to be ``application/json``.
        (if you want to send JSON as a different ``Content-Type``, call
        set_header *after* calling write()).

        Note that lists are not converted to JSON because of a potential
        cross-site security vulnerability.  All JSON output should be
        wrapped in a dictionary.  More details at
        http://haacked.com/archive/2008/11/20/anatomy-of-a-subtle-json-vulnerability.aspx
        """
        if self._finished:
            raise RuntimeError("Cannot write() after finish().  May be caused "
                               "by using async operations without the "
                               "@asynchronous decorator.")

        if isinstance(chunk, dict):
            chunk = jsonutil.json_encode(chunk)
        elif isinstance(chunk, list):
            chunk = jsonutil.json_encode({"list": chunk})
        else:
            chunk = jsonutil.json_encode({"result": chunk})
        chunk = utf8(chunk)
        self._write_buffer.append(chunk)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        if status is not None:
            self.set_status(status)

