from django.db import models
from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import MockTest, MockTestQuestion


class MockTestSerializer(ModelSerializer):
    models = MockTest
    fields = '__all__'

class MockTestQuestionSerializer(ModelSerializer):
    models = MockTestQuestion
    fields = '__all__'