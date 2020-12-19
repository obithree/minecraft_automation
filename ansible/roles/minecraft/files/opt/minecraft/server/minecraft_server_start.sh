#!/bin/sh

#screenの名前
SCREEN_NAME='minecraft'

screen -UAmdS $SCREEN_NAME java -server -Dfile.encoding=UTF-8 -Xms6G -Xmx6G -jar /opt/minecraft/server/server.jar
