class Homework():
    def __init__(self, model):
        self.__model = model

    @property
    def homework_id(self):
        return self.__model.pk

    @property
    def year(self):
        return self.__model.year

    @property
    def name(self):
        return self.__model.name

