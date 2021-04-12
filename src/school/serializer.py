from django.db.models import fields
from rest_framework import serializers
from .models import School, Coupons


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    pass

class StudentCouponRegistrationSerializer(serializers.Serializer):
    coupon = serializers.CharField(max_length=10)
    user = serializers.CharField(max_length=99999)

    class Meta:
        fields = ['coupon', 'user']
