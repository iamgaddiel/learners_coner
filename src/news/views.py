from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import News
from .serializer import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer


