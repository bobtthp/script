for ip in {192.168.179.151,192.168.179.152,192.168.170.151,192.168.170.152,172.16.22.190,172.16.22.191,172.16.8.55,172.16.8.56,197.1.8.140,192.168.76.72,192.168.73.72};
	do
		#ssh $ip "tar xf /usr/local/zabbix.tar.gz -C /usr/local/"
		#ssh $ip "useradd zabbix"
		#ssh $ip "chmod 777 /tmp -R "
		#hostname=`ssh $ip "hostname"`
		#ssh $ip "sed -i 's/^Hostname.*/Hostname='$hostname'/g' /usr/local/zabbix/conf/zabbix_agentd.conf"
		#ssh $ip "echo '/usr/local/zabbix/sbin/zabbix_agentd -c /usr/local/zabbix/conf/zabbix_agentd.conf' >> /etc/rc.local"
		ssh $ip "/usr/local/zabbix/sbin/zabbix_agentd -c /usr/local/zabbix/conf/zabbix_agentd.conf"
	done
