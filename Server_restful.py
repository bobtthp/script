from flask import Flask
import os
import psutil
import json
from flask import make_response
from functools import wraps
def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun
app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello 8000'

@app.route('/disk')
@allow_cross_domain
def disk():
    d = {}
    for i in psutil.disk_partitions():
        d[i[1]] = {}
        d[i[1]]['total'] =  psutil.disk_usage(i[1]).total/1024/1024/1024.0 #GB 
        d[i[1]]['used']  =  psutil.disk_usage(i[1]).used/1024/1024/1024.0  #%
        print d
    return json.dumps(d)
@app.route('/memory')
@allow_cross_domain
def mem():
    d = {}
    d['total'] = psutil.virtual_memory().total/1024/1024/1024.0
    d['available'] = psutil.virtual_memory().available/1024/1024/1024.0
    d['used'] = psutil.virtual_memory().used/1024/1024/1024.0
    d['free'] = psutil.virtual_memory().free/1024/1024/1024.0
    return json.dumps(d)
@app.route('/cpu')
@allow_cross_domain
def cpu():
    d = {}
    d['info'] = {}
    d['use'] = {}
    d['info']['counts'] = psutil.cpu_count()
    d['info']['cores'] = psutil.cpu_count(logical=False)
    cpuinfo = psutil.cpu_times_percent()
    d['use']['user'] =  cpuinfo.user
    d['use']['system'] = cpuinfo.system
    d['use']['idle'] = cpuinfo.idle
    return json.dumps(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
