from django.conf.urls import url
from django.urls import path
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, StudentListView, StudentRetrieveView


router = DefaultRouter()
router.register('admin', NewsViewSet)

urlpatterns = [
    path('', StudentListView.as_view(), name="news-list"),
    path('<pk>/', StudentRetrieveView.as_view(), name="news-retrive")
] 
urlpatterns += router.urls
