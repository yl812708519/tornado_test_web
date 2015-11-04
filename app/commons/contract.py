#!/usr/bin/env python
# -*- coding: utf-8 -*-


from xhtml2pdf.document import pisaDocument

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import fonts
from xhtml2pdf.default import DEFAULT_FONT
import reportlab.lib.styles
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

import logging

from decimal import Decimal
import re

# Copyright 2010 Dirk Holtwick, holtwick.it
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

log = logging.getLogger("xhtml2pdf")


# codes to solve the PDF's Chinese line-break problem below from http://slee.sinaapp.com/?p=76
import xhtml2pdf.reportlab_paragraph
from xhtml2pdf.reportlab_paragraph import LEADING_FACTOR


def wrap(self, availWidth, availHeight):
    # work out widths array for breaking
    self.width = availWidth
    style = self.style
    leftIndent = style.leftIndent
    first_line_width = availWidth - (leftIndent + style.firstLineIndent) - style.rightIndent
    later_widths = availWidth - leftIndent - style.rightIndent
    try:
        blPara = self.breakLinesCJK([first_line_width, later_widths])
    except:
        blPara = self.breakLines([first_line_width, later_widths])
    self.blPara = blPara
    autoLeading = getattr(self, 'autoLeading', getattr(style, 'autoLeading', ''))
    leading = style.leading
    if blPara.kind == 1 and autoLeading not in ('', 'off'):
        height = 0
        if autoLeading == 'max':
            for l in blPara.lines:
                height += max(l.ascent - l.descent, leading)
        elif autoLeading == 'min':
            for l in blPara.lines:
                height += l.ascent - l.descent
        else:
            raise ValueError('invalid autoLeading value %r' % autoLeading)
    else:
        if autoLeading == 'max':
            leading = max(leading, LEADING_FACTOR * style.fontSize)
        elif autoLeading == 'min':
            leading = LEADING_FACTOR * style.fontSize
        height = len(blPara.lines) * leading
    self.height = height
    return self.width, self.height


# end

def Create_PDF_into_buffer(html, font_file_path):

    # # 注册字体
    pdfmetrics.registerFont(TTFont('yahei', font_file_path))
    #
    fonts.addMapping('song', 0, 0, 'song')
    fonts.addMapping('song', 0, 1, 'song')
    DEFAULT_FONT['helvetica'] = 'yahei'
    xhtml2pdf.reportlab_paragraph.Paragraph.wrap = wrap
    return pisaDocument(html)


def multiple_replace(adict):
    """
    获得一个函数，用于：
    按照 给定字典中的key替换字符串中的值
    :param text:
    :type text:
    :param map:
    :type map:  dict
    :return:
    :rtype:
    """
    assert isinstance(adict, dict)
    rx = re.compile('|'.join(adict.keys()))

    def replace_text_map(text):
        if text:
            return rx.sub(lambda m: adict.get(m.group(0), ''), text)
        else:
            return ''
    return replace_text_map


def get_cn_price(value, capital=True, prefix=False, classical=None):

    """

    人民币数字转汉字表示 Ver 0.02

    作者: qianjin(AT)ustc.edu

    版权声明:

        只要保留本代码最初作者的电子邮件即可，随便用。用得爽的话，不反对请

    作者吃一顿。

    参数:

    capital:    True   大写汉字金额

                False  一般汉字金额

    classical:  True   圆

                False  元

    prefix:     True   以'人民币'开头

                False, 无开头


    """
    # 默认大写金额用圆，一般汉字金额用元

    if classical is None:

        classical = True if capital else False

    # 汉字金额前缀

    if prefix is True:

        prefix = '人民币'

    else:

        prefix = ''

    # 汉字金额字符定义

    dunit = ('角', '分')

    if capital:

        num = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')

        iunit = [None, '拾', '佰', '仟', '万', '拾', '佰', '仟',

                 '亿', '拾', '佰', '仟', '万', '拾', '佰', '仟']

    else:

        num = ('〇', '一', '二', '三', '四', '五', '六', '七', '八', '九')

        iunit = [None, '十', '百', '千', '万', '十', '百', '千',

                 '亿', '十', '百', '千', '万', '十', '百', '千']

    if classical:

        iunit[0] = '圆' if classical else '元'

    # 转换为Decimal，并截断多余小数

    if not isinstance(value, Decimal):

        value = Decimal(value).quantize(Decimal('0.01'))

    # 转化为字符串

    s = str(value)

    if len(s) > 19:

        raise ValueError('金额太大了，不知道该怎么表达。')

    istr, dstr = s.split('.')           # 小数部分和整数部分分别处理

    istr = istr[::-1]                   # 翻转整数部分字符串

    so = []     # 用于记录转换结果

    # 零

    if value == 0:

        return prefix + num[0] + iunit[0]

    haszero = False     # 用于标记零的使用

    if dstr == '00':

        haszero = True  # 如果无小数部分，则标记加过零，避免出现“圆零整”

    # 处理小数部分

    # 分

    if dstr[1] != '0':

        so.append(dunit[1])

        so.append(num[int(dstr[1])])

    else:

        so.append('整')         # 无分，则加“整”

    # 角

    if dstr[0] != '0':

        so.append(dunit[0])

        so.append(num[int(dstr[0])])

    elif dstr[1] != '0':

        so.append(num[0])       # 无角有分，添加“零”

        haszero = True          # 标记加过零了

    # 无整数部分

    if istr == '0':

        if haszero:             # 既然无整数部分，那么去掉角位置上的零

            so.pop()

        so.append(prefix)       # 加前缀

        so.reverse()            # 翻转

        return ''.join(so)

    # 处理整数部分

    for i, n in enumerate(istr):

        n = int(n)

        if i % 4 == 0:          # 在圆、万、亿等位上，即使是零，也必须有单位

            if i == 8 and so[-1] == iunit[4]:   # 亿和万之间全部为零的情况

                so.pop()                        # 去掉万

            so.append(iunit[i])

            if n == 0:                          # 处理这些位上为零的情况

                if not haszero:                 # 如果以前没有加过零

                    so.insert(-1, num[0])       # 则在单位后面加零

                    haszero = True              # 标记加过零了

            else:                               # 处理不为零的情况

                so.append(num[n])

                haszero = False                 # 重新开始标记加零的情况

        else:                                   # 在其他位置上

            if n != 0:                          # 不为零的情况

                so.append(iunit[i])

                so.append(num[n])

                haszero = False                 # 重新开始标记加零的情况

            else:                               # 处理为零的情况

                if not haszero:                 # 如果以前没有加过零

                    so.append(num[0])

                    haszero = True

    # 最终结果

    so.append(prefix)

    so.reverse()

    return ''.join(so)

if __name__ == '__main__':
    print get_cn_price('90000000023.123')
