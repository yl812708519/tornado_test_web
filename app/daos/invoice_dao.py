#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'freeway'

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, desc, func, Float
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin


class Invoice(IdMixin, CreatedAtMixin, UpdatedAtMixin, BaseModel):

    # 用户id
    user_id = Column(String(36))
    # 发票抬头
    title = Column(String(200), default='')
    # 发票编号
    invoice_num = Column(String(200), default='')
    # 发票类型(normal:增值税普通发票, special:增值税专用发票)
    invoice_type = Column(String(30), default='')
    # 开具类型(企业:company/个人:person)
    make_invoice_type = Column(String(30), default='')
    # 一般纳税人资格认证复印件
    taxpayer_certi_image = Column(String(200), default='')
    # 收件人
    recipient = Column(String(100), default='')
    # 收货地址
    delivery_address = Column(String(400), default='')
    # 联系电话
    contact_mobile = Column(String(20), default='')
    # 快递编号
    express_num = Column(String(20), default='')
    # 物流公司
    express_company = Column(String(50), default='')
    # 发票金额
    invoice_price = Column(Float, default=None)
    # 邮政编码
    postalcode = Column(String(10), default='')
    # 发票状态(preparing:待邮寄, sent:已邮寄)
    mailing_status = Column(String(30), default='preparing')
    # 发票状态 0:待开发票 1:已开发票
    invoice_status = Column(BigInteger, default=0)
    # 是否作废
    is_cancel = Column(BigInteger, default=0)


@model(Invoice)
class InvoiceDao(DatabaseTemplate):

    def count_by_user_id(self, user_id, start_time='', end_time='', mailing_status='', invoice_status='',
                         offset=0, page_size=10):
        conditions = []
        if start_time:
            conditions.append(Invoice.created_at >= start_time)
        if end_time:
            conditions.append(Invoice.created_at <= end_time)
        if mailing_status and len(mailing_status.strip()) != 0:
            conditions.append(Invoice.mailing_status == mailing_status)
        if invoice_status and len(invoice_status.strip()) != 0:
            conditions.append(Invoice.invoice_status == invoice_status)
        if user_id and len(user_id.strip()) != 0:
            conditions.append(Invoice.user_id == user_id)
        invoices = self.session.query(self.model_cls).filter(*conditions).\
            order_by(desc(self.model_cls.created_at)).limit(page_size).offset(offset).all()

        total_count = self.session.query(func.count('*')).select_from(self.model_cls).\
            filter(*conditions).scalar()

        return total_count, invoices

    def get_by_id(self, invoice_id, user_id):
        return self.session.query(self.model_cls).filter(Invoice.id == invoice_id,
                                                         Invoice.user_id == user_id).first()

    def update_invoice_by_id(self, invoice_id, user_id):
        return self.session.query(self.model_cls).filter(Invoice.id == invoice_id,
                                                         Invoice.user_id == user_id).update({'is_cancel': True, 'invoice_status': 2})