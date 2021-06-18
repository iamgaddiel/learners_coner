from django.db import models
from django.db.models.base import Model


class School(models.Model):
    contact_name = models.CharField(max_length=200)
    address = models.TextField()
    country = models.CharField(max_length=200)
    contact_email = models.EmailField(unique=True)
    contact_phone  = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return self.contact_name

class Coupons(models.Model):
    coupon_code = models.CharField(max_length=10, unique=True)
    expires_at = models.DateField(blank=True, null=True)
    school = models.OneToOneField(School, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.school.contact_name} - {self.coupon_code} | expires : {self.expires_at}"

# Create your models here.
