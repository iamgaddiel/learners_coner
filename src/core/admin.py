from django.contrib import admin
from core.models import CustomUser, Profile


admin.site.register(CustomUser)
admin.site.register(Profile)

