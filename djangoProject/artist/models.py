from django.db import models
from django.contrib.auth.models import User


class Work(models.Model):
    link = models.URLField()
    work_type = models.TextField()


class Artist(models.Model):
    name = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)