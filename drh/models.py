from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    url_enter =git models.CharField()