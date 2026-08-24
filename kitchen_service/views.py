from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.cooks.models import Cook
from apps.dishes.models import Dish
from apps.dish_types.models import DishType


@login_required
def index(request):
    num_cooks = Cook.objects.count()
    num_dishes = Dish.objects.count()
    num_dish_types = DishType.objects.count()

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
    }

    return render(request, "kitchen/index.html", context=context)
