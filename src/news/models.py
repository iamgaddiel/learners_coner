from django.db import models


class News(models.Model):
    title: str = models.CharField(max_length=50)
    source: str = models.CharField(max_length=50)
    link: str = models.CharField(max_length=50)

