#!/bin/bash

APP_NAME=www-yestar-web
listen_line=4
listen_start=8091

BASE_PATH=$(dirname $0)
BASE_PATH=${BASE_PATH/\./$(pwd)}
APP_PATH=$(dirname "$BASE_PATH")

RUNMOD=production
LOG_DIR=~/logs/$APP_NAME
mkdir -p $LOG_DIR


export PYTHONPATH=$APP_PATH

cd $APP_PATH
