from django.db.models.base import Model
from django.shortcuts import render_to_response
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import Subscription
from core.models import CustomUser


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


    def create(self, validated_data):
        # Check if user exists
        try:
            user_id = validated_data.get('user')
            user = CustomUser.objects.get(id=user_id)
            user.is_subscribed = True
            user.save()
        except CustomUser.DoesNotExist:
            return Response({"error": "user dose not exist"})
        return super().create(validated_data)