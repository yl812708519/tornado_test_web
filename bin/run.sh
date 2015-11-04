#!/bin/bash

base_path=$(dirname $0)
base_path=${base_path/\./$(pwd)}
source $base_path/env.sh

source $base_path/$APP_NAME/bin/activate

mkdir -p $LOG_DIR/bak

show_app_status() {
    APP_NAME=$1
    now_pids=`/bin/ps -ef|grep "app_name=$APP_NAME"|grep -v grep|awk ' ''{print $2}'`
    if [ -z "${now_pids}" ] ; then
        echo "$APP_NAME is stoped"
        return 1
    else
        for now_pid in ${now_pids};do
            echo "$APP_NAME is running. pid:${now_pid}"
        done
        return 0
    fi
}


start_app() {
    APP_NAME=$1
    RUNMOD=$2

    show_app_status "$APP_NAME"
    local result=$?
    if [ 0 -eq $result ]; then
        echo "$APP_NAME is still in running"
        return 0
    fi
    cd $APP_PATH
    for (( i=0; i<${listen_line}; i++));do
        listen_port=$[${listen_start}+${i}]
        python configs/application.py --port=${listen_port} \
                                      --runmod=$RUNMOD \
                                      --app_name=$APP_NAME \
                                      1>$LOG_DIR/output_${listen_port}.log \
                                      2>$LOG_DIR/error_${listen_port}.log &
    done
    sleep 3
    show_app_status "$APP_NAME"
    result=$?
    if [ 1 -eq $result ]; then
        for (( i=0; i<${listen_line}; i++));do
            listen_port=$[${listen_start}+${i}]
            echo "please check error:tail -200f $LOG_DIR/error_${listen_port}.log"
        done
        return 1
    fi
    echo "$APP_NAME start success"
    return 0
}

stop_app() {
    APP_NAME=$1
    now_pids=`/bin/ps -ef|grep "app_name=$APP_NAME"|grep -v grep|awk ' ''{print $2}'`
    if [ -z "${now_pids}" ] ; then
        echo "$APP_NAME is stoped"
        return 1
    else
        echo "$APP_NAME is stoping"
        for now_pid in ${now_pids};do
            echo "$APP_NAME kill pid:${now_pid}"
            /bin/kill ${now_pid}
        done
        sleep 4
        show_app_status "$APP_NAME"
        result=$?
        if [ 0 -eq $result ]; then
            echo "$APP_NAME stop failure. please check error:tail -200f $LOG_DIR/error_xxxx.log"
            return 1
        else
            mv $LOG_DIR/error_*.log $LOG_DIR/bak
            mv $LOG_DIR/output_*.log $LOG_DIR/bak
            echo "$APP_NAME stop success"
            return 0
        fi
    fi
}

if [ "$2" != "" ]; then
    RUNMOD=$2
fi

case "$1" in
	start)
	    start_app "$APP_NAME" "$RUNMOD"
		;;
	stop)
	    stop_app "$APP_NAME"
		;;
	status)
		show_app_status "$APP_NAME"
		;;
	restart)
	    stop_app "$APP_NAME"
	    start_app "$APP_NAME" "$RUNMOD"
		;;
	*)
		echo $"Usage: ./run.sh {start|stop|restart|status} {development|test|production}"
		exit 1
esac

exit 1
