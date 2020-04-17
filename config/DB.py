# coding=utf-8

import os


class DbConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", False)  # 是否输出SQL在控制台 用于调试
    SQLALCHEMY_COMMIT_ON_TEARDOWN = os.environ.get("SQLALCHEMY_COMMIT_ON_TEARDOWN", True)  # 在2.0下该配置被去除
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", False)
