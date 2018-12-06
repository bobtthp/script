#/bin/bash
#将佣金宝官网后台的静态化文件同步到防篡改服务器上

log_dir="/tmp/log/"
ip="11.11.11.11"
datasource="/git/script/"
dataremote="/tmp/git/script/"

if [ ! -d "$log_dir" ]; then
	mkdir $log_dir
fi

/usr/bin/inotifywait -mrq --timefmt '%F %T' --format '%T %w%f' -e close_write,move,delete,create $datasource | while read files
do
	today=`date '+%Y%m%d'`
	echo "------------------------------$ip----------------------------" >> $log_dir/crhwebsite_rsync_$today.log
	/usr/bin/rsync -avzrtopgLc -e "ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" $datasource $ip:$dataremote >> $log_dir/crhwebsite_rsync_$today.log  2>&1
	if [ $? -eq 0 ];then
		echo "${files} was rsynced successed........."    >> $log_dir/crhwebsite_rsync_$today.log
	else
		echo "${files} was rsynced failed........."   >> $log_dir/crhwebsite_rsync_$today.log
	fi
done
