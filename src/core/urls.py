from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.views import (
    CustomLoginView, UserRegistration,
    Root,
    PhoneNumberCheckView,
)

router = DefaultRouter()

urlpatterns = [
    path('user/register/', UserRegistration.as_view(), name='user_registration'),
    path('user/login/', CustomLoginView.as_view(), name='custom-login'),
    path('user/phone/confirm/', PhoneNumberCheckView.as_view(), name='phone_confirm'),
    path('classroom/', include('classroom.urls')),
    path('', Root.as_view(), name="root"),

    # drf
    path('auth/', include('rest_framework.urls')),

    # dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('lecture/', include('lecture.urls')),
    path('news/', include('news.urls')),
    path('note/', include('note.urls'))
    # path('podcast/', include('podcast.urls')),
]

urlpatterns += router.urls