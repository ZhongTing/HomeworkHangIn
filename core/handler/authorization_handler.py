from core.account.user_manager import UserManager


class AuthorizationHandler():
    __user_manager = UserManager()

    def __init__(self):
        pass

    @classmethod
    def login(cls, account, password):
        return cls.__user_manager.login(account, password)