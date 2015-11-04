#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.thrift.gen_py.csorder import ThriftCSOrderService
from app.thrift.gen_py.csorder.ttypes import Extest

from configs.thrift_builder import ThriftBuilder

__author__ = 'wangshubin'


def abc():

    party_client = ThriftBuilder.get_client("csorder_service", ThriftCSOrderService)
    # ps = party_client.gets_for_review(offset=0, count=10)
    # print ps
    party_client.get_for_workbench(1, '2', '3', 0, 10)


if __name__ == "__main__":

    # party_client = ThriftBuilder.get_client("csorder_service", ThriftCSOrderService)
    # ps = party_client.gets_for_review(offset=0, count=10)
    # print ps
    try:
        abc()
    except Extest, e:
        print e.errorCode
        print e.message
    # print ps.content
    # ps = party_client.delete_party('Mj')
    # print ps
    # comment_client = ThriftBuilder.get_client("comment_service", CommentService)
    # print comment_client.gets_for_review(1, 100)
    # print comment_client.deleted('134', 'post', 312)
    # party_post_client = ThriftBuilder.get_client("party_post_service", PartyPostService)
    # party_posts = party_post_client.gets_for_review(0, 100)
    # print party_posts
    # print type(party_posts[0])
    # print party_post_client.deleted(312, '3e68cf35-f088-4f0e-ae75-36ce2d067481')