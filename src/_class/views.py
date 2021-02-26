from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# custom import
from _class.models import Subject, Class
from _class.serializer import ClassSerializer, SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
