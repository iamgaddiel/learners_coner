from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
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

from core.models import CustomUser
from core.serializers import CustomUserSerializer, PhoneNumberConfirmSerializer


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
    # THIS CLASS IS NOT IN USE
    # @params username, password
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get("user")
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token'     : token.key,
            'user_id'   : user.id,
            'username'  : user.username,
            'full_name' : user.fullname,
            'phone'     : user.phone,
            'country'   : user.country,
            'level'     : user.level,
            'email'     : user.email,
            'role'      : user.role
        })

class Root(views.APIView):
    def get(self, *args, **kwargs):
        return Response({"data": "Working"}, status=200)

class PhoneNumberCheckView(views.APIView):
    def post(self, *args, **kwargs):
        sz = PhoneNumberConfirmSerializer(data=self.kwargs.get('phone'))
        if sz.is_valid():
            qs = CustomUser.objects.filter(phone=sz.validated_data.get('phone'))
            if qs.exists():
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
            if (password_check := check_password(password, user.password)): # validate password
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'username': user.username,
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
