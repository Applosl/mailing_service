#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask_mail import Message
from flask import current_app


def send_mail(receivers: list, subject: str, message: str, subtype: str = 'plain'):
    """
    发送邮件
    :param receivers: list
    :param subject: str
    :param message: str
    :param subtype: str
    :return:
    """
    message = Message(subject=subject, recipients=receivers, html=message, charset="utf-8")
    mail = current_app.extensions.get("mail")
    res = mail.send(message)
    print(res)
    print("邮件发送成功")
