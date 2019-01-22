#!/usr/bin/python -Es 
import threading
import os
print threading.__file__
def test():
	os.system('curl http://11.11.11.11:8000/cpu')
for i in range(30):
	import time
        time.sleep(0.5)
	for i in range(100):
		threading.Thread(target=test,name='thread-1').start()
	
