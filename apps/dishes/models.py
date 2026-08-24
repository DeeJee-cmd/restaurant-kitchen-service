from django.db import models

from apps.cooks.models import Cook
from apps.dish_types.models import DishType


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(
        DishType,
        on_delete=models.CASCADE,
        related_name='dishes',
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name='dishes',
    )

    def __str__(self):
        return self.name
