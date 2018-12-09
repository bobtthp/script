# -*- coding:utf-8 -*-
import datetime
import os
import time
f = '/mydata/qianxun/log/dc.log'
def get_time(f):
    today = (datetime.datetime.today()+datetime.timedelta(days=-1)).strftime("%Y%m%d")
    start = 'batch = %s-' % today
    end = 'batch = %s-' % today
    cmd = 'sed -n "/%s/{p;:start;n;:end;/%s/{p;bstart};N;bend}" %s' % (start,end,f)
    List = os.popen(cmd).readlines()
    jstart = List[0].split(' ')[1].split(',')[0]
    jstop = List[-1].split(' ')[1].split(',')[0]
    cost = '%d:%d:%d' % (int(jstop.split(':')[0]) - int(jstart.split(':')[0]),int(jstop.split(':')[1]) - int(jstart.split(':')[1]),int(jstop.split(':')[2]) - int(jstart.split(':')[2]))
    return cost
def date_fmt(str):
    hours = int(str.split(':')[0])
    minutes = int(str.split(':')[1])
    seconds = int(str.split(':')[2])
    if minutes < 0:
        hours = hours - 1
        minutes = minutes + 60
    if seconds < 0:
        if minutes > 0:
            minutes = minutes - 1
            seconds = seconds + 60
  
    print '任务日期:',(datetime.datetime.today()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
    print '任务时长:','%d:%d:%d' % (hours,minutes,seconds)
def get_file_update():
    file_path = '/mydata/voice/'
    today_dir = file_path + datetime.datetime.today().strftime("%Y_%m_%d")
    yestoday_dir = file_path + (datetime.datetime.today()+datetime.timedelta(days=-1)).strftime("%Y_%m_%d")
    before_yestoday_dir = file_path + (datetime.datetime.today()+datetime.timedelta(days=-2)).strftime("%Y_%m_%d")
    print os.popen('du -sh ' + yestoday_dir).readlines()[0].replace('\t',': ').replace('\n','')
    print os.popen('du -sh ' + before_yestoday_dir).readlines()[0].replace('\t',': ').replace('\n','')
if __name__ == "__main__":
    print '====任务监控===='
    date_fmt(get_time(f))
    print '====容量监控===='
    get_file_update()
