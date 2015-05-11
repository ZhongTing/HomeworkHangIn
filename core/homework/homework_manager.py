from app.settings import HOMEWORK_UPLOAD_FOLDER
from core.homework.homework import Homework
from core.models import HomeworkModel
from core.utility.error_exceptions import NotFoundError, DuplicateError
from django.db import IntegrityError
import os


class HomeworkManager():
    def __init__(self):
        self.__homework_cache = {}
        homework_model_list = HomeworkModel.objects.all()
        for homework_model in homework_model_list:
            self.__homework_cache[homework_model.pk] = Homework(homework_model)

    @staticmethod
    def create_homework(data):
        try:
            HomeworkModel.objects.create(**data)
        except IntegrityError:
            raise DuplicateError()

    def list_homework(self):
        homework_list = list()
        for key, value in self.__homework_cache.iteritems():
            homework_list.append({
                "id": value.homework_id,
                "name": value.name,
                "year": value.year,
            })

        return homework_list

    def get_homework(self, homework_id):
        return self.__homework_cache[homework_id]

    def upload_homework(self, homework_id, user, homework_file):
        filename = self._get_homework_filename(homework_id, user)
        save_file = open(filename, "wb")
        for chunk in homework_file:
            save_file.write(chunk)
        save_file.close()

    def download_homework(self, homework_id, user):
        filename = self._get_homework_filename(homework_id, user)
        print filename

    def _get_homework_filename(self, homework_id, user):
        print homework_id
        print self.__homework_cache
        if homework_id not in self.__homework_cache:
            raise NotFoundError()

        homework = self.__homework_cache[homework_id]
        student_id = str(user.student_id)
        year = str(homework.year)
        homework_id = str(homework.homework_id)
        filename = "%s/%s/%s/%s.zip" % (HOMEWORK_UPLOAD_FOLDER, year, homework_id, student_id)

        directory = os.path.dirname(filename)
        if not os.path.exists(directory):
            os.makedirs(directory)

        print filename
        return filename


homework_manager = HomeworkManager()