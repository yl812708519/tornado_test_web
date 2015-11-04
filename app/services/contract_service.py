#! /usr/bin/evt python
# -*- coding:utf-8 -*-


__author__ = 'yanglu'

from tornado.web import HTTPError
from app.commons.biz_model import BizModel, Attribute
from configs.database_builder import DatabaseBuilder
from app.services.base_service import BaseService
from app.daos.contract_dao import ContractDao


class ContractBO(BizModel):
    id = Attribute('')
    contract = Attribute('')
    biz_name = Attribute('')
    contract_name = Attribute('')
    seal_demand = Attribute('')
    part_num = Attribute('')
    remark = Attribute('')
    is_download_able = Attribute('')


class ContractService(BaseService):

    """
    数据库中合同存储分为三级
    可以通过biz_name单独存储这个合同和业务的对应
    也可以通过group_ + business.type 来存储同组公用的合同
    最宽泛的存储方式是通过biz_bo中的base_type 存储(商标，版权共有的)
    """


    def __init__(self):
        self._default_db = DatabaseBuilder.get_default_db_instance()

    def gets_by_biz_name(self, biz_name, biz_group, base_type):
        """

        :param biz_name: 业务名
        :type biz_name:string
        :param biz_group: 业务组名 Business.type
        :type biz_group:
        :param base_type: 业务基础类型
        :type base_type: mark/copyright/patent
        :return:
        :rtype:
        """
        with self.create_session(self._default_db) as session:
            contracts = ContractDao(session).gets_by_biz_name(biz_name, 'group_'+biz_group, base_type)
            return [ContractBO(**contract.fields) for contract in contracts]

    def get_dict_by_biz_name(self, biz_name, biz_group, base_type):
        with self.create_session(self._default_db) as session:
            contracts = ContractDao(session).gets_by_biz_name(biz_name, 'group_'+biz_group, base_type)
            inst_dict = dict()
            for instance in contracts:
                inst_dict[instance.contract] = instance.fields
            return inst_dict
