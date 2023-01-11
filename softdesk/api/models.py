from django.db import models
from django.contrib.auth import get_user_model


class Project(models.Model):
    title = models.CharField(
                             verbose_name='titre',
                             max_length=200,
                             null=False)
    description = models.TextField(
                                   max_length=2000,
                                   null=False)
    type = models.CharField(
                            max_length=100,
                            null=False)
    author = models.ForeignKey(
                               get_user_model(),
                               null=False,
                               on_delete=models.CASCADE)
