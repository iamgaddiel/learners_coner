from django.urls import path
from rest_framework.routers import DefaultRouter
from classroom.views import StudentSubject, SubjectViewSet, ClassViewSet

router = DefaultRouter(trailing_slash=True)
router.register('admin/subjects', SubjectViewSet, 'subjects')
router.register('admin/classes', ClassViewSet, 'student_class')


urlpatterns = [
    path('user/subject/list/', StudentSubject.as_view(), name='subject_list'),
]

urlpatterns += router.urls

