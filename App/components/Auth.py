# coding=utf-8

from typing import Optional
from App.Models.Models import Account


class Auth(object):
    """
    权限控制类
    """

    @staticmethod
    def check_account(app_id, secret) -> Optional[Account]:
        """
        检测账户信息
        :param app_id: int
        :param secret: str
        :return:
        """
        account_dao = Account.query.filter(Account.id == app_id, Account.secret == secret,
                                           Account.status == Account.STATUS_ON).first()

        if not isinstance(account_dao, Account):
            return None
        return account_dao
