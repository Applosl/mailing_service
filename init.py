#!/usr/bin/env python3
# coding=utf-8
import os

if __name__ == "__main__":
    # check dir
    if not os.path.exists('config'):
        os.mkdir('config', 0o755)

    if not os.path.exists('config/DB.py'):
        os.mkdir('config/DB.py', 0o755)

    with open('config/DB.py', 'w') as f:
        db_config = [
            'class DbConfig:',
            '\tSQLALCHEMY_DATABASE_URI = ""  # MYSQL CONFIG',
            '\tSQLALCHEMY_ECHO = False  # 是否输出SQL在控制台 用于调试',
            '\tSQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 在2.0下该配置被去除',
            '\tSQLALCHEMY_TRACK_MODIFICATIONS = False',
        ]
        f.writelines(db_config)

    if not os.path.exists('config/DB.py'):
        os.mkdir('config/DB.py', 0o755)

    with open('config/Mail.py', 'w') as f:
        mail_config = [
            'class MailConfig:',
            '\tMAIL_SERVER = "smtp.qq.com"  # 邮件服务器地址',
            '\tMAIL_PORT = "587"  # 端口',
            '\tMAIL_USE_TLS = True  # 是否使用TLS',
            '\tMAIL_USERNAME = ""  # 用户名',
            '\tMAIL_PASSWORD = ""  # 密码',
            '\tMAIL_DEFAULT_SENDER = ""  # 默认发件人名称',
        ]
        f.writelines(mail_config)
