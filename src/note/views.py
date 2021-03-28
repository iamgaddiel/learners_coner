from re import I
from django.shortcuts import render
from rest_framework import permissions, authentication, views, generics, mixins, viewsets
from rest_framework.response import Response

from core.models import CustomUser
from .models import Note
from .serializer import NoteSerializer, StudentNoteSerializer, StudentNoteSerializere


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

class StudentNote(generics.GenericAPIView):
    serializer_class = StudentNoteSerializer
    # permission_classes = [
    #     permissions.IsAuthenticated,
    # ]
    queryset = Note.objects.all()

    def get(self, request, *args, **kwargs):
        pass
    