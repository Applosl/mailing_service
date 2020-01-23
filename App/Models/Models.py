# coding: utf-8
from sqlalchemy import Column, DateTime, String, text
from sqlalchemy.dialects.mysql import BIGINT, INTEGER, TINYINT
from App.middleware.db import db


class Account(db.Model):
    __tablename__ = 'account'

    STATUS_ON = 1
    STATUS_OFF = 0

    id = Column(INTEGER(10), primary_key=True, comment='ID')
    secret = Column(String(512), nullable=False, comment='密码')
    create_at = Column(DateTime, nullable=False, comment='创建时间')
    status = Column(TINYINT(3), nullable=False, server_default=text("'0'"), comment='状态码')


class RequestLog(db.Model):
    __tablename__ = 'request_log'

    STATUS_ON = 1
    STATUS_OFF = 0

    id = Column(BIGINT(20), primary_key=True, comment='主键')
    account_id = Column(INTEGER(10), nullable=False, index=True, server_default=text("'0'"), comment='账户ID')
    send_mail = Column(String(255), nullable=False, comment='接收方账号')
    create_at = Column(DateTime, nullable=False, comment='创建时间')
    status = Column(TINYINT(3), nullable=False, server_default=text("'0'"), comment='状态码')
