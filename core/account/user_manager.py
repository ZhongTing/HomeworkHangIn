import hashlib
import uuid
import sys

from core.account.user import User
from core.models import UserModel, UserType
from core.utility.error_exceptions import AuthorizationError


class UserManager():
    def __init__(self):
        self.__user_token_cache = {}

    def get_user_from_token(self, token, use_cache=True):
        if use_cache and token in self.__user_token_cache:
            return self.__user_token_cache[token]

        try:
            user_model = UserModel.objects.get(access_token=token)
            user = User(user_model)
            self.__user_token_cache[token] = user
            return user

        except UserModel.DoesNotExist:
            raise AuthorizationError()

    def login(self, account, password):
        try:
            user_id = self._convert_to_user_identity(account)
            encrypt_password = self._encrypt_password(password)

            user_model = UserModel.objects.get(user_id=user_id, password=encrypt_password)
            if not user_model.access_token:
                user_model.access_token = self._create_access_token()
                user_model.save()

            return {
                "accessToken": user_model.access_token,
                "name": user_model.name,
                "account": user_model.account,
                "role": UserType.labels[user_model.role],
            }

        except UserModel.DoesNotExist:
            raise AuthorizationError()

    @staticmethod
    def _convert_to_user_identity(account):
        return hash(account) % sys.maxsize

    @staticmethod
    def _create_access_token():
        return str(uuid.uuid4()).replace("-", "")

    @staticmethod
    def _encrypt_password(password):
        return hashlib.sha224(password).hexdigest()


user_manager = UserManager()