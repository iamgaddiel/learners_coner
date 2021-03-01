from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    LectureTest
)

router = DefaultRouter()

# router.register('')

urlpatterns = [
    path('', LectureTest.as_view(), name="lect"),
]