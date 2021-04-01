from django.urls import path
from email_verification.views import TestEmailVerification


urlpatterns = [
    path('', TestEmailVerification.as_view(), name="test_email_verification")
]