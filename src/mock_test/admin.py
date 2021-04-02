from django.contrib import admin
from .models import MockTest, MockTestQuestion


admin.site.register(MockTestQuestion)
admin.site.register(MockTest)
