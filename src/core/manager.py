from django.contrib.auth.models import BaseUserManager
from django.db import IntegrityError


class CustomUserManger(BaseUserManager):
    def create_user(self, email,  password=None, username=""):
        if not email:
            raise ValueError('User must have an email')

        if not username:
            raise ValueError('User must have a username')

        # Validate email is unique in database
        # if self.model.filter(email = self.normalize_email(username).lower()).exists():
        #     raise ValueError('This email has already been registered.')
    
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)

        try:
            user.save(using=self._db)
        except IntegrityError as e:
            raise ValueError('This user with this details has already been registered', e)
        return user
