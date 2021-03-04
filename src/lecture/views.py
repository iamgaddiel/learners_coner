from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import views, mixins, permissions, viewsets
from rest_framework.serializers import Serializer
from .models import Lecture
from .serializer import LectureSerializer


class LectureTest(views.APIView):
    def get(self,*args, **kwargs):
        return Response({"data": "lectures working"})

class LectureView(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer()
    permission_classes = [
        permissions.IsAuthenticated,
        permissions.IsAdminUser
    ]

class StudentLecture(views.APIView):
    pass

