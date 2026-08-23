from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Cook(AbstractUser):
    years_of_experience = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
