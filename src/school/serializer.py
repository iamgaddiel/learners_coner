from django.db.models import fields
from rest_framework import serializers
from .models import School, Coupons


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    pass
