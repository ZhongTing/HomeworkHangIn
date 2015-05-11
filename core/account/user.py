from core.models import UserType


class User():
    def __init__(self, model):
        self._user = model

    def __str__(self):
        return str(self._user.__dict__)

    @property
    def is_valid(self):
        return True

    @property
    def account(self):
        return self._user.account

    @property
    def student_id(self):
        return self.account[1:self.account.find("@")]

    @property
    def is_ta(self):
        return self._user.role is UserType.ASSISTANT

    @property
    def is_student(self):
        return self._user.role is UserType.STUDENT