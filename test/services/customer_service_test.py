#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from app.services import customer_service

__author__ = 'wangshubin'


class CustomerServiceTest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        self.tclass = customer_service.CustomerService()   ##实例化了被测试模块中的类

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def testget_by_id(self):
        print self.tclass.get_by_id(158)
        self.assertEqual(self.tclass.get_by_id(158)["dealer_id"], 2, "第一个参数是函数,第二个参数是预期返回结果,第三个参数是错误提示信息")
        self.fail("自己添加的失败")

    def testcount_by_key(self):
        self.assertEqual(self.tclass.count_by_key(),14)

if __name__ =='__main__':
    unittest.main()