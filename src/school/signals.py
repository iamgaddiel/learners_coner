from django.dispatch import receiver
from django.db.models.signals import post_save
from core.models import CustomUser
from .models import School, Coupons
import shortuuid


@receiver(post_save, sender=School)
def create_coupons(sender, instance, created, **kwargs):
    if created:
        Coupons.objects.create(school=instance, coupon_code=shortuuid.ShortUUID().random(length=10))

@receiver(post_save, sender=School)
def save_coupons(sender, instance, **kwargs):
    instance.coupons.save()