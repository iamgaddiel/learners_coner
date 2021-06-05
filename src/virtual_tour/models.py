from django.db import models
from django.db.models.base import Model
from django.utils import timezone

class VirtualTour(models.Model):
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=400, unique=True)
    timestamp = models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return '{0}'.format(self.title)
