#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlencode
from tornado.web import authenticated
from app.handlers.application import BaseHandler, RestfulAPIHandler
from app.handlers.order.order import OrderDetailHandler
from app.commons.view_model import ViewModel
from app.services.mark_reg_service import MarkRegService
from app.services.business_service import BusinessService
from app.services.mark_category_item_service import MarkCategoryItemService
from app.services.ban_bos.mark_bo.mark_reg_bo import MarkApplicantBO, MarkCategoryBO, MarkInfoBO, MarkAttachBO


class MarkBizHandler(BaseHandler):
    """
    加载 商标注册，修改，变更 业务列表
    """
    def get(self, biz_type):
        mark_biz_type = 'mark_' + biz_type
        bizs = BusinessService().get_by_type(mark_biz_type)
        result = dict(bizs=ViewModel.to_views(bizs),
                      default=bizs[0],
                      biz_type=biz_type,
                      active_id=mark_biz_type,
                      is_order=False)
        self.render('ban_views/businesses.html', **result)

    def post(self, *args, **kwargs):
        """
        添加商标业务的订单和相应业务数据
        :param args:
        :param kwargs:
        :return:
        """
        user = self.current_user
        biz_type = self.get_argument('biz_type', '')
        if not user:
            # post请求的用户登录判断
            # authenticated post请求会报403
            url = self.get_login_url()
            url += "?" + urlencode(dict(next='mark/reg'))
            self.redirect(url)
            return
        detail_service = OrderDetailHandler.detail_service(biz_type)
        #  basebanservice.add
        detail_order_id = detail_service.add(user.user_id, biz_type)
        self.redirect('/order/'+str(detail_order_id))


class MarkApplicantJsonHandler(RestfulAPIHandler):
    """
    主题信息选择
    """

    @authenticated
    def post(self):
        """
        修改主体信息
        """
        user = self.current_user
        mark_bo = self.get_req_bo(MarkApplicantBO)
        # 确保共同申请人中 不包含 申请的主体id
        if mark_bo.applicant_id in mark_bo.co_applicant_ids:
            mark_bo.co_applicant_ids.remove(mark_bo.applicant_id)
        mark_service = MarkRegService()
        mark_service.update_applicant(user, mark_bo)


class MarkInfoJsonHandler(RestfulAPIHandler):
    """
    商标信息填写
    """

    @authenticated
    def post(self):
        mark_bo = self.get_req_bo(MarkInfoBO)
        user = self.get_current_user()
        MarkRegService().update_mark_info(mark_bo, user)


class MarkCategoryHandler(RestfulAPIHandler):
    """
    商标分类信息选择
    """

    @authenticated
    def post(self):
        """
        分类修改
        """
        user = self.current_user
        mark_bo = self.get_req_bo(MarkCategoryBO)
        MarkCategoryItemService().handle_category(mark_bo.category, mark_bo.itemtree, mark_bo.items)
        price = MarkRegService().update_category(mark_bo, user)
        if price:
            self.write({'result': 1, 'price': float(price)})
        else:
            self.write_success()


class MarkAttachHandler(RestfulAPIHandler):
    """
    商标附加信息
    """

    @authenticated
    def post(self):
        """

        :param mark_reg_order_id:
        :return:
        """
        mark_reg_bo = self.get_req_bo(MarkAttachBO)
        MarkRegService().update_attach(mark_reg_bo, self.current_user)
        self.write_success()
