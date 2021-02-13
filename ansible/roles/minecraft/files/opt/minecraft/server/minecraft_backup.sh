#!/bin/sh

SCREEN_NAME='minecraft'
EXEC_PATH='/opt/minecraft'
MINECRAFT_PATH="${EXEC_PATH}/server"
BACKUP_PATH="${EXEC_PATH}/server_backup"
BACKUP_TIME=`date +%Y%m%d-%H%M%S`
BACKUP_NAME="${BACKUP_PATH}/mc_backup_full_${BACKUP_TIME}.tar.gz"
BACKUP_GEN=30
LOG_PATH="${EXEC_PATH}/server/logs"

cd $EXEC_PATH

systemctl stop minecraft.service
# Backup
# tar is used with Relative Path
tar cfz $BACKUP_NAME server

# delete old backup and logs
BACKUP_GEN_PLUS=$(($BACKUP_GEN + 1))
rm -f `ls -t1d ${BACKUP_PATH}/* | tail -n+$BACKUP_GEN_PLUS`
rm -f `ls -t1d ${LOG_PATH}/* | tail -n+$BACKUP_GEN_PLUS`

# delete cache
sh -c "echo 1 > /proc/sys/vm/drop_caches"
systemctl start minecraft.service
