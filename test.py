import os
import json
import io
def decorator(times):
	def _decorator(func):
		def wrap(args):
			for i in range(times):
				print 'start'
				func(args)
				print 'stop'
		return wrap
	return _decorator
@decorator(2)
def start(*args):
	print 'func'
	print args



def Dict_file(Dir):
    if not os.path.isdir(Dir):
        print '-warning: please add args for dir'
    else:
        file_dict = {}
	n = 1
        for path,dirs,fs in os.walk(Dir):
            for f in fs:
                f_path = os.path.join(path,f)
		file_dict[n] = f_path
		n += 1	
		with open('log','w') as f:
			json.dump(file_dict,f,indent=4)


        return file_dict

print Dict_file('/git/script')
