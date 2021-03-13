from collections import defaultdict
from django.urls import path
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import PodcastViewSet


router = DefaultRouter()
router.register('admin', PodcastViewSet)

urlpatterns  = []

urlpatterns += router.urls