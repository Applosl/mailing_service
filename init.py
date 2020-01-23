#!/usr/bin/env python3
# coding=utf-8
import os

if __name__ == "__main__":
    # check dir
    if not os.path.exists('config'):
        os.mkdir('config', 0o755)

    if not os.path.exists('config/DB.py'):
        f = open('config/DB.py', 'w')
        f.close()

    with open('config/DB.py', 'w') as f:
        db_config = [
            'class DbConfig:\n',
            '\tSQLALCHEMY_DATABASE_URI = ""  # MYSQL CONFIG\n',
            '\tSQLALCHEMY_ECHO = False  # 是否输出SQL在控制台 用于调试\n',
            '\tSQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 在2.0下该配置被去除\n',
            '\tSQLALCHEMY_TRACK_MODIFICATIONS = False\n',
        ]
        f.writelines(db_config)

    if not os.path.exists('config/Mail.py'):
        f = open('config/Mail.py', 'w')
        f.close()

    with open('config/Mail.py', 'w') as f:
        mail_config = [
            'class MailConfig:\n',
            '\tMAIL_SERVER = "smtp.qq.com"  # 邮件服务器地址\n',
            '\tMAIL_PORT = "587"  # 端口\n',
            '\tMAIL_USE_TLS = True  # 是否使用TLS\n',
            '\tMAIL_USERNAME = ""  # 用户名\n',
            '\tMAIL_PASSWORD = ""  # 密码\n',
            '\tMAIL_DEFAULT_SENDER = ""  # 默认发件人名称\n',
        ]
        f.writelines(mail_config)
