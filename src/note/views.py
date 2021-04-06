from re import I
from django.shortcuts import render
from rest_framework import permissions, authentication, serializers, status, views, generics, mixins, viewsets
from rest_framework.response import Response
from classroom import serializer

from core.models import CustomUser
from .models import Note
from .serializer import NoteSerializer, StudentNoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]


class StudentNote(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = StudentNoteSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Note.objects.all()

    
    def create(self, request, *args, **kwargs):
        sq = self.serializer_class(data=request.data)
        if sq.is_valid(raise_exception=True):
            note = Note.objects.create(**sq.data)
            return Response(note, status=status.status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(id=self.kwargs.get('owner'))
            notes_qs = Note.objects.filter(owner=user.id)
            return Response(notes_qs, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, owner):
        try:
            user = CustomUser.objects.get(id=owner)
            notes_qs = Note.objects.get(owner=user.id, id=pk)
            return Response(notes_qs, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, owner):
        try:
            sq = self.serializer_class(data=request.data)
            if sq.is_valid():
                user = CustomUser.objects.get(id=owner)
                notes_qs = Note.objects.get(
                    owner=user.id, id=pk).update(**sq.data)
                return Response(sq.data, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, owner):
        try:
            user = CustomUser.objects.get(id=owner)
            notes_qs = Note.objects.get(
                owner=user.id, id=pk).delete()
            return Response(notes_qs, status=status.status.HTTP_204_NO_CONTENT)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)
