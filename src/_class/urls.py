from django.urls import path
from rest_framework.routers import DefaultRouter
from _class.views import SubjectViewSet, ClassViewSet

router = DefaultRouter(trailing_slash=True)
router.register('subjects', SubjectViewSet, 'subjects')
router.register('classes', ClassViewSet, 'student_class')


urlpatterns = []

urlpatterns += router.urls

