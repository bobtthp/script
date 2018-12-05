import datetime
import os
import time
f = '/tmp/dc.log'
def get_time(f):
    today = datetime.datetime.today().strftime("%Y%m%d")
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
  
    print '    date:',datetime.datetime.today().strftime("%Y-%m-%d")
    print 'job cost:','%d:%d:%d' % (hours,minutes,seconds)

if __name__ == "__main__":
    date_fmt(get_time(f))
