from django.db import models
from classroom.models import Class
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    ROLE : list = [
        ('student', 'student'),
        ('teacher', 'teacher'),
    ]

    SYLLABLE = [
        ('E.Africa', 'Learner conner E.Africa'),
        ('W.Africa', 'Learner conner W.Africa')
    ]

    fullname = models.CharField(max_length=50)
    email: str = models.EmailField(unique=True)
    phone:  str = models.CharField(max_length=20, unique=True)
    role: str = models.CharField(max_length=10, choices=ROLE)
    country: str = models.CharField(max_length=25)
    # level: str = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    level: str = models.CharField(max_length=4, default='')
    referral_code: str = models.CharField(max_length=40, help_text="Enter referral phone number", default="")
    timestamp: str = models.DateTimeField(auto_now_add=True)
    syllable: str = models.CharField(max_length=25, choices=SYLLABLE, default='')

    def __str__(self) -> str:
        return f'{self.username}'

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images %Y/%M/%d', default='user.png')
    address: str = models.TextField(default='')
    personal_referral_code: str = models.CharField(
        max_length=20, 
        default="", 
        help_text="Enter referral phone number"
    )
    dob = models.DateField(blank=True, null=True)
    

    def __str__(self) -> str:
        return f"{self.user.fullname}'s profile"

