from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=50, unique=True)
    link = models.CharField(max_length=400, unique=True)

    def __str__(self) -> str:
        return self.title
