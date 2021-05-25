from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from core.models import CustomUser


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp =  models.DateTimeField(auto_now=timezone.now)

    def __str__(self) -> str:
        return f'{self.owner.username} {self.title} '