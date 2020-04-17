# coding=utf-8

import traceback
from App.components.Auth import Auth
from functools import wraps
from flask import make_response, current_app
from flask_restful import reqparse
from App.middleware.db import db
from App.components.APIException import APIException


def check_auth():
    parser = reqparse.RequestParser()
    parser.add_argument('appid', type=str, required=True, help="appid is invalid", location='headers')
    parser.add_argument('secret', type=str, required=True, help="secret is invalid", location='headers')
    params = parser.parse_args()
    appid = params['appid']
    secret = params['secret']
    return Auth.check_account(app_id=appid, secret=secret)


def request_auth():
    """
    检查权限 装饰器
    :return:
    """

    def check_auth_decorator(func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            account = check_auth()
            if not account:
                return return_fail(code=10001, message='Permission forbidden')
            return func(account=account, *args, **kwargs)

        return wrap_function

    return check_auth_decorator


def base_api_response():
    """
    基础BaseApi响应
    :return:
    """

    def base_api_response_decorator(func):
        @wraps(func)
        def wrap_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except APIException as e:
                return make_response(returnApiException(e))
            except Exception as e:
                return make_response(return_internal_error(e))
            finally:
                db.session.close()

        return wrap_function

    return base_api_response_decorator


# API 异常错误
def returnApiException(e: APIException):
    error_file = e.__traceback__.tb_frame.f_code.co_filename
    error_line_no = e.__traceback__.tb_lineno
    current_app.logger.debug("API错误文件: %s 错误行号: %s " + str(e.message), error_file, error_line_no)
    return return_fail(code=e.code, message=e.message)


# 内部错误
def return_internal_error(e: Exception):
    error_file = e.__traceback__.tb_frame.f_code.co_filename
    error_line_no = e.__traceback__.tb_lineno
    error_message = traceback.format_exc()
    current_app.logger.error("服务内部错误 API错误文件: %s 错误行号: %s   | %s", error_file, error_line_no, error_message)
    return return_fail(code=30001, message="服务器内部错误")


# 返回成功
def return_success(data={}):
    return {
        "code": 0,
        "message": "OK",
        "data": data
    }


# 返回失败
def return_fail(message: str, code: int = 1):
    return {
        "code": code,
        "message": message,
    }
