import sys
import time
from kazoo.client import KazooClient
import json
root = '/bob'
config = {
	'hosts' : '11.11.11.11:2181',
	'timeout' : 120
}
zkclient = KazooClient(**config)
zkclient.start()
#print help(zkclient)
if not zkclient.exists(root):
	zkclient.create(root,'bob')
else:
	#print zkclient.get(root)
	if zkclient.exists(root + '/11.11.11.11'):
		data = zkclient.get(root + '/11.11.11.11')
                print json.loads(data[0])
                print data[1]
	else:
		zkclient.create(root + '/11.11.11.11','11.11.11.11')

#json = json.dumps('{"name":"boc"}')
#zkclient.set(root + '/11.11.11.11',json)
