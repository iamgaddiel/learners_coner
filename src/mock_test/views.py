from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import MockTestQuestionSerializer, MockTestSerializer
from .models import MockTest, MockTestQuestion


class MockTestViewSet(ModelViewSet):
    queryset = MockTest.objects.all()
    serializer_class = MockTestSerializer
    permission_classes = [IsAuthenticated]

class MockTestQuestionViewSet(ModelViewSet):
    queryset = MockTestQuestion.objects.all()
    serializer_class = MockTestQuestionSerializer
    permission_classes = [IsAuthenticated]
