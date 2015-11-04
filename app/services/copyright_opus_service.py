#! /usr/bin/env python
# coding:utf-8
import json
import time
from app.commons import dateutil
from app.daos.area_process_dao import ProvinceDao, CityDao
from app.daos.applicant_dao import ApplicantDao
from app.daos.copyright_opus_dao import CopyrightOpusOrderDao, CopyrightOpusOrder
from app.daos.options_dao import OptionDao
from app.services.ban_bos.copyright_opus import CopyrightOpusResBO, CopyrightOpusReqBO
from app.services.applicant_service import ApplicantService, ApplicantBO
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


class CopyrightOpusOrderService(BaseBanService):

    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()
        self.operator = CopyrightOperateService()

    @staticmethod
    def get_by_type(t, v):
        d = {'opus_nature': {1: '原创', 2: '改编', 3: '翻译', 4: '汇编', 5: '注释', 6: '整理', 7: '其他'},
             'right_get_way': {1: '原创', 2: '继承', 3: '承受', 4: '其他'},
             'right_ascription_way': {1: '个人作品', 2: '合作作品', 3: '法人作品', 4: '职务作品', 5: '委托作品'},
             'publish_status': {1: '已发表', 2: '未发表'},
             'right_own_state': {1: '全部', 2: '部分'},
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
        return CopyrightOpusOrderDao(session)

    def get_apply_app(self, order_apps):
        for order_app in order_apps:
            if order_app['source_type'] in ('word_copyright_app', 'art_copyright_app', 'other_copyright_app'):
                return order_app

    @staticmethod
    def get_data_obj(biz_type):
        """ 根据服务类型获得CopyrightOpusOrder

        :param biz_type:
        :type biz_type:
        :return CopyrightOpusOrder:
        :rtype:
        """
        return CopyrightOpusOrder()

    def deal_biz(self, biz, session):
        opus_copyright_bo = CopyrightOpusResBO(**biz.fields)
        option_dao = OptionDao(session)
        province_dao = ProvinceDao(session)
        user_id = opus_copyright_bo.user_id

        if opus_copyright_bo.applicant_id:
            applicant_bo = self.get_applicant(user_id, opus_copyright_bo.applicant_id)
        else:
            applicant_bo = ApplicantBO()
        right_own_selects = option_dao.gets_by_type('RIGHT_OWN_SELECT')
        right_own_select_bos = [OptionBO(**right_own_select.fields) for right_own_select in right_own_selects]
        opus_copyright_bo.right_own_selects = right_own_select_bos

        if opus_copyright_bo.opus_finish_date:
            opus_copyright_bo.opus_finish_date = dateutil.timestamp_to_string(opus_copyright_bo.opus_finish_date, '%Y-%m-%d')
        if opus_copyright_bo.first_publish_date:
            opus_copyright_bo.first_publish_date = dateutil.timestamp_to_string(opus_copyright_bo.first_publish_date, '%Y-%m-%d')
        if opus_copyright_bo.common_app_ids:
            opus_copyright_bo.common_app_ids = opus_copyright_bo.common_app_ids.split(',')
            opus_copyright_bo.common_app_applicants = self.gets_applicant_by_ids(session, user_id, opus_copyright_bo.common_app_ids)

        if opus_copyright_bo.is_info_finished:
            opus_copyright_bo.opus_nature_title = self.get_by_type('opus_nature', opus_copyright_bo.opus_nature)
            opus_copyright_bo.publish_status_title = self.get_by_type('publish_status', opus_copyright_bo.publish_status)
        if opus_copyright_bo.is_des_finished:
            opus_copyright_bo.right_get_way_title = self.get_by_type('right_get_way', opus_copyright_bo.right_get_way)
            opus_copyright_bo.right_ascription_way_title = self.get_by_type('right_ascription_way', opus_copyright_bo.right_ascription_way)
            opus_copyright_bo.right_own_state_title = self.get_by_type('right_own_state', opus_copyright_bo.right_own_state)

        if opus_copyright_bo.opus_sample:
            s = opus_copyright_bo.opus_sample.split('.')
            if s[1] in ['jpg', 'png', 'jpeg']:
                opus_copyright_bo.flag = 1
            else:
                opus_copyright_bo.flag = 2
        copyright_owner_servoce = CopyrightOwnerService()
        copyright_owner = copyright_owner_servoce.get_by_biz(opus_copyright_bo.id)
        if copyright_owner.type:
            copyright_owner.type = self.get_by_type('type', int(copyright_owner.type))
        if copyright_owner.certi_type:
            copyright_owner.certi_type = self.get_by_type('certi_type', int(copyright_owner.certi_type))
        if copyright_owner.province:
            copyright_owner.province = province_dao.get_by_value(copyright_owner.province).name
        if copyright_owner.sign_situation:
            copyright_owner.sign_situation = self.get_by_type('sign_situation', int(copyright_owner.sign_situation))
        opus_copyright_bo.copyright_owner = copyright_owner
        opus_copyright_bo.applicant = applicant_bo
        if opus_copyright_bo.opus_type:
            opus_type = option_dao.get_by_type_value('COPYRIGHT_TYPE', opus_copyright_bo.opus_type)
            opus_copyright_bo.opus_type = opus_type
        return opus_copyright_bo

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
            opus_copyright = CopyrightOpusOrderDao(session).get_by_order_user(user_id, order_id)
            if opus_copyright is None:
                raise ServiceException(20060, '404 not found')
            opus_copyright_bo = CopyrightOpusResBO(**opus_copyright.fields)
            if opus_copyright_bo.applicant_id:
                applicant_bo = self.get_applicant(user_id, opus_copyright_bo.applicant_id)
            else:
                applicant_bo = ApplicantBO()
            right_own_selects = option_dao.gets_by_type('RIGHT_OWN_SELECT')
            right_own_select_bos = [OptionBO(**right_own_select.fields) for right_own_select in right_own_selects]
            opus_copyright_bo.right_own_selects = right_own_select_bos

            if opus_copyright_bo.right_own_select:
                opus_copyright_bo.right_own_select = opus_copyright_bo.right_own_select.split(',')
            if opus_copyright_bo.opus_finish_date:
                opus_copyright_bo.opus_finish_date = dateutil.timestamp_to_string(opus_copyright_bo.opus_finish_date, '%Y-%m-%d')
            if opus_copyright_bo.first_publish_date:
                opus_copyright_bo.first_publish_date = dateutil.timestamp_to_string(opus_copyright_bo.first_publish_date, '%Y-%m-%d')
            if opus_copyright_bo.common_app_ids:
                opus_copyright_bo.common_app_ids = opus_copyright_bo.common_app_ids.split(',')
                opus_copyright_bo.common_app_applicants = self.gets_applicant_by_ids(session, user_id, opus_copyright_bo.common_app_ids)

            if opus_copyright_bo.is_info_finished:
                opus_copyright_bo.opus_nature_title = self.get_by_type('opus_nature', opus_copyright_bo.opus_nature)
                opus_copyright_bo.publish_status_title = self.get_by_type('publish_status', opus_copyright_bo.publish_status)
            if opus_copyright_bo.is_des_finished:
                opus_copyright_bo.right_get_way_title = self.get_by_type('right_get_way', opus_copyright_bo.right_get_way)
                opus_copyright_bo.right_ascription_way_title = self.get_by_type('right_ascription_way', opus_copyright_bo.right_ascription_way)
                opus_copyright_bo.right_own_state_title = self.get_by_type('right_own_state', opus_copyright_bo.right_own_state)

            if opus_copyright_bo.opus_sample:
                s = opus_copyright_bo.opus_sample.split('.')
                if s[1] in ['jpg', 'png', 'jpeg']:
                    opus_copyright_bo.flag = 1
                else:
                    opus_copyright_bo.flag = 2

            opus_copyright_bo.today = dateutil.timestamp_to_string(time.time(), '%Y-%m-%d')
            opus_copyright_bo.applicant = applicant_bo
            return opus_copyright_bo

    def update_applicant(self, copyright_opus_applicant_req_bo):
        """ 更新主体

        :param copyright_opus_applicant_req_bo:
        :type copyright_opus_applicant_req_bo:
        :return 订单信息对象:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_opus_order_dao = CopyrightOpusOrderDao(session)
            copyright_opus = copyright_opus_order_dao.get_by_order_id(copyright_opus_applicant_req_bo.order_id,
                                                                      copyright_opus_applicant_req_bo.user_id)
            if copyright_opus is not None:
                self.update_confirm_able(copyright_opus, 'applicant_id')
                copyright_opus.update(copyright_opus_applicant_req_bo.flat_attributes)
                copyright_opus_order_dao.update(copyright_opus)

    def update_info(self, copyright_opus_info_bo):
        """更新版权基本信息

        :param copyright_opus_info_bo:
        :type copyright_opus_info_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_opus_order_dao = CopyrightOpusOrderDao(session)
            copyright_opus = copyright_opus_order_dao.get_by_order_id(copyright_opus_info_bo.order_id,
                                                                      copyright_opus_info_bo.user_id)
            if copyright_opus is not None:
                if int(copyright_opus_info_bo.publish_status) == 2:
                    copyright_opus_info_bo.first_publish_date = ''
                    copyright_opus_info_bo.first_publish_country = ''
                    copyright_opus_info_bo.first_publish_city = ''
                if copyright_opus_info_bo.opus_finish_date:
                    copyright_opus_info_bo.opus_finish_date = dateutil.string_to_timestamp(copyright_opus_info_bo.
                                                                                           opus_finish_date[0:10])
                if int(copyright_opus_info_bo.publish_status) == 0 and copyright_opus_info_bo.first_publish_date:
                    copyright_opus_info_bo.first_publish_date = dateutil.string_to_timestamp(copyright_opus_info_bo.
                                                                                             first_publish_date[0:10])
                self.update_confirm_able(copyright_opus, 'opus_name')
                if copyright_opus.is_info_finished is False:
                    copyright_opus.is_info_finished = True
                copyright_opus.update(copyright_opus_info_bo.flat_attributes)
                copyright_opus_order_dao.update(copyright_opus)

    def update_att(self, copyright_opus_att_bo):
        """更新其它信息

        :param copyright_opus_att_bo:
        :type copyright_opus_att_bo:
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            copyright_opus_order_dao = CopyrightOpusOrderDao(session)
            copyright_opus = copyright_opus_order_dao.get_by_order_id(copyright_opus_att_bo.order_id,
                                                                      copyright_opus_att_bo.user_id)
            if copyright_opus is not None:
                copyright_opus.update(copyright_opus_att_bo.flat_attributes)
                self.update_confirm_able(copyright_opus, 'opus_purpose')
                if copyright_opus.is_des_finished is False:
                    copyright_opus.is_des_finished = True
                copyright_opus_order_dao.update(copyright_opus)

    @staticmethod
    def gets_applicant_by_ids(session, user_id, ids):
        applicant_dao = ApplicantDao(session)
        applicants = applicant_dao.gets_applicant_by_ids(user_id, [int(i) for i in ids])
        return [ApplicantBO(**applicant.fields) for applicant in applicants] if applicants else []