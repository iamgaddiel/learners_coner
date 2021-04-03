from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Subscription
from .serializer import SubscriptionSerializer


class SubscriptionViewSet(ListModelMixin, DestroyModelMixin, GenericAPIView):
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SubscriptionView(CreateModelMixin, GenericAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
