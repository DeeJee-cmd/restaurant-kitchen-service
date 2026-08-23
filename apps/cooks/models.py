from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Cook(AbstractUser):
    years_on_experience = models.PositiveSmallIntegerField(default=0)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
