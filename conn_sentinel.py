from redis.sentinel import Sentinel

sentinel = Sentinel([('127.0.0.1',26379)],socket_timeout=0.5)
#master = sentinel.discover_master('mymaster')
#print master
master = sentinel.master_for('mymaster',socket_timeout=0.5,password='',db=3)
master.set('11.11.11.11',"{'cpu':'10'}")
print master.get('11.11.11.11')
