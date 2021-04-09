from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from core.models import CustomUser


class Notification(models.Model):
    subject = models.CharField(max_length=400)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=timezone)

    def __str__(self) -> str:
        return self.subject
