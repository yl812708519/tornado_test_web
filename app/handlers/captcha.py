#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from wheezy.captcha.image import captcha, text, warp, rotate, offset, curve, noise, smooth
from wheezy.captcha.image import background
from app.handlers.application import BaseHandler
from app.services.captcha_service import CaptchaService
from configs.settings import Settings


class CaptchaHandler(BaseHandler):

    # 小写字母，去除可能干扰的i，l，o，z
    _letter_cases = "abcdefghjkmnprstuvwxy"
    # 大写字母
    _upper_cases = _letter_cases.upper()
    # 数字
    _numbers = ''.join(map(str, range(3, 10)))
    _init_chars = ''.join((_letter_cases, _upper_cases, _numbers))

    def get(self, *args, **kwargs):
        """  显示验证码
        :param args:
        :param kwargs:
        :return:
        """
        mobile = self.get_argument('account_name', '')
        code = CaptchaService.generate_captcha_by_mobile(mobile)
        font_filename1 = os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'fonts', 'SFSlapstickComicShaded.ttf')
        captcha_image = captcha(
            width=150,
            height=60,
            drawings=[
            background(),
            text(fonts=[font_filename1],
                 font_sizes=[48],
                 drawings=[
                     warp(),
                     rotate(),
                     offset()
                 ]),
            curve(),
            curve(),
            noise(),
            noise(),
            # smooth()
        ])
        image = captcha_image(code)
        img_stream = io.BytesIO()
        image.save(img_stream, format="JPEG", quality=75)
        s = img_stream.getvalue()
        self.set_header('Content-type', 'image/jpg')
        self.set_header('Content-length', len(s))
        self.write(s)