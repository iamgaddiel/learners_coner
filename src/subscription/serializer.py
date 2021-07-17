from django.db.models import fields
from django.db.models.base import Model
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .models import Subscription
from core.models import CustomUser


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            'user'
            # 'payment_type',
            # 'flw_ref',
            # 'user_type',
            # 'tx_ref',
            # 'amount',
            # 'duration',
            # 'subscription_date',
        ]


    def create(self, validated_data):
        # Check if user exists
        try:
            get_user = validated_data.get('user')
            user = CustomUser.objects.get(id=get_user.id)
            user.is_subscribed = True
            user.save()
        except CustomUser.DoesNotExist:
            return Response({"error": "user dose not exist"})
        return super().create(validated_data)


class SubscriptionDetailSerializer(ModelSerializer):
    class Meta:
        model  = Subscription
        fields  = '__all__'