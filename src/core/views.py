from django.contrib.auth.hashers import check_password
from django.contrib.sites.shortcuts import get_current_site
from django.urls.base import reverse
from django.conf import settings
from django.contrib.auth.hashers import check_password

# password reset
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, force_str, smart_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


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
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.request import QueryDict
from rest_framework.authtoken.views import ObtainAuthToken

from dj_rest_auth.registration.views import RegisterView, RegisterSerializer
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# JWT
from rest_framework_simplejwt.tokens import RefreshToken
import jwt

from core.models import CustomUser, Profile
from core.serializers import (
    CustomUserSerializer, 
    PasswordResetCompleteSerializer, 
    PasswordResetSerialier, 
    PhoneNumberConfirmSerializer, 
    ProfileUpdateSerializer,
    LoggedInPasswordResetSerializer
)
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


class UserProfileUpdate(generics.UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    lookup_field = "user"

    def perform_update(self, serializer):
        user_update_fields = [
            'fullname',
            'phone',
            'level',
            'country',
            'role',
        ]
        
        for data in self.request.data:
            if data in user_update_fields:
                try:
                    phone = self.request.data.get('phone')
                    fullname = self.request.data.get('fullname')
                    level = self.request.data.get('level')
                    country = self.request.data.get('country')
                    role = self.request.data.get('role')
                    user = CustomUser.objects.get(id=self.kwargs.get('user'))

                    if phone is not None:
                        user.phone = phone
                    if fullname is not None:
                        user.fullname = fullname
                    if level is not None:
                        user.level = level
                    if country is not None:
                        user.country = country
                    if role is not None:
                        user.role = role
                    user.save()

                except CustomUser.DoesNotExist:
                    return Response({"error": "user does not exist"})
        return super().perform_update(serializer)


class Root(views.APIView):
    def get(self, *args, **kwargs):
        print(type(settings.SECRET_KEY))
        return Response({
            "data": "Working", 
            "domain": self.request.get_host(),
            "email_host": settings.EMAIL_HOST_USER
        },status=200)


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
                    'username': user.username,
                    'token': token.key,
                    'user_id': user.id,
                    'username': user.username,
                    'full_name': user.fullname,
                    'phone': user.phone,
                    'country': user.country,
                    'level': user.level,
                    'email': user.email,
                    'role': user.role,
                    'is_verified': user.is_verified,
                    'is_subscribed': user.is_subscribed,
                    'image': user.profile.image,
                    'address': user.profile.address,
                    'dob': user.profile.dob,
                    'gender': user.profile.gender,
                    'personal_referral_code': user.profile.personal_referral_code
                }, status=200)

            return Response({
                'status': "error",
                'message': 'wrong login credentials'
            }, status=401)

        except CustomUser.DoesNotExist:
            return Response({
                'error': 'user does not exits',  # None
            }, status=404)


class VerifyEmail(generics.GenericAPIView):
    """
    @DESC: sends email verification code to user's email
    @PARAMS: email
    @REQUEST Method: POST, GET
    @TODO: add a serializer class
    """
    # Send email verification
    serializer_class = PasswordResetSerialier

    def post(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.data.get('email'))
            jwt_token = RefreshToken.for_user(
                user).access_token  # get JWT access token
            current_site_domain = Util.get_host_domain(request)
            relative_url = reverse('email_verification_confrim') # get the relative path to email verification
            absolute_url = f"{current_site_domain}{relative_url}?token={jwt_token}"
            
            data = {
                'message': f"Hi {user.username} use the link below to verify your account \n {absolute_url}",
                'sender': settings.EMAIL_HOST_USER,
                'recipient': user.email,
                'subject': "Email Verification"
            }
            Util.send_email(data)

            return Response({
                'data': "check your email to verify account, if it's not there then check your spam"
            })
        except CustomUser.DoesNotExist:
            return Response({"data": "user with this email does not exists"}, status=404)


class VerifyEmailConfirm(views.APIView):
    def get(self, request, *args, **kwargs):
        user_token = request.GET.get('token')
        payload = jwt.decode(user_token, settings.SECRET_KEY, ['HS256'])
        try:
            if not (user := CustomUser.objects.get(id=payload.get('user_id'))).is_verified:
                user.is_verified = True
                user.save()
            return Response({"data": "account successfully activated"})
        except jwt.ExpiredSignatureError:
            return Response({"error": "activation link has expired"}, status=400)
        except jwt.DecodeError:
            return Response({'error': "invalid token"}, status=400)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class PasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerialier

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            if CustomUser.objects.filter(email=email).exists():

                user = CustomUser.objects.get(email=email)
                uidb64 = urlsafe_base64_encode(str(user.id).encode('utf-8'))
                token = PasswordResetTokenGenerator().make_token(user)
                # current_site_domain = Util.get_host_domain(request)

                # relative_url = reverse(
                #     'password_reset_confirm', kwargs={
                #         'uidb64': uidb64, 'token': token
                #     })  # get the relative path to email verification

                # absolute_url = f"{current_site_domain}{relative_url}"
                absolute_url = f'https://www.learnerscorner.org/new-password?uidb64={uidb64}&token={token}'

                data = {
                    'message': f"Hi \n use the link below to reset your password \n {absolute_url}",
                    'sender': settings.EMAIL_HOST_USER,
                    'recipient': user.email,
                    'subject': "Password Reset"
                }
                print(data['sender'])
                Util.send_email(data)
                return Response({
                    "success": "Check mail your we've sent you a link to reset your password, if you don't find it check your spam"
                })
            else:
                return Response({"error": "Your email was not found"})

class PasswordResetConfrimView(views.APIView):
    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error', 'invalid token, kindly request a new one'})

            return Response({
                "success": True,
                "message": "Credential valid",
                "uidb64": uidb64,
                "token": token
            })

            #TODO redirect to front end link /new-password/ on success
            #TODO 

        except DjangoUnicodeDecodeError as e:
            return Response({'error', 'altered token, kindly request a new one'})

class PasswordResetCompleteView(generics.GenericAPIView):
    serializer_class = PasswordResetCompleteSerializer
    
    def patch(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                "success": True,
                "message": "password reset successful"
            }, status=status.HTTP_200_OK)


class LoggedInPasswordResetView(generics.GenericAPIView):
    serializer_class = LoggedInPasswordResetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user_id = serializer.data.get('user')
                old_password = serializer.data.get('old_password')
                new_password = serializer.data.get('new_password')
                confirm_new_password = serializer.data.get('confirm_new_password')
                user = CustomUser.objects.get(id=user_id)


                # Password comparison
                if check_password(old_password, user.password):
                    if new_password == confirm_new_password:
                        user.set_password(new_password)
                        user.save()
                        return Response({"success": "Password updated successfully"}, status=status.HTTP_205_RESET_CONTENT)
                    else:
                        return Response({"error": "passwords do not match"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"error": "invalid old password"}, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist as e:
                return Response({"error": "invalid user"}, status=status.HTTP_400_BAD_REQUEST)