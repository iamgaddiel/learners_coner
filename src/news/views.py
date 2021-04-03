from django.shortcuts import render
from rest_framework import mixins, permissions, views, viewsets
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from .models import News
from .serializer import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class StudentRetrieveView(mixins.ListModelMixin, RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class StudentListView(ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = News.objects.all()
    serializer_class = NewsSerializer

