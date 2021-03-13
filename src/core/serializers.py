from django.db.models import fields
from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import ValidationError
from core.models import CustomUser, Profile
import referral


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list = [
            # 'username',
            'fullname',
            'phone', 
            'country',
            'level',
            'password',
            'email',
            'referral_code',
        ]
        extra_kwargs = {
            "password": {
                "write_only": True, 
                'style': {
                    'input_type': 'password'
                }
            },
        }
        # validators: list = [sereferral_code_exists]

    def create(self, validated_data):

        # overide create method to hash user password 
        password = validated_data.pop("password")
        phone = validated_data.get('phone')
        fullname = validated_data.get('fullname')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.username = f'{fullname}-{phone}'

        # Check if inputted phone number exists
        referral_code = validated_data.get('referral_code')
        if referral_code is not None:
            referral_qs = Profile.objects.filter(personal_referral_code=referral_code)
            if not referral_qs.exists():
                raise serializers.ValidationError("Referral Code doesn't exists")
        user.save()
        
        # Creates user profile
        user_profile = Profile(user=user)
        user_profile.personal_referral_code = f'https://learners-corner.netlify.app/signup?ref_code{phone}'
        user_profile.save()
        return user

class PhoneNumberConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list = ['phone']

