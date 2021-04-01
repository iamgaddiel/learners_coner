from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class TestEmailVerification(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'data': 'email verification working'})