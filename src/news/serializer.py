from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import News


class NewsSerializer(ModelSerializer):
    model = News
    fields = '__all__'
