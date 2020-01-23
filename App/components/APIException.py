# -*- coding:utf-8 -*-


class APIException(Exception):
    """
    API 异常类
    """
    code = 0
    message = "success"

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
