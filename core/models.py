from django.db import models
from django_enumfield import enum


class UserType(enum.Enum):
    STUDENT = 1
    ASSISTANT = 2

    labels = {
        STUDENT: 'Student',
        ASSISTANT: 'Assistant'
    }


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, default=None, null=True, blank=True, unique=True)

    role = enum.EnumField(UserType, default=UserType.STUDENT)

    account = models.CharField(max_length=50, blank=False, unique=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "user"


class HomeworkModel(models.Model):
    homework_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    year = models.IntegerField(blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    total_score = models.IntegerField(blank=False, null=False)

    class Meta:
        unique_together = ('year', 'name')
        db_table = "homework"