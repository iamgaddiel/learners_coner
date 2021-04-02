from django.urls import path
from rest_framework.routers import DefaultRouter

from volunteers.views import VolunteerViewSet


router = DefaultRouter()
router.register('admin', VolunteerViewSet)

urlpattern = []
urlpattern += router.urls