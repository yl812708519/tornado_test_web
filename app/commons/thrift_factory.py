#!/usr/bin/env python
# -*- coding: utf-8 -*-
from thrift.transport import TTransport
from thrift.transport.TSocket import TSocket

__author__ = 'freeway'


class ThriftClientFactory(object):


    @classmethod
    def get_transport(cls, host, port):
        socket = TSocket(host, port)
        transport = TTransport.TBufferedTransport(socket)

        return transport
