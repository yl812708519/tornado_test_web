#!/bin/bash

APP_NAME=www-yestar-web
RUNMOD=development
LOG_DIR=~/logs/$APP_NAME
mkdir -p $LOG_DIR
export PYTHONPATH=~/deploy/$APP_NAME
source ~/deploy/$APP_NAME/bin/$APP_NAME/bin/activate

cd ~/deploy/$APP_NAME

listen_line=1
listen_start=8082


case "$1" in
	start)
		/bin/rm -rf $LOG_DIR/$APP_NAME.port
		/bin/touch $LOG_DIR/$APP_NAME.port
		for (( i=0; i<${listen_line}; i++));do
			listen_port=$[${listen_start}+${i}]
			echo ${listen_port} >> $LOG_DIR/$APP_NAME.port
			python configs/application.py --port=${listen_port} \
			                              --runmod=$RUNMOD \
			                              1>~/logs/$APP_NAME/py_output_${listen_port}.log \
			                              2>~/logs/$APP_NAME/py_error_${listen_port}.log &
		done
		echo "start ok !"
		;;
	stop)
		get_port_line=`/bin/cat $LOG_DIR/$APP_NAME.port`
		for stop_port in ${get_port_line};do
			now_pid=`/bin/ps -ef|grep "port=${stop_port}"|grep -v grep|awk ' ''{print $2}'`
			/bin/kill $now_pid
		done
		echo "stop"
		;;
	status)
		get_port_line=`/bin/cat $LOG_DIR/$APP_NAME.port`
		for i in ${get_port_line};do
			now_pid=`/bin/ps -ef|grep ${i}|grep -v grep`
			if [ -z "${now_pid}" ] ; then
				echo ${i} "is stop"
			else
				echo ${now_pid}
			fi
		done
		;;
	restart)
		get_port_line=`/bin/cat $LOG_DIR/$APP_NAME.port`
		for stop_port in ${get_port_line};do
			now_pid=`/bin/ps -ef|grep "port=${stop_port}"|grep -v grep|awk ' ''{print $2}'`
			/bin/kill $now_pid
		done
		echo "stop"

		/bin/rm -rf $LOG_DIR/$APP_NAME.port
		/bin/touch $LOG_DIR/$APP_NAME.port
		for (( i=0; i<${listen_line}; i++));do
			listen_port=$[${listen_start}+${i}]
			echo ${listen_port} >> $LOG_DIR/$APP_NAME.port
			python configs/application.py --port=${listen_port} \
			                              --runmod=development \
			                              1>~/logs/$APP_NAME/py_output_${listen_port}.log \
			                              2>~/logs/$APP_NAME/py_error_${listen_port}.log &
		done
		echo "start ok !"
		;;
	*)
		echo $"Usage: bash $0 {start|stop|restart|status}"
		exit 1
esac

exit 1
