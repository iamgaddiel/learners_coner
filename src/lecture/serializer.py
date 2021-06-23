from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Lecture, Course


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'
        

class GetStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['level', 'subject', 'term', 'note', 'title']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
