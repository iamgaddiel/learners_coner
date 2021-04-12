from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification, UserNotification


@receiver(post_save, sender=Notification)
def create_notification(sender, created, **kwargs):
    pass