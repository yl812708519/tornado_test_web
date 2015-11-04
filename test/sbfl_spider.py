#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yanglu'

import urllib2
import re
from lxml import etree

"""
    爬取第三级商标分类的爬虫
    数据来自：http://www.sbfl.cn/

    一二级类都在一个页面上。。。
    当初写的爬虫找不到了。。。
    后来的哥们自己写个吧。。。对不住咯
"""




class Rules(object):
    def __init__(self, allow=None, follow=False, parse_func=None):
        self.allow = allow
        if follow is True:
            self.parse_func = None
        elif follow is False:
            self.parse_func = parse_func
        self.follow = follow


user_agents = ['Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)']

url = 'http://www.sbfl.cn/'


class OurSpider(object):

    start_url = url
    rules = [
        Rules(allow='show.asp\?bh=\w+', parse_func='parse_items')
    ]

    def _get_tree(self, url=None):
        if url is None:
            url = self.start_url
        request = urllib2.Request(url, headers={'User-Agent': user_agents[0]})

        html = urllib2.urlopen(request).read().decode('gbk')
        domain = 'http://' + request.origin_req_host
        tree = etree.HTML(html)
        return tree, domain

    def get_content(self):
        follow_urls = []
        tree, domain = self._get_tree()
        href_list = tree.xpath('//a/@href')
        for href in href_list:
            href = domain + '/' + href
            for rule in self.rules:
                allow = '.*' + rule.allow
                patten = re.compile(allow)
                if patten.match(href):
                    if rule.parse_func is not None:
                        method = getattr(self, rule.parse_func)
                        follow_urls.append(dict(url=href, method=method))
        self.parse(follow_urls)

    def parse(self, follow_urls):

        for follow in follow_urls:
            tree, domain = self._get_tree(follow['url'])
            method = follow['method']
            method(tree)

    def parse_items(self, tree=None):
        if tree:
            # 处理数据
            h1 = tree.xpath('/html/body/div[3]/h1/text()')
            text = tree.xpath('/html/body/div[3]/div/text()')
            parent_code = h1[0][:4]
            print '#' + parent_code
            for txt in text:
                if txt.strip():
                    items = txt.split(u'，')
                    for item in items:
                        item = item.strip()
                        endswith = item[-6:]
                        if endswith.isdigit():
                            if item.find(u'（') == 0:
                                item = item[item.index(u'）')+1:]

                            if item[-7] == 'C':
                                code = 'C'+endswith
                                name = item[:-7]
                            else:
                                code = endswith
                                name = item[:-6]
                            # id, code, name, parent_code, created_at, updated_at
                            print "value('"+code+"', '"+name+"', '"+parent_code+"'),"
                else:
                    continue



if __name__ == '__main__':
    test = OurSpider().get_content()

# url2 = 'show.asp?bh=0104'
# # request = urllib2.Request(url, headers={'User-Agent': user_agents[0]})
# # html = urllib2.urlopen(request).read().decode('gbk')
# # print html
# import re
# patten = re.compile('.*show\.asp\?bh=\w+')
# match = patten.match(url2)
# print match.group()