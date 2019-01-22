import datetime
import sys
from ruamel import yaml
import json
import hashlib
import os
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
    md5 = hashlib.md5()
    if os.path.isdir(f):
        print '-warning: it is dir, please add "-d" '
    else:
        f = open(f,'rb')
        md5.update(f.read())
        f.close()
        return md5.hexdigest()

def Dict_file(Dir):
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
	if os.path.exists(conf):
		with open(conf,'r') as f:
			New_Dict = D
			del_list = []
			Dict = json.load(f)
			Dict['version'] = version
			Dict['update_version'] += 1
			Dict['update'] = []
			Dict['last_version'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
			with open(conf,'w') as f:
                        	json.dump(Dict,f,indent=4)
                	return 0
        	except Exception as E:
                	print E
	else:
		Dict = {}
		Dict['md5_list'] = D
		Dict['update_version'] = 1
		Dict['version'] = version
		Dict['last_version'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		try:
			with open(conf,'w') as f:
                        	json.dump(Dict,f,indent=4)
                	return 0
        	except Exception as E:
                	print E

if __name__ == '__main__':
        D = Dict_file(sys.argv[1])
	Md5ToFile(D,sys.argv[2])
