#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.handlers.monitor import MonitorOkHandelr
from app.handlers.copyright.copyright import CopyrightBizHandler
from app.handlers.copyright.copyright_opus import CopyrightOpusOrderInfoHandler, CopyrightOpusOrderAttaHandler, \
    CopyrightOpusOrderApplicantHandler
from app.handlers.copyright.copyright_soft import CopyrightSoftOrderApplicantHandler, CopyrightSoftOrderFeatureHandler, \
    CopyrightSoftOrderInfoHandler, \
    CopyrightSoftOrderAttachHandler

from app.handlers.demo.demo import DemoHandler, ApplicantBuysHandler, ApplicantSalesHandler, SettingsHandler, \
    ChangePwdHandler

# from app.handlers.demo.seminar import PatentHandler, TrademarkHandler, Project_applicationHandler
from app.handlers.demo.upload_file import AttachmentUpload
from app.handlers.example import ExampleHandler
from app.handlers.home import HomeHandler, AboutHandler, AgreementHandler, LawHandler, SecretHandler, StaticHomeHandler, \
    MarkServiceHandler, AppServiceHandler
from app.handlers.iframeupload import IFrameUploadHandler

from app.handlers.options import OptionJsonHandler
from app.handlers.password import PasswordResetHandler, PasswordResetLoginHandler, PasswordCheckCodeHandler, \
    PasswordCheckCodeAPIHandler, PasswordSendSmsMsgAPIHandler

from app.handlers.profile.password import PasswordChangeHandler, PasswordJsonHandler

from app.handlers.session import SessionNewHandler, SessionHandler, AccountCheckAPIHandler
from app.handlers.captcha import CaptchaHandler

from app.handlers.profile.profile import ProfileHandler
from app.handlers.signup import SignUpHandler, SignUpPasswordHandler, \
    SignUpAPIHandler, SignUpSendSmsMsgAPIHandler
from app.handlers.site_statistics import SiteStatisticHandler


# 36ban  业务handler

from app.handlers.address.delivery_address import DeliveryAddressHandler, DeliveryAddressesHandler
from app.handlers.applicant.applicant import ApplicantNewHandler, ApplicantHandler, ApplicantsHandler, ApplicantSubmitHandler
from app.handlers.invoice.invoice import InvoiceHandler, InvoicesHandler, InvoiceDetailHandler, InvoiceDemandHandler, \
    InvoiceCancelHandler, InvoiceSubmitHandler
from app.handlers.invoice.invoice_basic import InvoiceBasicNewHandler, InvoiceBasicDetailHandler, InvoiceBasicSubmitHandler

from app.handlers.mark.mark_reg import MarkApplicantJsonHandler, MarkInfoJsonHandler, MarkAttachHandler, \
    MarkCategoryHandler, MarkBizHandler
from app.handlers.mark.mark_reg_apply import MarkRegApplyinfoHandler, \
    MarkRegApplyMainHandler
from app.handlers.mark.mark_change import MarkChangeApplicantJsonHandler, MarkChangeInfoJsonHandler, \
    MarkChangeAttachHandler
from app.handlers.mark.mark_forecast import MarkForecastHandler, UserForecastHandler
from app.handlers.mark.mark_catogory import MarkCategoryJsonHandler
from app.handlers.order.order import OrderDetailHandler, OrderDelegateHandler, OrderConfirmHandler, \
    OrderTrashHandler, OrderStatusHandler
from app.handlers.order.order_pay import OrderPayHandler, OrderPayNotifyHandler, PayTestHandler
from app.handlers.order.user_order import UserOrdersHandler
from app.handlers.order.order_contract import OrderContractsHandler
from app.handlers.contract import ContractHandler, ContractDownloadHandler

from app.handlers.mark.mark_transfer import MarkTrasferApplicantHandler, \
    MarkTrasferBizHandler, MarkTransferCommonHandler


class Routes(object):
    """url路由配置信息.
    for example::
        HANDLERS = [
            (r"/", HomeHandler),
            (r"/archive", ArchiveHandler),
            (r"/feed", FeedHandler),
            (r"/entry/([^/]+)", EntryHandler),
            (r"/compose", ComposeHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
        ]
    """

    _handlers = None
    _bingo_handlers = None
    _ban_handlers = None

    @classmethod
    def get_handlers(cls):
        if cls._handlers is None:
            cls._handlers = cls.get_bingo_handlers() + cls.get_ban_handlers()
        return cls._handlers

    @classmethod
    def get_bingo_handlers(cls):
        if cls._bingo_handlers is None:
            cls._bingo_handlers = \
                [
                    (r"/example", ExampleHandler),
                    (r"/", HomeHandler),
                    (r"/iframe_upload", IFrameUploadHandler),
                    (r"/demo/demo", DemoHandler),

                    (r"/home/index", HomeHandler),
                    # 静态页面
                    (r"/home/about", AboutHandler),
                    (r"/home/agreement", AgreementHandler),
                    (r"/home/law", LawHandler),
                    (r"/home/secret", SecretHandler),

                    (r"/(customer|banner_activity|advantage|about|404|500|error)", StaticHomeHandler),

                    # (r"/seminar/patent", PatentHandler),
                    # (r"/seminar/trademark", TrademarkHandler),
                    #
                    # (r"/seminar/registration", RegistrationHandler),
                    # (r"/seminar/project_application", Project_applicationHandler),

                    # 用户中心
                    (r"/user/profile", ProfileHandler),
                    # 注册
                    (r"/signup", SignUpHandler),
                    (r"/signup/password", SignUpPasswordHandler),
                    (r"/signup.json", SignUpAPIHandler),
                    (r"/signup/send_sms_msg.json", SignUpSendSmsMsgAPIHandler),
                    (r"/captcha.jpg", CaptchaHandler),
                    # 登录
                    (r"/session", SessionHandler),
                    (r"/session/new", SessionNewHandler),
                    (r"/account/check.json", AccountCheckAPIHandler),
                    (r"/password/check_code", PasswordCheckCodeHandler),
                    (r"/password/send_sms_msg.json", PasswordSendSmsMsgAPIHandler),  # 发送验证码
                    (r"/password/check_code.json", PasswordCheckCodeAPIHandler),
                    (r"/password/reset", PasswordResetHandler),  # 密码重置
                    (r"/password/reset/login", PasswordResetLoginHandler),  # 密码重置登录
                    (r"/user/password", PasswordChangeHandler),  # 修改密码
                    (r"/password.json", PasswordJsonHandler),

                    # demo 商标出售 求购  专利出售 求购
                    (r"/patent_applicant_buys", ApplicantBuysHandler),
                    (r"/patent_applicant_sales", ApplicantSalesHandler),
                    (r"/personalSet", SettingsHandler),
                    (r"/change_word", ChangePwdHandler),

                    # options 通用下拉数据ajax获取数据
                    (r"/option.json", OptionJsonHandler),

                    # 测试上传文件demo
                    (r'/demo/upload_file.json', AttachmentUpload),

                ]
        return cls._bingo_handlers

    @classmethod
    def get_ban_handlers(cls):
        if cls._ban_handlers is None:
            cls._ban_handlers = \
                [


                    (r"/user/orders", UserOrdersHandler),  # 用户订单列表
                    (r"/user/forecast", UserForecastHandler),  # 用户订单列表

                    (r"/mark/(reg|cha|transfer)", MarkBizHandler),  # 选择商标注册服务
                    # (r"/mark/reg/confirm", MarkRegOrderHandler),  # 选择商标注册服务
                    (r"/mark/reg/forecast", MarkForecastHandler),  # 商标预判页面
                    (r"/mark/reg/applicant", MarkApplicantJsonHandler),  # 选择主体(预判通过后申请的)
                    (r"/mark/reg/info", MarkInfoJsonHandler),  # 输入商标信息(专家预判商标信息填写)
                    (r"/mark/reg/category", MarkCategoryHandler),  # 商标分类选择
                    (r"/mark/category.json", MarkCategoryJsonHandler),  # 商标分类选择
                    (r"/mark/reg/attach", MarkAttachHandler),  # 商标分类选择

                    (r"/mark/apply/info", MarkRegApplyinfoHandler),
                    (r"/mark/apply/main", MarkRegApplyMainHandler),
                    # (r"/mark/apply/confirm", MarkRegApplyOrderHandler),

                    (r"/mark/transfer/applicant", MarkTrasferApplicantHandler),  # 商标转让 主体信息 表单提交
                    (r"/mark/transfer/biz_info", MarkTrasferBizHandler),  # 商标转让 业务信息
                    (r"/mark/transfer/common", MarkTransferCommonHandler),  # 商标转让 商标共有人
                    # (r"/mark/transfer/confirm", MarkTransferOrderHandler),


                    (r"/order/(\d+)", OrderDetailHandler),  # 订单详情页
                    (r"/order/status/(\d+)", OrderStatusHandler),  # 订单详情页
                    (r"/order/pay/(alipay|wxpay)", OrderPayHandler),  # 订单付款页
                    (r"/pay/test", PayTestHandler),  # 订单付款页
                    (r"/order/trash", OrderTrashHandler),  # 放入垃圾箱，申请代填
                    (r"/order/delegated", OrderDelegateHandler),  # 申请代填
                    (r"/order/confirm", OrderConfirmHandler),  # 订单审核
                    (r"/pay/notify/(alipay|wxpay)", OrderPayNotifyHandler),  # 支付回调
                    (r"/order/contracts/(\d+)", OrderContractsHandler),  # 合同/材料列表
                    (r"/contract/detail", ContractHandler),  # 合同预览

                    (r"/contract/download", ContractDownloadHandler),  # 合同下载
                    # 主体申
                    (r"/applicant/new", ApplicantNewHandler),  # 添加主体
                    (r"/applicant/submit", ApplicantSubmitHandler),
                    (r"/applicant/(\d+)/edit", ApplicantNewHandler),  # 修改主体
                    (r"/applicant/(\d+)/detail", ApplicantHandler),  # 主体详情
                    (r"/user/applicants", ApplicantsHandler),  # 主体列表
                    # 发票
                    (r"/invoice_basic/new", InvoiceBasicNewHandler),  # 发票信息管理添加
                    (r"/invoice_basic/submit", InvoiceBasicSubmitHandler),
                    (r"/invoice_basic/(\d+)/change", InvoiceBasicNewHandler),  # 发票信息管理修改
                    (r"/invoice_basic/detail", InvoiceBasicDetailHandler),  # 发票基本信息详情
                    (r"/invoice", InvoiceHandler),  # 获取发票添加页
                    (r"/invoice/submit", InvoiceSubmitHandler),  # 提交发票数据
                    (r"/invoices", InvoicesHandler),  # 发票列表
                    (r"/invoice/(\d+)/detail", InvoiceDetailHandler),  # 已开发票详情
                    (r"/invoice/demands", InvoiceDemandHandler),  # 发票索取列表
                    (r"/invoice/cancel", InvoiceCancelHandler),  # 发票作废

                    # 地址管理
                    (r"/delivery_address", DeliveryAddressHandler),  # 添加，删除地址
                    (r"/delivery_addresses", DeliveryAddressesHandler),  # 地址列表
                    # 商标变更
                    (r"/mark/change/applicant", MarkChangeApplicantJsonHandler),  # 商标变更的基本信息
                    (r"/mark/change/info", MarkChangeInfoJsonHandler),  # 商标附加信息
                    (r"/mark/change/attach", MarkChangeAttachHandler),  # 商标分类修改
                    # (r"/mark/change/category", MarkChangeCategoryHandler),

                    (r"/mark/service", MarkServiceHandler),  # 商标服务
                    (r"/app/service", AppServiceHandler),  # 运用服务

                    (r"/ok", MonitorOkHandelr),
                    (r"/site/statistic", SiteStatisticHandler),
                    (r"/copyright/(opus|soft)", CopyrightBizHandler),  # 版权服务index页
                    (r"/copyright/opus/applicant", CopyrightOpusOrderApplicantHandler),
                    (r"/copyright/opus/info", CopyrightOpusOrderInfoHandler),
                    (r"/copyright/opus/att", CopyrightOpusOrderAttaHandler),
                    (r"/copyright/soft/applicant", CopyrightSoftOrderApplicantHandler),
                    (r"/copyright/soft/info", CopyrightSoftOrderInfoHandler),
                    (r"/copyright/soft/feature", CopyrightSoftOrderFeatureHandler),
                    (r"/copyright/soft/att", CopyrightSoftOrderAttachHandler),
                ]
        return cls._ban_handlers

