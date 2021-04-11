from django.db.models import fields
from rest_framework import serializers
from .models import School, Coupons

import shortuuid


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def create(self, validated_data):
        school = School(**validated_data)
        school.save()

        coupons = Coupons.objects.create(
            coupon_code = shortuuid.ShortUUID().random(length=10),
            school = school
        )
        coupons.save()
        return school

class SchoolSerializer(serializers.ModelSerializer):
    pass
