#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# thrift 服务注册 启动
#
import logging
import sys

from thrift.TMultiplexedProcessor import TMultiplexedProcessor
from app.thrift.cs_record_thrift_handler import ThriftCsRecordHandler

from app.thrift.gen_py.csorder import ThriftCSOrderService, ThriftCustomerRecordService
from app.thrift.gen_py.csorder import ThriftOrderStatusService
from app.thrift.gen_py.csorder import ThriftOrderTipService
from app.thrift.gen_py.csorder import ThriftSmsNotifyService
from app.thrift.csorder_thrift_handler import ThriftCSOrderHandler
from app.thrift.csorder_thrift_handler import ThriftOrderStatusHandler
from app.thrift.csorder_thrift_handler import ThriftOrderTipHandler
from app.thrift.csorder_thrift_handler import ThriftSmsNotifyHandler
from configs.thrift_builder import ThriftBuilder


# reload(sys)
# sys.setdefaultencoding('utf8')
# define("runmod", default='development', help="runing mod. [development|test|production]")
# define("app_name", default='None')
# tornado.options.parse_command_line()
#set run mode
# DatabaseBuilder.run_mode = options.runmod
# ThriftBuilder.run_mode = options.runmod
# MemCacheFactory.run_mode = options.runmod

def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    shutdown()


def shutdown():
    exit(0)


def start():
    multiplexed_processor = TMultiplexedProcessor()

    processor = ThriftCSOrderService.Processor(ThriftCSOrderHandler())
    multiplexed_processor.registerProcessor("csorder_service", processor)

    processor = ThriftOrderStatusService.Processor(ThriftOrderStatusHandler())
    multiplexed_processor.registerProcessor("order_status_service", processor)

    processor = ThriftOrderTipService.Processor(ThriftOrderTipHandler())
    multiplexed_processor.registerProcessor("order_tip_service", processor)

    processor = ThriftSmsNotifyService.Processor(ThriftSmsNotifyHandler())
    multiplexed_processor.registerProcessor("thrift_sms_notify", processor)

    processor = ThriftCustomerRecordService.Processor(ThriftCsRecordHandler())
    multiplexed_processor.registerProcessor("customer_record_service", processor)

    ThriftBuilder.start_server_by_name(multiplexed_processor, name='cs_order')

if __name__ == "__main__":
    start()
