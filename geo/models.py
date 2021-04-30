from django.db import models


class Cities(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    currency = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=100)