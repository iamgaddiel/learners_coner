from django.db import models


class Podcast(models.Model):
    title = models.CharField(max_length=100)
    podcast = models.FileField(default='', upload_to='%Y%M%d')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title} {self.timestamp}'
