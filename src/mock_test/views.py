from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import MockTestDetailSerializer, MockTestQuestionSerializer, MockTestSerializer
from .models import MockTest, MockTestQuestion
import json


class MockTestViewSet(ModelViewSet):
    queryset = MockTest.objects.all()
    serializer_class = MockTestSerializer
    permission_classes = [IsAuthenticated]

class MockTestQuestionViewSet(ModelViewSet):
    queryset = MockTestQuestion.objects.all()
    serializer_class = MockTestQuestionSerializer
    permission_classes = [IsAuthenticated]

class ListMockTestQuestions(GenericAPIView):
    serializers = MockTestDetailSerializer

    def get(self, request, pk):
        try:
            mock_test = MockTest.objects.filter(pk=pk).values()
            mock_test_question = MockTestQuestion.objects.filter(mock_test=mock_test.pk).values()
            return Response({
                "mock_test": mock_test,
                "mock_test_questions": mock_test_question
            }, status=status.HTTP_200_OK)
        except MockTest.DoesNotExist as e:
            return Response({"error": "Mock Test was not found"}, status=status.HTTP_404_NOT_FOUND)
        except MockTestQuestion.DoesNotExist:
            return Response({"error": "No Mock Test Questions not found"}, status=status.HTTP_404_NOT_FOUND)
