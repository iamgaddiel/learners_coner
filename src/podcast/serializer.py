from rest_framework import serializers
from .models import Podcast


class PodcastSerializer(serializers.Serializer):
    class Meta:
        model = Podcast
        fields = '__all__'
