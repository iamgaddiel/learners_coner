from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from core.models import CustomUser


class Notification(models.Model):
    MESSAGE_RECIPIENT = [
        ('students', 'students'),
        ('teachers', 'teachers'),
    ]
    subject = models.CharField(max_length=400)
    message = models.TextField()
    recipient = models.CharField(max_length=9, choices=MESSAGE_RECIPIENT)
    timestamp = models.DateTimeField(auto_now=timezone)

    def __str__(self) -> str:
        return self.subject
