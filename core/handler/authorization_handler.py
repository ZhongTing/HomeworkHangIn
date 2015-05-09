from core.account.user_manager import UserManager


class AuthorizationHandler():
    __user_manager = UserManager()

    def __init__(self):
        pass

    @classmethod
    def login(cls, data):
        account = data["account"]
        password = data["password"]
        access_token = cls.__user_manager.login(account, password)
        return access_token