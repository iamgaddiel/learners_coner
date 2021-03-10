from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    LectureTest,
    LectureViewSet,
    StudentLecture
)

router = DefaultRouter()
router.register('admin', LectureViewSet)

urlpatterns = [
    path('', LectureTest.as_view(), name="lect"),
    path('user/detail/<str:level>/<str:subject>/<int:term>/', StudentLecture.as_view(), name="student_lecture"),
]

urlpatterns += router.urls