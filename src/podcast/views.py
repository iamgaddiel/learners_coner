from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
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
    serializers = PodcastSerializer
    parser_classes = [
        parsers.FormParser,
        # parsers.FileUploadParser,
    ]
    permission_classes = [
        permissions.AllowAny
    ]
    # authentication_classes = [
    #     permissions.IsAuthenticated,
    #     permissions.IsAdminUser
    # ]

class PodcastTestView(views.APIView):
    def get(self, *args, **kwargs):
        return Response({"data": "podcast working"})