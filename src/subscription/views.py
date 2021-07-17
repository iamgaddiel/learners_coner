from django.shortcuts import get_list_or_404, get_object_or_404, render
from core.models import CustomUser
from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from .models import Subscription
from .serializer import SubscriptionSerializer, SubscriptionDetailSerializer


class SubscriptionViewSet(ModelViewSet):
    permission_classes = [
        IsAuthenticated, IsAdminUser
    ]
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()


class GetSubscriptionDetail(GenericAPIView):
    query_set = Subscription.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]
    serializer_class = SubscriptionDetailSerializer

    def get(self, request, *args, **kwargs) -> None: 
        get_subscription: Subscription = get_object_or_404(Subscription, id = kwargs.get('id'))
        users: list = get_list_or_404(CustomUser, is_subscribed=True)
        this_subscription_users: list = []
        
        for user in users:
            if user.subscription.tx_ref == get_subscription.tx_ref:
                detail: dict = {
                    'fullname': user.fullname,
                    'email': user.email,
                    'user_type': user.role,
                    'payment_type': get_subscription.payment_type,
                    'flw_ref': user.subscription.flw_ref,
                    'tx_ref': user.subscription.tx_ref,
                    'amount': user.subscription.amount,
                    'subscription_data': user.subscription.subscription_data,
                    'duration': user.subscription.duration,
                    'expiration_date': user.subscription.expiration_date
                }
                this_subscription_users.append(detail)
        return Response({"error": this_subscription_users}, stauts=status.HTTP_200_OK)
        
class SubscriptionView(CreateModelMixin, GenericAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class GetSubscriptionFullDetails(GenericAPIView):
#     permission_classes = [
#         IsAuthenticated, IsAdminUser
#     ]
#     serializer_class = SubscriptionSerializer
#     queryset = Subscription.objects.all()

#     def get(self, request, *args, **kwargs):
#         subscriptions = self.serializer()
#         return Response(, status=status.HTTP_200_OK))