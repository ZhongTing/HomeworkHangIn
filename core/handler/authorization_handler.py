from core.account.user_manager import UserManager


class AuthorizationHandler():
    __user_manager = UserManager()

    def __init__(self):
        pass

    @classmethod
    def login(cls, account, password):
        return cls.__user_manager.login(account, password)

    @classmethod
    def is_valid(cls, token):
        user = cls.__user_manager.get_user_from_token(token)
        return user.is_valid

    @classmethod
    def get_account(cls, token):
        user = cls.__user_manager.get_user_from_token(token)
        return user.account