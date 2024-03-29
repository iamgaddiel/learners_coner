from django.db.models import fields
from django.urls import resolve, reverse
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import serializers
from rest_framework import validators
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.validators import ValidationError

# Project
from core.models import CustomUser, Profile
from core.utils import Util

# password reset
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, force_str, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# JWT
from rest_framework_simplejwt.tokens import RefreshToken
import jwt

# confirm email
# from verify_email.email_handler import send_verification_email
# import referral


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list = [
            'fullname',
            'phone',
            'country',
            'level',
            'password',
            'email',
            'role',
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

    def create(self, validated_data):

        # overide create method to hash user password
        password = validated_data.pop("password")
        phone = validated_data.get('phone')
        fullname = validated_data.get('fullname')
        user_role = validated_data.get('role')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.username = f'{fullname}-{phone}'

        # Check if inputted phone number exists
        referral_code = validated_data.get('referral_code')
        if referral_code is not None:
            if not (referral_qs := Profile.objects.filter(personal_referral_code=referral_code)).exists():
                # if not referral_qs.exists():
                raise serializers.ValidationError("Referral doesn't exists")
        if user_role == "admin":
            user.is_superuser = True
            user.is_staff = True
        user.save()

        # Creates user profile
        user_profile = Profile(user=user)
        user_profile.personal_referral_code = f'https://learnerscorner.org/signup?ref_code={phone}'
        user_profile.save()

        # send verification email to user
        try:
            jwt_token = RefreshToken.for_user(user).access_token  # get JWT access token
            current_site_domain = Util.get_host_domain(self.context['request'])
            relative_url = reverse('email_verification_confrim') # get the relative path to email verification
            absolute_url = f"{current_site_domain}{relative_url}?token={jwt_token}"
            
            data = {
                'message': f"Hi {user.username} use the link below to verify your account \n {absolute_url}",
                'sender': settings.EMAIL_HOST_USER,
                'recipient': user.email,
                'subject': "Email Verification"
            }
            Util.send_email(data)

            return user
        except CustomUser.DoesNotExist:
            return Response({"data": "user with this email does not exists"}, status=404)
        

class PhoneNumberConfirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields: list = ['phone']


class PasswordResetSerialier(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'address',
            'dob',
            'gender',
            'image'
        ]

class PasswordResetCompleteSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=1, max_length=20, write_only=True)
    password_confirm = serializers.CharField(min_length=1, max_length=20, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'confirm_password', 'uidb64', 'token']
    
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password_confrim = attrs.get('password_confirm')
            uidb64 = attrs.get('uidb64')
            token = attrs.get('token')
            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            # check if link has been used before
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('invalid token, kindly request a new one', 404)

            # password comparison
            if password != password_confrim:
                raise AuthenticationFailed('Passwords do not match', 404)
            
            user.set_password(password)
            user.save()

        except DjangoUnicodeDecodeError as e:
            return Response({'error', 'altered token, kindly request a new one'})

        return super().validate(attrs)


class LoggedInPasswordResetSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    old_password = serializers.CharField(min_length=4, write_only=True)
    new_password = serializers.CharField(min_length=4, write_only=True)
    confirm_new_password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        fields = ['user', 'old_password', 'new_password', 'confirm_new_password']


class GetStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]

class GetTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]
