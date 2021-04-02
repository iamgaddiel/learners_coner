from django.db.models.base import Model
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions
from .models import Video
from .serializer import VideoSerializer


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Video.objects.all()

