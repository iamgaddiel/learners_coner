from django.db import models


class Volunteer(models.Model):
    first_name      = models.CharField(max_length=50)
    last_name       =  models.CharField(max_length=50)
    email           = models.EmailField(unique=True)
    phone_number    = models.CharField(max_length=50)
    gender          = models.CharField(max_length=5)
    title           = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    country         = models.CharField(max_length=50)
    age             = models.PositiveIntegerField()
    degree          = models.CharField(max_length=50)
    other_degree    = models.CharField(max_length=50)
    work_mode       = models.CharField(max_length=50)
    skillsets       = models.CharField(max_length=250)
    learn_about_us  = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"