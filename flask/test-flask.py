#!/usr/local/bin/python

from flask import Flask
from flask import request


app = Flask(__name__)

#进入app.route前,拦截器作用
@app.before_request
def before_request():
    ip = request.remote_addr
    url = request.url
    print(ip)
    print(url)

@app.route('/test/info')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)
