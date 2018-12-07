from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Custom User Model for storing extra profile 
    information.
    """
    dob = models.DateField(null = True)