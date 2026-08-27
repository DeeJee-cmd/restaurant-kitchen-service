from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from apps.dishes.forms import DishForm
from apps.dishes.models import Dish


class DishesListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5
    queryset = Dish.objects.select_related("dish_type")
    template_name = "kitchen/dishes/dish_list.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dishes/dish_form.html"
    success_url = reverse_lazy("dishes:dish-list")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.cooks.add(self.request.user)
        return response


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kitchen/dishes/dish_detail.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dishes/dish_form.html"
    success_url = reverse_lazy("dishes:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "kitchen/dishes/dish_confirm_delete.html"
    success_url = reverse_lazy("dishes:dish-list")
