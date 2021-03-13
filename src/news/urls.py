from django.conf.urls import url
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet


router = DefaultRouter()
router.register('admin', NewsViewSet)

urlpatterns = [] 
urlpatterns += router.urls
