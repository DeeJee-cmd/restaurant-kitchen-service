from django.views import generic

from apps.dish_types.models import DishType


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "dish_types/dish_type_list.html"
    context_object_name = "dish_type_list"