from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    NoteViewSet,
    StudentNote
)


router = DefaultRouter()
router.register('admin', NoteViewSet)

urlpatterns = [
    path('<int:pk>/<int:owner>/', StudentNote.as_view(), name="user_get"),
    path('<int:owner>/', StudentNote.as_view(),name="user_note_list"),
    path('<int:pk>/<int:owner>/', StudentNote.as_view(),name="user_note_update"),
    path('<int:pk>/<int:owner>/', StudentNote.as_view(),name="user_note_delete"),
]

urlpatterns += router.urls