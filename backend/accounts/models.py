from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        JUDGE = "JUDGE", 'Judge'
        CLERK = "CLERK", 'Clerk'
        LAWYER = "LAWYER", 'Lawyer'

    role = models.CharField(max_length=20, choices=Role.choices)

    def save(self, *args, **kwargs):
        # Only assign the default role if the role is not provided
        if not self.pk and not self.role:  # Check if it's a new user and no role is assigned
            self.role = self.Role.ADMIN  # Assign default role if no role is set
        super().save(*args, **kwargs)  # Call the original save method

