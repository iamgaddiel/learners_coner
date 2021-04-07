import json
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


class StudentNote(mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = StudentNoteSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Note.objects.all()
    

    def get(self, request, pk, owner):
        try:
            user = CustomUser.objects.get(id=owner)
            if Note.objects.filter(owner=user.id, id=pk).exists():
                note_qs = Note.objects.filter(owner=user.id, id=pk).values()[0]
                return Response(note_qs, status=status.HTTP_200_OK)
            else:
                return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk, owner):
        try:
            sq = self.serializer_class(data=request.data)
            if sq.is_valid():
                user_instance = CustomUser.objects.get(id=owner)
                notes_qs = Note.objects.filter(
                    owner=user_instance.pk, id=pk).update(**sq.data)
                return Response({"id": pk, **sq.data, "owner_id": user_instance.pk}, status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, owner):
        try:
            user_instance = CustomUser.objects.get(id=owner)
            notes_qs = Note.objects.get(
                owner=user_instance.pk, id=pk).delete()
            return Response({"success": "delete successful"}, status=status.HTTP_204_NO_CONTENT)

        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
        except Note.DoesNotExist:
            return Response({"error": "note not found"}, status=status.HTTP_404_NOT_FOUND)


class StudentNoteList(generics.GenericAPIView):
    serializer_class = StudentNoteSerializer
    def get(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(id=self.kwargs.get('owner'))
            notes_qs = Note.objects.filter(owner=user.id).values()
            sz = self.serializer_class(notes_qs, many=True)
            return Response(sz.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "owner not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, *args, **kwargs):
        sq = self.serializer_class(data=request.data)
        try:
            if sq.is_valid(raise_exception=True):
                user = CustomUser.objects.get(pk=self.kwargs.get('owner'))
                note = Note.objects.create(owner=user, **sq.data)
                return Response({"detail": "Note created successfully"}, status=status.HTTP_201_CREATED)
        except CustomUser.DoesNotExist:
            return Response({"error": "user not found"}, status=status.HTTP_201_CREATED)
