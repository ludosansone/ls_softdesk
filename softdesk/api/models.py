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

    def __str__(self):
        return self.title


class Issue(models.Model):
    title = models.CharField(
                             verbose_name='titre',
                             max_length=200,
                             null=False)
    description = models.TextField(
                                   max_length=2000,
                                   null=False)
    tag = models.CharField(
                           max_length=100,
                           null=False)
    priority = models.CharField(
                                max_length=100,
                                null=False)
    status = models.CharField(
                              max_length=100,
                              null=False)
    created_time = models.DateTimeField(
                                        verbose_name='date et heure de création',
                                        auto_now_add=True)
    project = models.ForeignKey(
                                Project,
                                on_delete=models.CASCADE,
                                null=False)
    author = models.ForeignKey(
                               get_user_model(),
                               on_delete=models.CASCADE,
                               null=False,
                               related_name='author')
    assigned = models.ForeignKey(
                                get_user_model(),
                                on_delete=models.CASCADE,
                                null=False,
                                related_name='assigned')

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.TextField(
                                   max_length=2000,
                                   null=False)
    created_time = models.DateTimeField(
                                        verbose_name='date et heure de création',
                                        auto_now_add=True)
    issue = models.ForeignKey(
                              Issue,
                              on_delete=models.CASCADE,
                              null=False)
    author = models.ForeignKey(
                               get_user_model(),
                               on_delete=models.CASCADE,
                               null=False)
