#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wangshubin'
import os
import MySQLdb

import yaml

from configs.settings import Settings


"""
1 自动创建数据库表
2 自动生成对应dao
3 自动生成对应service
4
"""


class AutoCode(object):
    def __init__(self):
        file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/databases.yaml'), 'r')
        yml = yaml.load(file_stream)
        runmod = "development"
        databases_config = yml.get(runmod)
        config = databases_config["yestarbops"]
        # 建立和数据库系统的连接
        conn = MySQLdb.connect(host=config.get('host'), user=config.get('username'), passwd=config.get('password'),
                               charset=config.get('encoding'))
        conn.select_db(config.get('database'))
        self.conn = conn

    def create_table(self, **kwargs):
        """
        创建数据库表，默认5个字段：id, created_at, updated_at, operator_id, is_deleted

        :param kwargs:
        """
        drop_table_sql = "DROP TABLE IF EXISTS "+kwargs["table_name"]
        create_table_sql = """
                            CREATE TABLE  """+kwargs["table_name"]+""" (
                              id INT NOT NULL AUTO_INCREMENT,
                              """+','.join(kwargs['columns'])+""",
                              created_at BIGINT NOT NULL,
                              updated_at BIGINT NOT NULL,
                              operator_id BIGINT NOT NULL,
                              is_deleted BIGINT DEFAULT 0,
                              PRIMARY KEY (id))
        """
        print create_table_sql
        cursor = self.conn.cursor()
        #执行SQL
        cursor.execute(drop_table_sql)
        result = cursor.execute(create_table_sql)
        print result
        cursor.close()

    def create_dao(self,**kwargs):

        """
        创建dao.py文件，默认5个基本方法。
        :param kwargs:
        """
        table_name = kwargs["table_name"]
        file_dir = kwargs["file_dir"]
        tns = table_name.split("_")
        dao_name = ""
        for tn in tns:
            dao_name+=tn.capitalize()
        cursor = self.conn.cursor()
        #执行SQL 获取所有字段信息
        cursor.execute("select * from "+kwargs["table_name"])
        base_gets_sql ="""SELECT \n"""
        columns = list()
        des_len = len(cursor.description)
        for index,col in enumerate(cursor.description):  #字段信息
            columns.append(col[0])
            if index==des_len-1:
                base_gets_sql+=' '*24+col[0]+"\n"
            else:
                base_gets_sql+=' '*24+col[0]+",\n"
        base_gets_sql+="""                     FROM """+table_name
        gets_sql=base_gets_sql+"""\n                     WHERE is_deleted=0"""
        get_by_id_sql = base_gets_sql+"""\n                     WHERE id=?\n                     ORDER BY updated_at DESC"""
        save_sql = "INSERT INTO "+table_name+"\n                        ("+",\n                         ".join(col_tem for col_tem in  columns if col_tem!="id")+")\n"+"                     VALUES\n                        ("+",\n                         ".join(":"+col_tem for col_tem in columns if col_tem !="id")+")"
        update_sql = "UPDATE "+table_name+"\n                     SET\n                        "+",\n                        ".join(col_tem+"=:"+col_tem for col_tem in  columns if col_tem!="id")+"\n                     WHERE id=:id"
        dao_content= """#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app.commons import dateutil

from app.daos.base_dao import YestarBopsBaseDao


class """+dao_name+"""Dao(YestarBopsBaseDao):
    \"\"\""""+table_name+"""表数据访问对象

    \"\"\"
    TABLE_NAME = '"""+table_name+"""'
    GETS_SQL = \"\"\""""+gets_sql+"""\n                     ORDER BY updated_at DESC\"\"\"

    GET_BY_ID_SQL = \"\"\""""+get_by_id_sql+"""\"\"\"

    SAVE_SQL = \"\"\""""+save_sql+"""\"\"\"

    UPDATE_SQL = \"\"\""""+update_sql+"""\"\"\"

    DELETE_SQL = \"\"\"UPDATE """+table_name+"""
                     SET
                        is_deleted = 1,
                        operator_id = :operator_id,
                        updated_at = :updated_at
                     WHERE  id=:id\"\"\"

    def gets(self):
        \"\"\"查询所有记录
        :return: array
        \"\"\"
        return self._dbfactory.gets(self.GETS_SQL)

    def get_by_id(self, """+table_name+"""_id):
        \"\"\"根据id查询单条记录
        :param """+table_name+"""_id:
        :return: """+table_name+""" 信息
        \"\"\"
        return self._dbfactory.get(self.GET_BY_ID_SQL, ["""+table_name+"""_id])

    def save(self, """+table_name+"""):
        \"\"\"保存

        :param """+table_name+""":"""+table_name+"""信息
        :return: """+table_name+""" id
        \"\"\"
        """+table_name+"""["updated_at"] = """+table_name+"""["created_at"] = dateutil.timestamp()
        return self._dbfactory.execute(self.SAVE_SQL, """+table_name+""")

    def update(self, """+table_name+"""):
        \"\"\"更新

        :param """+table_name+""":
        :return:
        \"\"\"
        """+table_name+"""["updated_at"] = dateutil.timestamp()
        return self._dbfactory.execute(self.UPDATE_SQL, """+table_name+""")

    def delete(self, """+table_name+"""):
        \"\"\"逻辑删除，修改is_deleted = 1

        :param """+table_name+""":
        :return:
        \"\"\"
        """+table_name+"""["updated_at"] = dateutil.timestamp()
        return self._dbfactory.execute(self.DELETE_SQL, """+table_name+""")

        """
        tf = open(file_dir+table_name+"_dao.py","w")
        tf.write(dao_content)
        cursor.close()

    def create_service(self,**kwargs):

        """
        创建service.py文件，默认5个基本方法。
        :param kwargs:
        """
        table_name = kwargs["table_name"]
        file_dir = kwargs["file_dir"]
        tns = table_name.split("_")
        service_name = ""
        for tn in tns:
            service_name+=tn.capitalize()
        dao_content= """#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.daos.yestarbops."""+table_name+"""_dao import """+service_name+"""Dao


class """+service_name+"""Service(object):
    \"\"\""""+table_name+"""表数据访问对象

    \"\"\"
    def __init__(self):
        self._"""+table_name+"""_dao = """+service_name+"""Dao()

    def gets(self):
        \"\"\"查询所有记录
        :return: array
        \"\"\"
        return self._"""+table_name+"""_dao.gets()

    def get_by_id(self, """+table_name+"""_id):
        \"\"\"根据id查询单条记录
        :param """+table_name+"""_id:
        :return: """+table_name+""" 信息
        \"\"\"
        return self._"""+table_name+"""_dao.get_by_id("""+table_name+"""_id)

    def save(self, """+table_name+"""):
        \"\"\"保存

        :param """+table_name+""":"""+table_name+"""信息
        :return: """+table_name+""" id
        \"\"\"
        return self._"""+table_name+"""_dao.save("""+table_name+""")

    def update(self, """+table_name+"""):
        \"\"\"更新

        :param """+table_name+""":
        :return:
        \"\"\"
        return self._"""+table_name+"""_dao.update("""+table_name+""")

    def delete(self, """+table_name+"""):
        \"\"\"逻辑删除，修改is_deleted = 1

        :param """+table_name+""":
        :return:
        \"\"\"
        return self._"""+table_name+"""_dao.delete("""+table_name+""")

        """
        tf = open(file_dir+table_name+"_service.py", "w")
        tf.write(dao_content)

if __name__ == "__main__":
    ac = AutoCode()
    msg = dict(
        table_name="test",
        columns=['name VARCHAR(45) NOT NULL',
                 'type VARCHAR(45) NOT NULL',
                 'age VARCHAR(45) NOT NULL'
                 ]
    )
    ac.create_table(**msg)

    ac.create_dao(**dict(table_name="test", file_dir="../../app/daos/yestarbops/"))
    ac.create_service(**dict(table_name="test", file_dir="../../app/services/yestarbops/"))
#
# file_stream = file(os.path.join(Settings.SITE_ROOT_PATH, 'configs/databases.yaml'), 'r')
# yml = yaml.load(file_stream)
# runmod = "development"
# databases_config = yml.get(runmod)
# config = databases_config["default"]
# # 建立和数据库系统的连接
# conn = MySQLdb.connect(host=config.get('host'), user=config.get('username'), passwd=config.get('password'),
#                        charset=config.get('encoding'))
# conn.select_db(config.get('database'))
# #获取操作游标
# cursor = conn.cursor()
# #执行SQL
# count = cursor.execute("""select * from users """)
# for pp in dir(cursor):
#     if not pp.startswith("_"):
#         print pp  # cursor[pp]
# print count
# print '-----------' * 100
# for col in cursor.description:  #字段信息
#     print col[0].ljust(15), col
# print '-----------' * 100
# for rel in cursor:
#     #遍历查询结果
#     print rel
# #关闭连接，释放资源
# cursor.close();