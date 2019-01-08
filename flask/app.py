#!/usr/local/bin/python

from flask import Flask
from flask import request
import os
import json

app = Flask(__name__)

#进入app.route前,拦截器作用
@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    print("userIP:"+ip)
    print("requestURL:"+url)

@app.route('/test/info')
def index():
    return "Hello, World!"

#@app.route("/cmd/ls")
#def command():
#    return os.popen('ls').read()


@app.route("/cmd/<name>")
def command_name(name):
#    result = os.popen('%s') % name
#    return result
    return os.popen(name).read()
    

#if __name__ == '__main__':
#    app.run(debug=True,host="0.0.0.0",port=5000)
