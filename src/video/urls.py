from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet
from .views import ListVideo, VideoViewSet


router = DefaultRouter(trailing_slash=False)
router.register('admin', VideoViewSet)

urlpatterns = [
    path('list/', ListVideo.as_view(), name="list_video")
]
urlpatterns += router.urls