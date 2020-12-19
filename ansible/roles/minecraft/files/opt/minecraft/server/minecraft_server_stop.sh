#!/bin/sh

# screenの名前
SCREEN_NAME='minecraft'

if [ -n "$(screen -list | grep -o "${SCREEN_NAME}")" ]; then
    # 停止開始
    echo [date '+%F %T'] 'server stop script start'
    # サーバー内にアナウンス
    screen -S $SCREEN_NAME -X stuff 'say 30秒後にサーバーを停止します\015'
    sleep 30s
    # セーブコマンド発行
    screen -S $SCREEN_NAME -X stuff 'save-all\015'
    sleep 5s
    # 停止コマンド発行
    screen -S $SCREEN_NAME -X stuff 'stop\015'
    #停止実行待機
    sleep 30s
else
    echo [date '+%F %T']  'server is not runnning'
fi
