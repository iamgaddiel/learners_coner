from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    NoteViewSet,
    StudentNote,
    StudentNoteList
)


router = DefaultRouter()
router.register('admin', NoteViewSet)

urlpatterns = [
    path('user/<int:owner>/', StudentNoteList.as_view(),name="user_note_list"),
    path('user/<int:owner>/', StudentNoteList.as_view(), name="user_note_post"),
    path('user/<int:pk>/<int:owner>/', StudentNote.as_view(), name="user_note_get"),
    path('user/<int:pk>/<int:owner>/', StudentNote.as_view(),name="user_note_update"),
    path('user/<int:pk>/<int:owner>/', StudentNote.as_view(),name="user_note_delete"),
]

urlpatterns += router.urls