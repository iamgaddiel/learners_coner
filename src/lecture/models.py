from django.db import models
from classroom.models import Class, Subject
from ckeditor.fields import RichTextField


class Lecture(models.Model):
    title = models.CharField(max_length=70, unique=True, default='')
    note = RichTextField(blank=True, null=True)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    term = models.IntegerField(default=1)
    week = models.PositiveIntegerField(help_text="lecture week")
    timestamp = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return r'{self.title} week {week}'
