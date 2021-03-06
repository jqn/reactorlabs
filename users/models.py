from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    editor = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
