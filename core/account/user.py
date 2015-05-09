class User():
    def __init__(self, model):
        self._user = model

    def __str__(self):
        return str(self._user.__dict__)