from core.account.user_manager import UserManager
from core.utility.error_exceptions import AuthorizationError
from django.test import TestCase
from core.models import UserModel


class TestUserManager(TestCase):
    def setUp(self):
        self._user_manager = UserManager()
        UserModel.objects.create(user_id=1775634455973687126, access_token="token1", account="account1", password="9440e64e095ff718c1926110fd811e64948984c9dee7ef860feb4d5d")
        UserModel.objects.create(user_id=3589683559412082469, access_token="token2", account="account2", password="f346538a32757f10aa71baf7cf05693a6ac006f61347c5d5a1cfbd83")

    def test_get_user_from_token(self):
        user = self._user_manager.get_user_from_token("token1")
        self.assertEqual(user.account, 'account1')

    def test_get_user_from_token_exception(self):
        try:
            user = self._user_manager.get_user_from_token("no this token")
            self.assertTrue(False)
        except AuthorizationError:
            pass

    def test_login(self):
        user = self._user_manager.login("account1", "password1")
        self.assertEqual(user["accessToken"], "token1")
        self.assertEqual(user["account"], "account1")

    def test_login_fail(self):
        try:
            user = self._user_manager.login("no this account", "no this password")
            self.assertTrue(False)
        except AuthorizationError:
            pass

    def tearDown(self):
        UserModel.objects.all().delete()
