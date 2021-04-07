from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path

from mock_test.views import MockTestQuestionViewSet, MockTestViewSet, ListMockTestQuestions


router = DefaultRouter()
router.register('mocktest', MockTestViewSet)
router.register('mocktest_question', MockTestQuestionViewSet)

urlpatterns = [
    path('mocktest/verbose/<int:pk>/', ListMockTestQuestions.as_view(), name="mock_test_verbose")
]
urlpatterns += router.urls