from django.db import models


class UserModel(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=False, null=False, primary_key=True)
    access_token = models.CharField(max_length=50, default='', blank=False, unique=True)

    account = models.CharField(max_length=50, blank=False, unique=False)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = "user"