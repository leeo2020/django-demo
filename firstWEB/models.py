from __future__ import unicode_literals
from django.db import models


# Create your models here.

class Cal(models.Model):
    value_a = models.CharField(max_length=10)
    value_b = models.CharField(max_length=10)
    result = models.CharField(max_length=10)


class Stastics(models.Model):
    value_a = models.CharField(max_length=10)
    value_b = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
