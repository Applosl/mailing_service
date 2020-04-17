# -*- coding:utf-8 -*-
import os


class MailConfig:
    """
    邮件中间件配置
    """
    MAIL_SERVER = os.environ.get("MAIL_SERVER")  # 邮件服务器地址
    MAIL_PORT = os.environ.get("MAIL_PORT")  # 端口
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", True)  # 是否使用TLS
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")  # 用户名
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")  # 密码
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")  # 默认发件人名称
