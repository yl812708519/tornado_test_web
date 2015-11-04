#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2011-6-12

@author: freeway
"""
from app.handlers.widgets.checkbox import CheckBoxWidget
from app.handlers.widgets.common import CommonWidget
from app.handlers.widgets.download import DownloadWidget
from app.handlers.widgets.html import HtmlSelectWidget
from app.handlers.widgets.paginate import PaginateWidget
from app.handlers.widgets.radio import RadioWidget
from app.handlers.widgets.select import SelectWidget
from app.handlers.widgets.user import UserDomainWidget, UserAvatarWidget, UserAboutWidget
from app.handlers.widgets.date import DateWidget
from app.handlers.widgets.simpleprofile import SimpleProfileWidget


class Widgets(object):
    """Widgets 只有一个widgets的属性定义好即可.
    ::
        widgets={
            'widget':CommonWidget,
            'paginate':PaginateWidget,
            'userdomain':UserDomainWidget,
            'useravatar':UserAvatarWidget,
            'userlist':UserListWidget,
            'userabout':UserAboutWidget,
            'simpleprofile':SimpleProfileWidget,
            'date':DateWidget,
            'follow':FollowWidget,
            'spacetabs':SpaceTabsWidget}

    """
    widgets = {
        'widget': CommonWidget,
        'html_select': HtmlSelectWidget,
        'select': SelectWidget,
        'radio': RadioWidget,
        'checkbox': CheckBoxWidget,
        'paginate': PaginateWidget,
        'userdomain': UserDomainWidget,
        'useravatar': UserAvatarWidget,
        'userabout': UserAboutWidget,
        'simpleprofile': SimpleProfileWidget,
        'date': DateWidget,
        'download': DownloadWidget}
