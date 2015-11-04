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


if __name__ == '__main__':
    import os
    from tornado.template import Loader

    font_file_path = os.path.join('/Users/yanglu/workspace/python/www-yestar-web/', 'configs', 'fonts', 'Microsoft_vista_yahei.ttf')
    pdfmetrics.registerFont(TTFont('yahei', font_file_path))

    fonts.addMapping('song', 0, 0, 'song')
    fonts.addMapping('song', 0, 1, 'song')
    DEFAULT_FONT['helvetica'] = 'yahei'
    xhtml2pdf.reportlab_paragraph.Paragraph.wrap = wrap
    loader = Loader('/Users/yanglu/workspace/python/www-yestar-web/app/views/ban_views/contract/copyright')
    t = loader.load('opus_register.html')
    pisaDocument(t.generate(font=font_file_path), open('test.pdf', 'w+'))