from django.db import models
from classroom.models import Class

class Video(models.Model):
    TERM = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    title = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=400, unique=True)
    level = models.ForeignKey(Class, on_delete=models.CASCADE)
    term = models.CharField(max_length=3, choices=TERM)

    def __str__(self) -> str:
        return f"{self.title} | level: {self.level} | term: {self.term}"
