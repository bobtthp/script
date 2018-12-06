#!/usr/bin/python
import hashlib
import sys
import os
def Md5sum(f):
    md5 = hashlib.md5()
    if os.path.isdir(f):
        print 'it is dir'
    else:
        f = open(f,'rb')
        md5.update(f.read())
        f.close()
        return md5.hexdigest()
def Dict_file(Dir):
    if not os.path.isdir(Dir):
        print 'please add args for dir'
    else:
        file_dict = {}
        for path,dirs,fs in os.walk(Dir):
            for f in fs:
                f_list = []
                f_path = os.path.join(path,f)
                f_list.append(f_path)
                file_dict[f] = f_list
        return file_dict
def Md5_dict(Dict):
    for f in Dict:
        file_md5 = Md5sum(Dict[f][0])
        Dict[f].append(file_md5)
    return Dict
def Compare_dict(d1,d2):
    for f in d1:
        if f in d2:
            if d1[f][1] != d2[f][1]:
                print '-warning: different md5 for same files'
                print d1[f][0],d1[f][1],'====>',d2[f][0],d2[f][1]
        else:
            print '-warning: different files in dirs'
            print d1[f][0],d1[f][1]
    for f in d2:
        if f in d1:
            pass
        else:
            print '-warning: different files in dirs'
            print d2[f][0],d2[f][1]
if __name__ == '__main__':
    file_path = sys.argv[1:]
    try:
        if '-d' in file_path:
                file_path.remove('-d')
                dir1 =  Md5_dict(Dict_file(file_path[0]))
                dir2 =  Md5_dict(Dict_file(file_path[1]))
                Compare_dict(dir1,dir2)
        else:         
            File = file_path
            print Md5sum(File[0]),File[0]
    except Exception as e:
        print e
