from django.db.models import fields
from rest_framework import serializers

from core.models import CustomUser
from .models import Notification, UserNotification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

    def create(self, validated_data):
        recipient = validated_data.get('recipient')
        notification = Notification.objects.create(validated_data)
        notification.save()
        try:
            # create users notification
            if recipient == "students":
                for student in (students := CustomUser.objects.filter(role="student")):
                    user_notification = UserNotification.objects.create(
                        user = student.id,
                        notification = notification.id
                    )
                    user_notification.save()
            
            if recipient == "teachers":
                for teacher in (teachers := CustomUser.objects.filter(role="teacher")):
                    user_notification = UserNotification.objects.create(
                        user = teacher.id,
                        notification = notification.id
                    )
                    user_notification.save()
        except CustomUser.DoesNotExist:
            print("not user with the query exists")
        return notification
