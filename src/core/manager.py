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

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            username=username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def _allow_edit(self, obj=None):
        if not obj:
            return True
        return not (obj.is_staff or obj.is_superuser)

    def has_change_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_delete_permission(self, request, obj=None):
        return self._allow_edit(obj)

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True