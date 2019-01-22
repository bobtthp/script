from flask import Flask

app=Flask(__name__,template_folder='../static/html')
app.debug = True

@app.route('/')
def hello():
    return 'hello 8000'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
