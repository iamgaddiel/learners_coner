from django.urls import path
import rest_framework
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import SchoolViewset

router = DefaultRouter()
router.register('admin/', SchoolViewset)

urlpatterns = []
urlpatterns += router.urls
