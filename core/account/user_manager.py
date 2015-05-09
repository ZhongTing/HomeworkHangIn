from core.account.user import User
from core.models import UserModel
from core.utility.error_exceptions import AuthorizationError


class UserManager():
    __user_token_cache = {}

    def __init__(self):
        pass

    @classmethod
    def get_user_from_token(cls, token, use_cache=True):
        if use_cache and token in cls.__user_token_cache:
            return cls.__user_token_cache[token]

        try:
            user_model = UserModel.objects.get(access_token=token)
            user = User(user_model)
            cls.__user_token_cache[token] = user
            return user

        except UserModel.DoesNotExist:
            raise AuthorizationError()