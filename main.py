#!/usr/bin/env python3
# coding=utf-8

from flask import Flask
from App.restful_env import restful_build

app = Flask(__name__)
restful_build(app)

if __name__ == '__main__':
    app.run(debug=True, port=9990)  # 开启
