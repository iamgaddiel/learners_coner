from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GetStudentNote, GetStudentNotes, NoteViewSet


router = DefaultRouter()
router.register('', NoteViewSet)

urlpatterns = [
    path('user/<phone>/', GetStudentNotes.as_view(),name="user_note_list"),
    path('user/<int:pk>/<owner>/', GetStudentNote.as_view(), name="user_note")
]

urlpatterns += router.urls