from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet
from .views import VideoViewSet


router = DefaultRouter()
router.register('', VideoViewSet)

urlpatterns = []
urlpatterns += router.urls