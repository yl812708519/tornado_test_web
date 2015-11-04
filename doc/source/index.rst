.. aiwanr documentation master file, created by
   sphinx-quickstart on Fri May  9 11:17:18 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===========================
Spiral Developer's Guide
===========================

Install
===========
On Windows7
-----------------

1. 安装Python
"""""""""""""""""""""""""""""""""""""""

| 去python.org下载Python，地址为
| https://www.python.org/ftp/python/2.7.8/python-2.7.8.amd64.msi ,
| 安装的时候选择Add Python.exe to Path

2. 安装setuptools
"""""""""""""""""""""""""""""""""""""""

| 去 https://pypi.python.org/pypi/setuptools 下载 ez_setup.py 文件
| 然后执行python ez_setup.py

3. 安装pip
"""""""""""""""""""""""""""""""""""""""

| 去 https://pypi.python.org/pypi/pip#downloads 下载pip的压缩包
| 解压后进入解压目录，执行python setup.py install

4. 安装MySQL
"""""""""""""""""""""""""""""""""""""""
| 去 http://dev.mysql.com/downloads/file.php?id=452278 下载
| 如果本地不需要MySQL Server的话可以就安装几个Client命令行，必须包含connector/c
| 或者可以单独去下载安装MySQL Connector/c
| 去 http://dev.mysql.com/downloads/connector/c/

5. 安装MySQL-python
"""""""""""""""""""""""""""""""""""""""
| win7 64位的在网上找了好久，终于找到了
| 下载地址 http://arquivos.victorjabur.com/python/modules/MySQL-python-1.2.3.win-amd64-py2.7.exe
| 下载后点击运行安装
| 安装完成后再查看python安装目录下的Lib\site-packages里面是否有mysqldb，如果有则将目录改成MySQLdb，python是认大小写的

6. 安装pycurl
"""""""""""""""""""""""""""""""""""""""
| 下载pycurl-7.19.0.win-amd64-py2.7.exe，
| 可以到CSDN查找并下载
| http://download.csdn.net/detail/chenjun819/5206113
| 然后进行安装

7. 设置环境变量
"""""""""""""""""""""""""""""""""""""""
| 将Python下面的Scripts目录加入到Path中，因为这样可以让pip可以直接在命令提示符下直接执行
| 然后重新运行cmd

8. 通过pip安装其他的组件
"""""""""""""""""""""""""""""""""""""""
在cmd下面执行如下命令::

    pip install tornado
    pip install pyyaml
    pip install Image
    pip install sphinx


On Ubuntu
-----------------

install shell::

    sudo apt-get install python

    #install tornado
    wget http://github.com/downloads/facebook/tornado/tornado-2.0.tar.gz
    tar -xvzf tornado-2.0.tar.gz
    cd tornado-2.0
    python setup.py build
    sudo python setup.py install

    sudo apt-get install python-pycurl

    #install aiwanr dependency pack
    sudo apt-get -y install python-mysqldb python-yaml python-imaging

    sudo apt-get -y install g++ python-dev

    wget http://mirror.bjtu.edu.cn/apache//thrift/0.7.0/thrift-0.7.0.tar.gz
    tar -xvzf thrift-0.7.0.tar.gz
    cd thrift-0.7.0
    chmod 777 configure
    chmod 777 /lib/erl/rebar

    #install nginx
    sudo apt-get -y install nginx

    #install mysql
    sudo apt-get -y install mysql-server-5.1 mysql-client-5.1


ubuntu 下Mysql IDE工具，MySql workbench

On Mac
--------------

install shell::

    #install homebrew
    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    #install wget
    brew install wget
    #install mysql
    brew install mysql

    #install pip
    sudo easy_install pip

    #install x11
    wget http://xquartz.macosforge.org/downloads/SL/XQuartz-2.7.6.dmg
    open XQuartz-2.7.6.dmg
    #下面这一行好像不是必须的
    ln -s /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.9.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers/X11 /usr/local/include/X11

    sudo su -
    export CFLAGS=-Qunused-arguments
    pip install MySQL-python
    pip install pyyaml
    pip install Image
    pip install sphinx

    #start mysql on mac
    mysql.server start


Other IDE
----------
MySql workbench
PyCharm


.. toctree::
   :hidden:

   project
   commons
   configs
   services
   daos