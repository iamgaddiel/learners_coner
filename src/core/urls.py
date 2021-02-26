from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import (
    UserRegistration,
    CustomAuthToken
)

router = DefaultRouter()

urlpatterns = [
    path('user/register/', UserRegistration.as_view(), name='user_registration'),
    path('user/login/', CustomAuthToken.as_view(), name='auth-login'),
    path('classroom/', include('_class.urls')),

    # drf
    path('auth/', include('rest_framework.urls')),

    # dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    
]

urlpatterns += router.urls