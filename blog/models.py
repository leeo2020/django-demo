from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Articles(models.Model):
    title = models.CharField('title', max_length=10)
    content = models.TextField('content', max_length=128, blank=True)
    createdTime = models.DateTimeField('createdTime')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

    def __str__(self):
        return self.title
