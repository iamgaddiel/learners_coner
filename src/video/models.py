from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from classroom.models import Class

class Video(models.Model):
    TERM = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    ]
    title = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=400, unique=True)
    level = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    term = models.CharField(max_length=3, choices=TERM, default=TERM[0])

    def __str__(self) -> str:
        return f"{self.title} | level: {self.level} | term: {self.term}"
