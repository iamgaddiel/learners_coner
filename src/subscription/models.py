from django.db import models
from core.models import CustomUser


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    flw_ref = models.CharField(max_length=160)
    user_type = models.CharField(max_length=20)
    tx_ref = models.CharField(max_length=150)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.tx_ref}"

