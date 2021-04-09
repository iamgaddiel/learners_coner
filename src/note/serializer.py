from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Note
from core.models import CustomUser


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'content', 'owner']

class StudentNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'owner_id']
