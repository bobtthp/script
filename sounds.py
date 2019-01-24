#coding:utf-8
from flask import Flask,request
import pyttsx
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
app=Flask(__name__)
app.debug = True
@app.route('/beep',methods=['POST','GET'])
def beep():
    if request.method == 'GET':
        return 'not get method'
    else:
        rec_json =  request.data
        rec_dict = json.loads(rec_json)
        status =  rec_dict['state']
        if rec_dict.has_key('message'):
            messages = rec_dict['message']
        else:
            messages = '有异常报警，未设置报警信息'
        if status == 'alerting':
            speak = pyttsx.init()
            rate = speak.getProperty('rate')
            speak.setProperty('rate',rate - 20)
            speak.say(messages)
            speak.runAndWait()
        return 'ok'
if __name__ == '__main__':
    app.run(host='172.28.223.177', port=8000)



