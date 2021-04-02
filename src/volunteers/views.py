from django.shortcuts import render
from rest_framework import permissions, serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Volunteer
from .serializer import VolunteerSerializer

class VolunteerViewSet(ModelViewSet):
    queryset = Volunteer
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = VolunteerSerializer
