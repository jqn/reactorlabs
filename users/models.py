from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    editor = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
