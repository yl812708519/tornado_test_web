#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2011-6-20

@author: willian.huw
"""
from app.handlers.widgets.widget import Widget


class PaginateWidget(Widget):
    def render(self, page=1, total_count=0, url='',
               per_page_size=15, show_last_page=False, show_page_count=False,
               show_page_nav=True, place_holder='(pg)'):
        output = ""
        prefix = ""
        suffix = ""
        index = url.index(place_holder)
        if index > -1:
            prefix = url[0:index]
            pos = index + len(place_holder)
            if pos < len(url):
                suffix = url[pos:]
        else:
            return url
        total_page = int(total_count / per_page_size) + (0 if total_count % per_page_size == 0 else 1)

        if show_page_count:
            output += u"共" + str(total_page) + u"页<span class=\"pipe\">|</span>"

        if page > 1:
            output += u" <a href='" + prefix + str(page - 1) + suffix + \
                      u"' class='prev_page' rel='prev start'>&laquo; 上一页</a>"

        if show_page_nav:
            if page - 1 > 5:
                output += u" <a href='" + prefix + '1' + suffix + u"'>[1]</a>"
                if page - 1 > 6:
                    output += "..."
            for i in range(page - 5, page):
                if i <= 0:
                    continue
                output += "<a href='" + prefix + str(i) + suffix + "'>[" + str(i) + "]</a>"
            output += " <strong>" + str(page) + "</strong>"
            for i in range(page + 1, total_page):
                if i >= page + 5:
                    break
                output += " <a href='" + prefix + str(i) + suffix + "'>[" + str(i) + "]</a>"
            if total_page - page > 5:
                output += "..."
            if show_last_page and total_page - page >= 5:
                output += " <a href='" + prefix + str(total_page) + suffix + "'>[" + str(total_page) + "]</a>"
        if page < total_page:
            output += u" <a href='" + prefix + str(page + 1) + suffix + \
                      u"' class='next_page' rel='next'>下一页 &raquo;</a>"
        return output