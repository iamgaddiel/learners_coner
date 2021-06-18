from django.shortcuts import render
from rest_framework import viewsets, views, mixins, permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.models import CustomUser
from .models import Coupons, School
from .serializer import SchoolSerializer, CouponsSerializer, StudentCouponRegistrationSerializer


class SchoolViewset(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]
    queryset = School.objects.all()

class StudentCouponRegistrationView(GenericAPIView):
    queryset = Coupons.objects.all()
    serializer_class = StudentCouponRegistrationSerializer
    def post(self, request, *args, **kwargs):
        if (sz := self.serializer_class(data=request.data)).is_valid():
            try:
                Coupons.objects.get(coupon_code=sz.data.get('coupon'))
                user = CustomUser.objects.get(id=sz.data.get('user'))
                user.is_subscribed = True
                user.save()
                return Response({"data": "subscription successful"}, status=status.HTTP_200_OK)

            except CustomUser.DoesNotExist:
                return Response({"error": "User was not found"}, status=status.HTTP_404_NOT_FOUND)
            except Coupons.DoesNotExist:
                return Response({"error": "School with this coupon code was not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            print(request.data)
            return Response({'error': 'Invalid parameters sent'}, status=status.HTTP_404_NOT_FOUND)