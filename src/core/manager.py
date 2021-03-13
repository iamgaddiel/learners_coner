from django.contrib.auth.models import BaseUserManager

class CustomUserManger(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have a username')
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user