#!/usr/bin/env python3
# coding=utf-8

import os
from flask import Flask
from App.restful_env import restful_build
from gevent.pywsgi import WSGIServer
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
restful_build(app)

if __name__ == '__main__':
    if os.environ.get('FLASK_ENV') == 'production':
        print('prod Env')
        http_server = WSGIServer(('127.0.0.1', 9990), app)
        http_server.serve_forever()
    else:
        print('dev Env')
        app.run(port=9990)  # 开启
