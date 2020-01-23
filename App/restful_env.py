# coding=utf-8

import flask_restful
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask import jsonify
from config import DB, Mail as Mail_config
from App.controllers import Index


def restful_build(app):
    app.config.from_object(DB.DbConfig)  # 加载数据库配置
    app.config.from_object(Mail_config.MailConfig)  # 加载 Mail 配置
    db = SQLAlchemy()
    db.init_app(app=app)  # 初始化数据库引擎
    api = flask_restful.Api(app)
    api.add_resource(Index.Index, '/send_mail')  # Index 模块

    Mail(app=app)  # 注册Mail

    # 注册统一404处理
    @app.errorhandler(404)
    def error(e):
        ret = {
            "code": 1,
            "message": "error request"
        }
        return jsonify(ret)
