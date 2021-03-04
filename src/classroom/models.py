from django.db import models


class Class(models.Model):
    title = models.CharField(max_length=4, unique=True)

    def __str__(self) -> str:
        return self.title

class Subject(models.Model):
    title = models.CharField(max_length=25, unique=True)
    classes = models.ManyToManyField(Class)

    def __str__(self) -> str:
        return self.title

