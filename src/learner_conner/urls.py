from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls'))  # api,
]

# urlpatterns += [
#     path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login')
# ]