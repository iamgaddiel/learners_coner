from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.urls.base import reverse
from django.conf import settings

# RestframeWork
from rest_framework import (
    generics,
    mixins,
    permissions,
    serializers,
    authentication,
    viewsets,
    views,
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.request import QueryDict
from rest_framework.authtoken.views import ObtainAuthToken

from dj_rest_auth.registration.views import RegisterView, RegisterSerializer

# JWT
from rest_framework_simplejwt.tokens import RefreshToken
import jwt

from core.models import CustomUser
from core.serializers import CustomUserSerializer, PhoneNumberConfirmSerializer
from .utils import Util
from learner_conner.settings import EMAIL_HOST_USER


class UserRegistration(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

# Admin only


class Users(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]


class CustomAuthToken(ObtainAuthToken):
    # return more info when getting user token
    # THIS VIEW IS NOT IN USE
    # @params username, password
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.id,
            'username': user.username,
            'full_name': user.fullname,
            'phone': user.phone,
            'country': user.country,
            'level': user.level,
            'email': user.email,
            'role': user.role
        })


class Root(views.APIView):
    def get(self, *args, **kwargs):
        print(type(settings.SECRET_KEY))
        return Response({"data": "Working"}, status=200)


class PhoneNumberCheckView(views.APIView):
    def post(self, *args, **kwargs):
        sz = PhoneNumberConfirmSerializer(data=self.kwargs.get('phone'))
        if sz.is_valid():
            if (qs := CustomUser.objects.filter(phone=sz.validated_data.get('phone'))).exists():
                # if qs.exists():
                return Response({"status": 'error', "message": "phone number exists"})
        return Response({"status": "success", "message": "phone number found"})


class CustomLoginView(views.APIView):
    """
    @params [phone, password]
    @method POST
    @returns [username, token, user_id, username, full_name, phone, country, level, email, role]
    """

    def post(self, request, format=None) -> Response:

        # get phone and password
        phone = request.data.get('phone')
        password = request.data.get('password')

        try:
            # get user
            user = CustomUser.objects.get(phone=phone)
            if (password_check := check_password(password, user.password)):  # validate password
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'username'  : user.username,
                    'token'     : token.key,
                    'user_id'   : user.id,
                    'username'  : user.username,
                    'full_name' : user.fullname,
                    'phone'     : user.phone,
                    'country'   : user.country,
                    'level'     : user.level,
                    'email'     : user.email,
                    'role'      : user.role
                }, status=200)

            return Response({
                'status': "error",
                'message': 'wrong login credentials'
            }, status=401)

        except CustomUser.DoesNotExist:
            return Response({
                'error': 'user does not exits',  # None
            }, status=404)


class SendVerificationEmail(generics.GenericAPIView):
    """
    @DESC: sends email verification code to user's email
    @PARAMS: email
    @REQUEST Method: POST, GET
    @TODO: use POST method to get user email not get
    """
    # Send email verification
    def post(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.data.get('email'))
            jwt_token = RefreshToken.for_user(user).access_token # get JWT access token
            current_site_domain = get_current_site(request).domain #get sites domain
            relative_url = reverse('email_verification_confrim') # get the relative path to email verification
            absolute_url = f"http://{current_site_domain}{relative_url}?token={jwt_token}"
            # domain = f"http://{}"
            data = {
                'message'     : f"Hi {user.username} use the link below to verify your account \n {absolute_url}",
                'sender'      : settings.EMAIL_HOST_USER,
                'recipient'   : user.email,
                'subject'     : "Email Verification"
            }
            data.get('sender')
            Util.send_email(data)
            return Response({
                'data': 'check your email to verify account'
            })
        except CustomUser.DoesNotExist:
            return Response({"data": "user with this email does not exists"}, status=404)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user_token = request.GET.get('token')
        payload = jwt.decode(user_token, settings.SECRET_KEY)
        try:
            if not (user := CustomUser.objects.get(id=payload.get('user_id'))).is_verified:
                user.is_verified = True
                user.save()
            return Response({"data": "account successfully activated"})
        except jwt.ExpiredSignatureError:
            return Response({"error": "activation link has expired"}, status=400)
        except jwt.DecodeError:
            return Response({'error': "invalid token"}, status=400)

