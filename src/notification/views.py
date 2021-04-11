from django.shortcuts import render
from rest_framework import views, viewsets
from core.models import CustomUser
from notification.serializer import NotificationSerializer
from .models import Notification

# Create your views here.
class Notification(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification

