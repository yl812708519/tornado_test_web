#!/usr/bin/env bash
base_path=$(dirname $0)
base_path=${base_path/\./$(pwd)}

source $base_path/env.sh

platform=`uname`
if [[ "$platform" == 'Linux' ]]; then
    sudo apt-get install -y python-dev
    sudo apt-get install -y cronolog
    sudo apt-get install -y python-pip
    sudo apt-get install -y libmysqlclient-dev
    sudo apt-get install -y python-virtualenv
    sudo apt-get install -y libyaml-dev
    sudo apt-get install -y libmemcached-dev
    sudo apt-get install -y libfreetype6-dev
elif [[ "$platform" == 'Darwin' ]]; then
    brew install libmemcached
    brew install wget
    brew install mysql
    sudo easy_install pip
    sudo pip install virtualenv
fi

if [ ! -d $base_path/$APP_NAME ];then
    virtualenv --no-site-packages $base_path/$APP_NAME
fi