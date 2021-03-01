from django.shortcuts import render
from rest_framework import generics, mixins, permissions, viewsets
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from dj_rest_auth.registration.views import RegisterView, RegisterSerializer

from core.models import CustomUser
from core.serializers import CustomUserSerializer


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