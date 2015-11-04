#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yanglu'

from app.thrift.gen_py.csorder.constants import *


class OrderStatusMap(object):
    """
    保证前后台统一，减少查询关键字的交互
    真正的对照表在thrift生成的constants文件中
    配置在csorder.thrift 中使用常量配置
    该类为了方便使用作对照（主要是项目里太多。。不敢改。。T-T）
    这个类可以取消掉。直接引用该文件中的对照关系
    项目中的关键字 对照
    """
    WRITE_INFO = WRITE_INFO         # 'wirte_info'
    WAIT_REVIEW = WAIT_REVIEW       # 'wait_review'
    WAIT_DELEGATE = WAIT_DELEGATE   # 'wait_delegate'
    WAIT_PAYMENT = WAIT_PAYMENT     # 'wait_payment'
    PAID = PAID                     # 'paid'
    COMPLETED = COMPLETED           # 'completed'
    INVALID = INVALID               # 'invalid'
    WAITE_UPLOAD = WAITE_UPLOAD     # 'wait_upload'
    STUFF_SEND = STUFF_SEND         # 'stuff_send'


class BaseOrderStatus(dict):
    def __init__(self, **kwargs):
        self.biz_statuses = kwargs

        iterable = {'write_info': ' 填写信息',
                    'wait_delegate': '正在代填',
                    'wait_review': ' 等待审核',
                    'wait_payment': ' 等待付款',
                    'paid': '已付款',
                    'stuff_send': '待邮寄',
                    'completed': '已完成',
                    'invalid': '已作废',
                    'wait_upload': '材料生成'}
        super(BaseOrderStatus, self).__init__(iterable, **kwargs)


class BizStatusMap(object):

    mark_reg = BaseOrderStatus(non_submit='未提交', submited='已提交',
                               send_accept='下发受理通知书', correction='补正',
                               first_correction='第一次补正', secend_correction='第二次补正',
                               notice='进入公告', reject='已部分驳回/驳回')

    copyright_app = BaseOrderStatus(accepted='版权已受理', awarded='版权已下证')

    # 商标的所有业务用的都是同一套状态
    collective_mark_reg = prove_mark_reg = reissue_reg_credential = \
        reg_col_pro_applicant = age_rec_applicant = sub_service_applicant = \
        provide_mark_reg_proof = correct_mark_reg_items = mark_transfer_apply = \
        reissue_mark_transfer = mark_reg

    art_copyright = other_copyright = software_copyright = word_copyright = copyright_app

    @classmethod
    def get_biz_status(cls, order_type, is_paid_included):
        status = getattr(cls, order_type, dict()).biz_statuses
        if is_paid_included:
            status[OrderStatusMap.PAID] = BaseOrderStatus().get(OrderStatusMap.PAID)
        return status



# if __name__ == '__main__':
#     print BizStatusMap.get_biz_status('mark_reg', False)