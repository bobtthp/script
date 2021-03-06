#-*- coding:utf-8 -*-
import datetime
import sys
from ruamel import yaml
import json
import hashlib
import os
import chardet
conf = 'md5_list.json'
def Time(mon=0):
	month = int(datetime.datetime.today().strftime("%m"))
	year = int(datetime.datetime.today().strftime("%y"))
	if month - mon > 1:
		month-= mon
		dir = '%s/%s' % (year,month)
	else:
		year-= 1
		if month - mon < 1:
			month = month +12 -mon
		else:
			month-= mon
		dir = '%s/%s' % (year,month)
	return dir
def decorator(info):
	def wrap(func):
		print 'start===>' 
		func()
		print info
		print 'stop====>'
	return wrap


def Md5sum(f):
	'''return md5 for file'''
    	md5 = hashlib.md5()
    	if os.path.isdir(f):
        	print '-warning: it is dir, please add "-d" '
    	else:
        	f = open(f,'rb')
        	md5.update(f.read())
        	f.close()
        return md5.hexdigest()

def Dict_file(Dir):
    '''walk dir and return dict for file and md5'''
    if not os.path.isdir(Dir):
        print '-warning: please add args for dir'
    else:
        file_dict = {}
        for path,dirs,fs in os.walk(Dir):
            for f in fs:
                f_path = os.path.join(path,f)
		if not os.path.isdir(f_path):
                	file_dict[f_path] = Md5sum(f_path)
        return file_dict

def Md5ToFile(D,version):
	'''write update file infomations into md5.json'''
	if os.path.exists(conf):
		with open(conf,'rb') as f:
			New_Dict = D
			del_list = []
			Dict = json.load(f)
			Dict['version'] = version
			Dict['update_version'] += 1
			Dict['update'] = []
			Dict['last_version'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			Dict['charset_unusual_file'] = GBK_Dict
			for File in Dict['md5_list']:
				if File not in New_Dict:
					Dict['update'].append(File + ':' + Dict['md5_list'][File])
					del_list.append(File)
				else:
					if Dict['md5_list'][File]	!= New_Dict[File]:
						Dict['update'].append(File + ' ==> ' + Dict['md5_list'][File])
						Dict['md5_list'][File] = New_Dict[File]
			for File in New_Dict:
				if File not in Dict['md5_list']:
					Dict['update'].append(File + ' ==>' + New_Dict[File])
					Dict['md5_list'][File] = New_Dict[File]
			if del_list:
				for File in del_list:
					Dict['md5_list'].pop(File)
		try:
			with open(conf,'wb') as f:
                        	json.dump(Dict,f,indent=4)
                	return 0
        	except Exception as E:
                	print E
	else:
		Dict = {}
		Dict['md5_list'] = D
		Dict['update_version'] = 1
		Dict['version'] = version
		Dict['charset_unusual_file'] = GBK_Dict
		Dict['last_version'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		try:
			with open(conf,'wb') as f:
                        	json.dump(Dict,f,indent=4)
                	return 0
        	except Exception as E:
                	print E

def to_unicode(strs):
	'''strs to unicode '''
        charset = ['utf-8','gbk']
        try:
                strs = strs.decode(charset[0])
        except UnicodeDecodeError:
                strs = strs.decode(charset[1])
        return strs
def DealDict(Dict):
	'''reslove charset,deal not ascii'''
	try:
		gbk_dict = {}
		org_keys = []
		for key in Dict:
			if chardet.detect(key)['encoding'] != 'ascii':
				org_keys.append(key)
				gbk_key = to_unicode(key)
				gbk_dict[gbk_key] = Dict[key]
	except Exception as E:
		print E
	finally:
		for keys in org_keys:
			Dict.pop(keys)
	return Dict,gbk_dict
if __name__ == '__main__':
        Dict = Dict_file(sys.argv[1])
	Dict,GBK_Dict = DealDict(Dict)
	Md5ToFile(Dict,sys.argv[2])
