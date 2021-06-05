from rest_framework import serializers
from .models import VirtualTour


class VirtualTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = VirtualTour
        fields = '__all__'
