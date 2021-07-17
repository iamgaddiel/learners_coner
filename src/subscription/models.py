from django.db import models
from core.models import CustomUser

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    flw_ref = models.CharField(max_length=160)
    user_type = models.CharField(max_length=20, blank=True)
    tx_ref = models.CharField(max_length=150)
    subscription_date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(default=0.0)
    expiration_date = models.DateField(blank=True, null=True)
    duration = models.PositiveIntegerField(default=3)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.tx_ref}"

    def save(self, *args, **kwargs) -> None:
        from datetime import date
        from dateutil.relativedelta import relativedelta as reldate
        self.expiration_date = self.subscription_date + reldate(months=+self.duration)
        return super().save()

