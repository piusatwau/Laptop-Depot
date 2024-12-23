from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Custom User Mnager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        
        # Create and return a regular user with the given username, email, and password.
       
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        
        # Create and return a superuser with the given username, email, and password.
       
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


# CUstom User Model
class User(AbstractBaseUser, PermissionsMixin):
    
    # Custom User model that uses email instead of username for authentication.
    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)  # Indicates if the user is active
    is_staff = models.BooleanField(default=False)  # Determines if the user can access the admin site
    is_admin = models.BooleanField(default=False)  # Custom field for admin distinction
    date_joined = models.DateTimeField(auto_now_add=True)

    # Specify the fields to use for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Use the custom manager
    objects = CustomUserManager()

    def __str__(self):
        return self.email
