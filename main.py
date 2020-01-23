#!/usr/bin/env python3
# coding=utf-8

import sys
from flask import Flask
from App.restful_env import restful_build
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
restful_build(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'prod':
        print('prod Env')
        http_server = WSGIServer(('', 9990), app)
        http_server.serve_forever()
    else:
        print('dev Env')
        app.run(debug=True, port=9990)  # 开启
