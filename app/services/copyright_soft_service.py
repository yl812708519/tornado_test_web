#! /usr/bin/env python
# coding:utf-8
import time
from app.commons import dateutil
from app.daos.area_process_dao import ProvinceDao
from app.daos.applicant_dao import ApplicantDao
from app.daos.copyright_soft_dao import CopyrightSoftOrderDao, CopyrightSoftOrder
from app.daos.options_dao import OptionDao
from app.services.applicant_service import ApplicantService, ApplicantBO
from app.services.ban_bos.copyright_soft import CopyrightSoftRespBO
from app.services.basebanservice import BaseBanService
from app.services.copyright_owner_service import CopyrightOwnerService
from app.services.customer_service_order_service import CustomerServiceOrderService
from app.services.order_operate_service import CopyrightOperateService
from app.services.order_status_service import OrderStatusService
from app.services.base_service import ServiceException
from app.services.options_service import OptionBO
from configs.database_builder import DatabaseBuilder
from configs.order_status_map import OrderStatusMap

__author__ = 'zhaowenlei'


class CopyrightSoftOrderService(BaseBanService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.operator = CopyrightOperateService()

    @staticmethod
    def get_by_type(t, v):
        d = {'is_publish': {1: '已发表', 2: '未发表'},
             'develop_way': {1: '独立开发', 2: '合作开发', 3: '委托开发', 4: '下达任务开发'},
             'right_get_way': {1: '原始取得', 2: '继受取得'},
             'right_range': {1: '全部', 2: '部分'},
             'soft_description': {1: '原创', 2: '修改'},
             'type': {1: '自然人', 2: '企业法人', 3: '机关法人', 4: '事业单位法人', 5: '社会团体法人', 6: '其他组织', 7: '其他'},
             'certi_type': {1: '居民身份证', 2: '军官证', 3: '护照', 4: '企业法人营业执照', 5: '组织机构代码证书', 6: '事业单位法人证书',
                            7: '社团法人证书', 8: '其他有效证件'},
             'sign_situation': {1: '本名', 2: '别名', 3: '匿名'},
             'com_type': {1: '国有企业', 2: '集体企业', 3: '私营企业', 4: '港澳台商投资企业', 5: '外商投资企业', 6: '股份有限公司'}}

        try:
            return d[t][v]
        except:
           return ''

    @staticmethod
    def get_biz_dao(session):
        """ 获得CopyrightOpusDao对象

        :param session:
        :type session:
        :return:
        :rtype:
        """
        return CopyrightSoftOrderDao(session)

    @staticmethod
    def get_data_obj(biz_type):
        """ 根据服务类型获得CopyrightOpusOrder

        :param biz_type:
        :type biz_type:
        :return CopyrightOpusOrder:
        :rtype:
        """
        return CopyrightSoftOrder()

    def detail_pay(self, order, session):
        """版权业务付款之后要更新为“等待上传申请书”的状态，并记录支付状态

        :param order:
        :type order:
        :param session:
        :type session:
        :return:
        :rtype:
        """
        order.status = OrderStatusMap.WAITE_UPLOAD
        OrderStatusService().update_order_status(order, OrderStatusMap.WAITE_UPLOAD, 0, session)
        CustomerServiceOrderService().add_cs_order(order, 'upload', order.csu_id, session)
        return order

    @staticmethod
    def get_applicant(user_id, applicant_id):
        """ 根据服user_id, applicant_id获取主体

        :param user_id:
        :type user_id:
        :param applicant_id:
        :type applicant_id:
        :return 主体对象:
        :rtype:
        """
        applicant_service = ApplicantService()
        return applicant_service.get_by_id(user_id, applicant_id)

    def get_apply_app(self, order_apps):
        for order_app in order_apps:
            if order_app['source_type'] in ('software_copyright_app'):
                return order_app

    def deal_biz(self, biz, session):
        option_dao = OptionDao(session)
        province_dao = ProvinceDao(session)
        copyright_soft_bo = CopyrightSoftRespBO(**biz.fields)
        user_id = copyright_soft_bo.user_id
        if copyright_soft_bo.applicant_id:
            applicant_bo = self.get_applicant(user_id, copyright_soft_bo.applicant_id)
        else:
            applicant_bo = ApplicantBO()
        right_ranges = option_dao.gets_by_type('RIGHT_RANGE')
        right_range_bos = [OptionBO(**right_range.fields) for right_range in right_ranges]
        copyright_soft_bo.right_ranges = right_range_bos

        if copyright_soft_bo.soft_finish_date:
            copyright_soft_bo.soft_finish_date = dateutil.timestamp_to_string(copyright_soft_bo.soft_finish_date, '%Y-%m-%d')
        else:
            copyright_soft_bo.soft_finish_date = ''
        if copyright_soft_bo.publish_date:
            copyright_soft_bo.publish_date = dateutil.timestamp_to_string(copyright_soft_bo.publish_date, '%Y-%m-%d')
        else:
            copyright_soft_bo.publish_date = ''

        if copyright_soft_bo.common_app_ids:
            copyright_soft_bo.common_app_ids = copyright_soft_bo.common_app_ids.split(',')
            copyright_soft_bo.common_app_applicants = self.gets_applicant_by_ids(session, user_id, copyright_soft_bo.common_app_ids)

        if copyright_soft_bo.is_info_finished:
            copyright_soft_bo.soft_description_title = self.get_by_type('soft_description', copyright_soft_bo.soft_description)
            copyright_soft_bo.is_publish_title = self.get_by_type('is_publish', copyright_soft_bo.is_publish)
            copyright_soft_bo.develop_way_title = self.get_by_type('develop_way', copyright_soft_bo.soft_description)
            copyright_soft_bo.right_get_way_title = self.get_by_type('right_get_way', copyright_soft_bo.right_get_way)
            copyright_soft_bo.right_range_title = self.get_by_type('right_range', copyright_soft_bo.right_range)

        copyright_soft_bo.today = dateutil.timestamp_to_string(time.time(), '%Y-%m-%d')
        copyright_soft_bo.applicant = applicant_bo

        copyright_owner_servoce = CopyrightOwnerService()
        copyright_owner = copyright_owner_servoce.get_by_biz(copyright_soft_bo.id)
        if copyright_owner.type:
            copyright_owner.type = self.get_by_type('type', int(copyright_owner.type))
        if copyright_owner.certi_type:
            copyright_owner.certi_type = self.get_by_type('certi_type', int(copyright_owner.certi_type))
        if copyright_owner.province:
            copyright_owner.province = province_dao.get_by_value(copyright_owner.province).name
        copyright_soft_bo.copyright_owner = copyright_owner

        return copyright_soft_bo

    def get_by_user_id_order_id(self, user_id, order_id):
        """ 根据服user_id, order_id获取版权订单信息

        :param user_id:
        :type user_id:
        :param order_id:
        :type order_id:
        :return 订单信息对象:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            option_dao = OptionDao(session)
            copyright_soft = CopyrightSoftOrderDao(session).get_by_order_user(user_id, order_id)
            if copyright_soft is None:
                raise ServiceException(20060, '404 not found')
            copyright_soft_bo = CopyrightSoftRespBO(**copyright_soft.fields)
            if copyright_soft_bo.applicant_id:
                applicant_bo = self.get_applicant(user_id, copyright_soft_bo.applicant_id)
            else:
                applicant_bo = ApplicantBO()
            right_ranges = option_dao.gets_by_type('RIGHT_RANGE')
            right_range_bos = [OptionBO(**right_range.fields) for right_range in right_ranges]
            copyright_soft_bo.right_ranges = right_range_bos

            if copyright_soft_bo.range_select:
                copyright_soft_bo.range_select = copyright_soft_bo.range_select.split(',')

            if copyright_soft_bo.soft_finish_date:
                copyright_soft_bo.soft_finish_date = dateutil.timestamp_to_string(copyright_soft_bo.soft_finish_date, '%Y-%m-%d')
            else:
                copyright_soft_bo.soft_finish_date = ''
            if copyright_soft_bo.publish_date:
                copyright_soft_bo.publish_date = dateutil.timestamp_to_string(copyright_soft_bo.publish_date, '%Y-%m-%d')
            else:
                copyright_soft_bo.publish_date = ''

            if copyright_soft_bo.common_app_ids:
                copyright_soft_bo.common_app_ids = copyright_soft_bo.common_app_ids.split(',')
                copyright_soft_bo.common_app_applicants = self.gets_applicant_by_ids(session, user_id, copyright_soft_bo.common_app_ids)

            if copyright_soft_bo.is_info_finished:
                copyright_soft_bo.soft_description_title = self.get_by_type('soft_description', copyright_soft_bo.soft_description)
                copyright_soft_bo.is_publish_title = self.get_by_type('is_publish', copyright_soft_bo.is_publish)
                copyright_soft_bo.develop_way_title = self.get_by_type('develop_way', copyright_soft_bo.soft_description)
                copyright_soft_bo.right_get_way_title = self.get_by_type('right_get_way', copyright_soft_bo.right_get_way)
                copyright_soft_bo.right_range_title = self.get_by_type('right_range', copyright_soft_bo.right_range)

            copyright_soft_bo.today = dateutil.timestamp_to_string(time.time(), '%Y-%m-%d')
            copyright_soft_bo.applicant = applicant_bo

            return copyright_soft_bo

    def update_applicant(self, req_bo):
        """ 更新主体

        :param req_bo:
        :type req_bo:
        :return 订单信息对象:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_soft_order_dao = CopyrightSoftOrderDao(session)
            copyright_soft = copyright_soft_order_dao.get_by_order_id(req_bo.order_id,
                                                                      req_bo.user_id)
            if copyright_soft is not None:
                self.update_confirm_able(copyright_soft, 'applicant_id')
                copyright_soft.update(req_bo.flat_attributes)
                copyright_soft_order_dao.update(copyright_soft)

    def update_info(self, req_bo):
        """更新版权基本信息

        :param req_bo:
        :type req_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_soft_order_dao = CopyrightSoftOrderDao(session)
            copyright_soft = copyright_soft_order_dao.get_by_order_id(req_bo.order_id,
                                                                      req_bo.user_id)
            self.update_confirm_able(copyright_soft, 'soft_name')
            if copyright_soft.is_info_finished is False:
                copyright_soft.is_info_finished = True
            copyright_soft.update(req_bo.flat_attributes)
            copyright_soft_order_dao.update(copyright_soft)

    def update_feature(self, req_bo):
        """更新软件特点

        :param req_bo:
        :type req_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_soft_order_dao = CopyrightSoftOrderDao(session)
            copyright_soft = copyright_soft_order_dao.get_by_order_id(req_bo.order_id,
                                                                      req_bo.user_id)
            self.update_confirm_able(copyright_soft, 'hardware_env')
            copyright_soft.update(req_bo.flat_attributes)
            copyright_soft_order_dao.update(copyright_soft)

    def update_attach(self, req_bo):
        """更新其它信息

        :param req_bo:
        :type req_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_soft_order_dao = CopyrightSoftOrderDao(session)
            copyright_soft = copyright_soft_order_dao.get_by_order_id(req_bo.order_id,
                                                                      req_bo.user_id)
            self.update_confirm_able(copyright_soft, 'source_program')
            copyright_soft.update(req_bo.flat_attributes)
            copyright_soft_order_dao.update(copyright_soft)

    @staticmethod
    def gets_applicant_by_ids(session, user_id, ids):
        applicant_dao = ApplicantDao(session)
        applicants = applicant_dao.gets_applicant_by_ids(user_id, [int(i) for i in ids])
        return [ApplicantBO(**applicant.fields) for applicant in applicants] if applicants else []