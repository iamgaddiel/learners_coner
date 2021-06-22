from django.urls import path
import rest_framework
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import SchoolViewset, StudentCouponRegistrationView

router = DefaultRouter()
router.register('admin', SchoolViewset)

urlpatterns = [
    path('coupon/subscription/', StudentCouponRegistrationView.as_view(), name="coupon_subscription")
]
urlpatterns += router.urls
