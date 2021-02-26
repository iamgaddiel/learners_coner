from rest_framework import serializers
from _class.models import Class, Subject

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['title']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title']

