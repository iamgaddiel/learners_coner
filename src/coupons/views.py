from django.shortcuts import render
from rest_framework import viewsets, views, mixins, permissions
from .models import Coupons, School
from .serializer import SchoolSerializer, CouponsSerializer


class SchoolViewset(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = School.object.all()

