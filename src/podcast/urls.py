from collections import defaultdict
from django.urls import path
from rest_framework import urlpatterns
from rest_framework import routers
from rest_framework.routers import DefaultRouter
# from .views import (PodcastViewSet, PodcastGetAllView, PodcastGetView) #this app is deactivated in the settings


router = DefaultRouter()
# router.register('admin', PodcastViewSet)

urlpatterns  = [
    # path('get/all/', PodcastGetAllView.as_view(), name="podcast_get")
]

urlpatterns += router.urls