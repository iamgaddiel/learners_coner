from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Video
from .serializer import VideoSerializer


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = []
    authentication_classes = []
    queryset = Video.objects.all()
