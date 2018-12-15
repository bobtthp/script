#/bin/bash

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
	echo "------------------------------$ip----------------------------" >> $log_dir/$today.log
	/usr/bin/rsync -avzrtopgLc -e "ssh -oUserKnownHostsFile=/dev/null -oStrictHostKeyChecking=no" $datasource $ip:$dataremote >> $log_dir/$today.log  2>&1
	if [ $? -eq 0 ];then
		echo "${files} was rsynced successed........."    >> $log_dir/$today.log
	else
		echo "${files} was rsynced failed........."   >> $log_dir/$today.log
	fi
done
