from django.shortcuts import render
from rest_framework import permissions, mixins, viewsets, views
from core.models import CustomUser
from core.serializers import CustomUserSerializer


class Users(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]


