from rest_framework import serializers
from rest_framework import validators
from rest_framework.validators import ValidationError
from core.models import CustomUser, Profile
import referral


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list = [
            'username',
            'first_name',
            'last_name', 
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
        user = CustomUser(**validated_data)
        user.set_password(password)

        referral_code = validated_data.get('referral')
        if referral_code != '':
            referral_qs = Profile.objects.filter(referral_code=referral_code)
            if not referral_qs.exists():
                raise serializers.ValidationError("Referral Code doesn't exists")
        user.save()

        user_profile = Profile(user=user)
        user_profile.personal_referral_code = validated_data.get('phone')
        user_profile.save()
        return user


