from core.models import HomeworkModel
from django.test import TestCase
from core.homework.homework_manager import HomeworkManager


class TestHomeworkManager(TestCase):
    def setUp(self):
        self._homework_manager = HomeworkManager()
        data1 = {
            "year": 1,
            "name": "name1",
            "total_score": 10,
        }
        data2 = {
            "year": 2,
            "name": "name2",
            "total_score": 20,
        }
        self._homework_manager.create_homework(data1)
        self._homework_manager.create_homework(data2)

    def test_list_homework(self):
        homework_list = self._homework_manager.list_homework()
        self.assertEqual(homework_list[0]["year"], 1)
        self.assertEqual(homework_list[0]["name"], "name1")

        self.assertEqual(homework_list[1]["year"], 2)
        self.assertEqual(homework_list[1]["name"], "name2")

    def test_get_homework(self):
        homework = self._homework_manager.get_homework(1)
        self.assertEqual(homework.year, 1)
        self.assertEqual(homework.name, "name1")
        self.assertEqual(homework.total_score, 10)

        homework = self._homework_manager.get_homework(2)
        self.assertEqual(homework.year, 2)
        self.assertEqual(homework.name, "name2")
        self.assertEqual(homework.total_score, 20)

    def tearDown(self):
        HomeworkModel.objects.all().delete()