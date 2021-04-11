from django.contrib import admin
from .models import Notification, UserNotification

# Register your models here.
admin.site.register(Notification)
admin.site.register(UserNotification)