
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


start('func have args')
