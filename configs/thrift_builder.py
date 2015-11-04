#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import socket
import logging
from thrift.protocol import TBinaryProtocol
# from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol
from thrift.protocol.TMultiplexedProtocol import TMultiplexedProtocol
import yaml
from app.commons.thrift_factory import ThriftClientFactory
from configs.settings import Settings

from thrift.server import TServer
from thrift.transport import TSocket, TTransport

__author__ = 'freeway'


class ThriftBuilder(object):

    _thrifts_config = None
    run_mode = 'development'
    _transports = {}

    @classmethod
    def _get_thrifts_config_by_name(cls, name='default'):
        if cls._thrifts_config is None:
            with file(os.path.join(Settings.SITE_ROOT_PATH, 'configs', 'thrifts.yaml'), 'r') as file_stream:
                cls._thrifts_config = yaml.load(file_stream).get(cls.run_mode)
        thrifts_config = cls._thrifts_config.get(name)
        return thrifts_config

    @classmethod
    def _get_transport_by_name(cls, name):
        thrifts_config = cls._get_thrifts_config_by_name(name)
        return ThriftClientFactory.get_transport(thrifts_config['host'], thrifts_config['port'])

    # 用于调用inc查询客服订单列表、 判断客服代填，审核订单 权限
    # 以下为服务端代码
    @classmethod
    def start_server_by_name(cls, multiplexed_processor, name='default'):
        thrifts_config = cls._get_thrifts_config_by_name(name)
        port = thrifts_config['port']
        if cls._is_port_free(port):
            transport = TSocket.TServerSocket(port=port)
            tfactory = TTransport.TBufferedTransportFactory()
            pfactory = TBinaryProtocol.TBinaryProtocolFactory()
            server = TServer.TThreadedServer(multiplexed_processor, transport, tfactory, pfactory)
            print 'Starting the thrift server at port ', port, '...'
            server.serve()
        else:
            logging.info("thrift port is not free. Port:"+str(port) + "...maybe thrift server is running :)")

    @staticmethod
    def _is_port_free(port):
        s = socket.socket()
        s.settimeout(0.5)
        try:
            return s.connect_ex(('localhost', port)) != 0
        finally:
            s.close()

    @classmethod
    def get_client(cls, service_name, service, name="cs_order"):
        """

        :return: SearchService.Client
        """
        old_transport = cls._transports.get(name)
        if old_transport is not None:
            old_transport.close()
        transport = cls._get_transport_by_name(name)
        cls._transports[name] = transport
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        protocol = TMultiplexedProtocol(protocol, service_name)
        service_client = service.Client(protocol)
        transport.open()
        return service_client


if __name__ == "__main__":

    client = ThriftBuilder.get_search_service_client()
    pageResult = client.search("select id from support_project_tags where is_deleted=0 order by id desc", 0, 2)
    print pageResult.results
    print pageResult.pageCount
    print pageResult.total
    print pageResult.pageSize
