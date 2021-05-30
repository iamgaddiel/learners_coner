from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import (
    views, 
    permissions,
    authentication, 
    parsers
)
from .models import Podcast
from .serializer import PodcastSerializer


class PodcastViewSet(ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

class PodcastGetAllView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        podcasts = Podcast.objects.all()
        serializer = PodcastSerializer(podcasts, many=True)
        return Response(serializer.data, status=202)

class PodcastGetView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, *args, **kwargs):
        podcasts = Podcast.objects.all(id=self.kwargs.get('id'))
        serializer = PodcastSerializer(podcasts, many=True)
        return Response(serializer.data, status=202)

class PodcastTestView(views.APIView):
    def get(self, *args, **kwargs):
        return Response({"data": "podcast working"})