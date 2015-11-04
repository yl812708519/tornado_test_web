#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import time
import signal
import thread
from app.commons.memcache_factory import MemCacheFactory
from app.services.oss_upload_service import OssUploadService
from configs import thrift_application
from configs.database_builder import DatabaseBuilder

from configs.routes import Routes
from configs.settings import Settings
from configs.thrift_builder import ThriftBuilder
from configs.widgets import Widgets
from tornado.options import define, options
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import sys


reload(sys)
sys.setdefaultencoding('utf8')
define("port", default=8888, help="Web application's port", type=int)
define("runmod", default='development', help="runing mod. [development|test|production]")
define("app_name", default='None')

MAX_WAIT_SECONDS_BEFORE_SHUTDOWN = 3


def sig_handler(sig, frame):
    logging.warning('Caught signal: %s', sig)
    tornado.ioloop.IOLoop.instance().add_callback(shutdown)


def shutdown():
    logging.info('Stopping http server')
    http_server.stop()
    logging.info('Will shutdown in %s seconds ...', MAX_WAIT_SECONDS_BEFORE_SHUTDOWN)
    io_loop = tornado.ioloop.IOLoop.instance()

    deadline = time.time() + MAX_WAIT_SECONDS_BEFORE_SHUTDOWN

    def stop_loop():
        now = time.time()
        if now < deadline and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 1, stop_loop)
        else:
            io_loop.stop()
            logging.info('Web Application Is Shutdown')

    # shut down thrift
    stop_loop()


def main():

    tornado.options.parse_command_line()
    settings = Settings.settings()

    # set run mode
    DatabaseBuilder.run_mode = options.runmod
    ThriftBuilder.run_mode = options.runmod
    OssUploadService.run_mode = options.runmod
    MemCacheFactory.run_mode = options.runmod
    settings["ui_modules"] = Widgets.widgets
    handlers = Routes.get_handlers()
    # public dir routes
    handlers = list(handlers or [])
    # file_list = [os.path.normcase(f) for f in os.listdir(public_path)]
    # for public_sub_dir in file_list:
    #     if os.path.isfile(os.path.join(public_path, public_sub_dir)):
    #         handlers = [(r"/("+public_sub_dir+r")",
    #                      StaticFileHandler,
    #                      dict(path=public_path))] + handlers
    #     else:s
    #         handlers = [(r"/"+public_sub_dir+"/(.*)",
    #                      StaticFileHandler,
    #                      dict(path=public_path+r'/'+public_sub_dir+r'/'))] + handlers

    application = tornado.web.Application(handlers=handlers, **settings)

    global http_server
    http_server = tornado.httpserver.HTTPServer(application)
    
    logging.info("Web application is running. Port:"+str(options.port))
    http_server.listen(options.port)

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    thread.start_new_thread(thrift_application.start, ())

    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
