from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import MockTest, MockTestQuestion


class MockTestSerializer(ModelSerializer):
    class Meta:
        model = MockTest
        fields = '__all__'

class MockTestQuestionSerializer(ModelSerializer):
    class Meta:
        model = MockTestQuestion
        fields = '__all__'

class MockTestDetailSerializer(ModelSerializer):
    class Meta:
        model = MockTest
        fields  = '__all__'
        