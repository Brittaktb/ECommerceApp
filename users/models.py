from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)  # adds column

    def __str__(self):
        return f"User {self.username}"