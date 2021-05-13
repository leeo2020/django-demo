from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('name', max_length=25)


class Tags(models.Model):
    name = models.CharField('tag', max_length=20)


class Author(models.Model):
    name = models.CharField('author', max_length=15)


class Articles(models.Model):
    title = models.CharField('title', max_length=10)
    intro = models.TextField('abstract', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', default='1')
    tags = models.ManyToManyField(Tags, blank=True)
    content = models.TextField('content')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, verbose_name='author', default='1')
    createdTime = models.DateTimeField('createdTime')

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'article'

    def __str__(self):
        return self.title
