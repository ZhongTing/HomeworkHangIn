import zipfile

from os.path import basename
from app.settings import HOMEWORK_UPLOAD_FOLDER
from core.homework.homework import Homework
from core.models import HomeworkModel
from core.utility.error_exceptions import NotFoundError, DuplicateError, ParameterError, AuthorizationError
from django.db import IntegrityError
from django.http import HttpResponse
import os


class HomeworkManager():
    def __init__(self):
        self.__homework_cache = {}
        homework_model_list = HomeworkModel.objects.all()
        for homework_model in homework_model_list:
            self.__homework_cache[homework_model.pk] = Homework(homework_model)

    def create_homework(self, data):
        try:
            homework_model = HomeworkModel.objects.create(**data)
            self.__homework_cache[homework_model.pk] = Homework(homework_model)
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
        filename = self._get_homework_file_path(homework_id, user)
        save_file = open(filename, "wb")
        for chunk in homework_file:
            save_file.write(chunk)
        save_file.close()

    def download_homework(self, homework_id, user):
        if user.is_student:
            file_path = self._get_homework_file_path(homework_id, user)
        elif user.is_ta:
            file_path = self._get_homework_zip_file_path(homework_id)
        else:
            raise AuthorizationError()

        if not os.path.isfile(file_path):
            raise NotFoundError()

        chunks = []
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(8192)
                if chunk:
                    chunks.append(chunk)
                else:
                    break

        response = HttpResponse(b''.join(chunks), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_path)

        return response

    def _get_homework_zip_file_path(self, homework_id):
        folder_path = self._get_homework_file_folder(homework_id)
        zip_filename = "temp/all_%s_hw.zip" % str(homework_id)

        temp_zip = zipfile.ZipFile(zip_filename, 'w')
        for root, dirs, files in os.walk(folder_path):
            for f in files:
                path = os.path.join(root, f)
                temp_zip.write(path, basename(path))
        temp_zip.close()

        return zip_filename

    def _get_homework_file_path(self, homework_id, user):
        student_id = str(user.student_id)
        folder_path = self._get_homework_file_folder(homework_id)
        file_path = "%s/%s.zip" % (folder_path, student_id)

        return file_path

    def _get_homework_file_folder(self, homework_id):
        if homework_id not in self.__homework_cache:
            raise ParameterError()

        homework = self.__homework_cache[homework_id]
        year = str(homework.year)
        homework_id = str(homework.homework_id)
        folder_path = "%s/%s/%s" % (HOMEWORK_UPLOAD_FOLDER, year, homework_id)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        return folder_path


homework_manager = HomeworkManager()