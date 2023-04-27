from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomUserManager(BaseUserManager):
    """
    Custom user manager that provides methods for creating and managing user instances.
    """
    def create_user(self, username, password=None, role=None, **extra_fields):
        """
        Create and save a new user instance with the given username, password, and role.
        """
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, role=role, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model that inherits from AbstractBaseUser and PermissionsMixin.
    """
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=30)
    # Add other fields as needed, e.g. email, first_name, last_name, etc.

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']