from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Volunteer


class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'

