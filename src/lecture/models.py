from django.db import models
from _class.models import Class
from ckeditor.fields import RichTextField


class Lecture(models.Model):
    title = models.CharField(max_length=30, unique=True)
    note = RichTextField(blank=True, null=True)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    week = models.CharField(max_length=2, help_text="lecture week")
    timestamp = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
