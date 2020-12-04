from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    message = models.TextField(max_length=400)

    def __str__(self):
        return f"{self.name}"
