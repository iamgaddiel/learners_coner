from django.db import models
from _class.models import Class
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    ROLE : list = [
        ('student', 'student'),
        ('teacher', 'teacher'),
    ]

    email: str = models.EmailField(unique=True)
    phone:  str = models.CharField(max_length=20, unique=True)
    role: str = models.CharField(max_length=10, choices=ROLE)
    country: str = models.CharField(max_length=25)
    level: str = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    referral_code: str = models.CharField(max_length=20, unique=True, help_text="Enter referral phone number")
    timestamp: str = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.username}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images %Y/%M/%d', default='user.png')
    address: str = models.TextField(default='')
    personal_referral_code: str = models.CharField(
        max_length=20, 
        unique=True, 
        default="", 
        help_text="Enter referral phone number"
    )
    dob = models.DateField(blank=True, null=True)
    

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}'s profile"

