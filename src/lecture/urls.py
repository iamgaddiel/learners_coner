from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    LectureTest,
    LectureViewSet,
    StudentLecture,
    GetAllLectures,
    CourseViewSet,
    ListCourse,
    GetCourse,
)

router = DefaultRouter()
router.register('admin', LectureViewSet)
router.register('course/admin', CourseViewSet)

urlpatterns = [
    path('user/detail/<str:level>/<str:subject>/<int:term>/', StudentLecture.as_view(), name="student_lecture"),
    path('list/', GetAllLectures.as_view(), name="lecture_list"),
    path('course/list/', ListCourse.as_view(), name="course_list"),
    path('course/get/<int:pk>/', GetCourse.as_view(), name="course_get"),
]

urlpatterns += router.urls