from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from apps.dishes.forms import DishForm
from apps.dishes.models import Dish


# Create your views here.
class DishesListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")
    template_name = "kitchen/dishes/dish_list.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dishes/dish_form.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/dishes/dish_detail.html"
