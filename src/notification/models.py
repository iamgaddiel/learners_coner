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
        return f"{self.subject} - {self.timestamp}"

class UserNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user.username} notification {self.notification.timestamp}"