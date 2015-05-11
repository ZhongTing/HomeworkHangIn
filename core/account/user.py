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
    def role(self):
        return self._user.role