from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VirtualTourViewSet, VirtualTourClientView


router = DefaultRouter()
router.register('admin', VirtualTourViewSet)

urlpatterns = [
    path('get/', VirtualTourClientView.as_view(), name="get_virtual_tour")
]

urlpatterns += router.urls