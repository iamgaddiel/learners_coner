from django.db import models
from core.models import CustomUser


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=100)
    flw_ref = models.CharField(max_length=150)
    tx_ref = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.tx_ref}"

