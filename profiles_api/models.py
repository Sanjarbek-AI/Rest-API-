from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserProfileManager(BaseUserManager):
    """Helps django to customize default User model"""

    def create_user(self, email, name, password=None):
        """Creates new user profile object"""

        if not email:
            raise ValueError("User must have email address !!!")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, name, password):
        """Create new superuser for the project with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represent user profile in our system. """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get users full name"""
        return f'{self.name} {self.email}'

    def get_short_name(self):
        """Used to get users short name"""
        return f'{self.name}'

    def __str__(self):
        """Used to convert objects to string by Django"""
        return f'{self.name} => {self.email}'

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users\' Profiles'
