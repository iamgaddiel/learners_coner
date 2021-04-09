from rest_framework.routers import DefaultRouter
from django.urls import path, include
from core.serializers import ProfileUpdateSerializer
from core.views import (
    CustomLoginView, 
    LoggedInPasswordResetView, 
    PasswordResetConfrimView, 
    PasswordResetView,
    UserProfileUpdate, 
    UserRegistration,
    Root,
    PhoneNumberCheckView,
    VerifyEmail,
    VerifyEmailConfirm,
    FacebookLogin,
    PasswordResetCompleteView
)

router = DefaultRouter()

urlpatterns = [
    path('user/register/', UserRegistration.as_view(), name='user_registration'),
    path('user/login/', CustomLoginView.as_view(), name='custom-login'),
    path('user/phone/confirm/', PhoneNumberCheckView.as_view(), name='phone_confirm'),
    path('user/profile/<int:user>/update/', UserProfileUpdate.as_view(), name="profile_update"),
    path('email/verification/', VerifyEmail.as_view(), name="send_email_verification"),
    path('email/verification/confirm/', VerifyEmailConfirm.as_view(), name="email_verification_confrim"),
    path('classroom/', include('classroom.urls')),
    path('', Root.as_view(), name="root"),

    # Facebook login
    path('auth/facebook', include('rest_framework_social_oauth2.urls')),
    # path('auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    # path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    
    # password reset urls
    path('password-reset/', PasswordResetView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfrimView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # logged in password reset
    path('user/password-reset/', LoggedInPasswordResetView.as_view(), name="logged_in_password_reset"),
    # drf
    path('auth/', include('rest_framework.urls')),

    # dj-rest-auth
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('lecture/', include('lecture.urls')),
    path('news/', include('news.urls')),
    path('note/', include('note.urls')),
    path('mock/', include('mock_test.urls')),
    path('video/', include('video.urls')),
    path('volunteers/', include('volunteers.urls')),
    path('subscription/', include('subscription.urls')),
    path('classroom/', include('classroom.urls')),
    # path('email/verification/', include('email_verification'))
    # path('podcast/', include('podcast.urls')),
]
urlpatterns += router.urls