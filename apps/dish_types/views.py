from django.views import generic
from django.urls import reverse_lazy

from apps.dish_types.forms import DishTypeSearchForm, DishTypeForm
from apps.dish_types.models import DishType


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_types/dish_type_list.html"
    context_object_name = "dish_type_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen/dish_types/dish_type_detail.html"


class DishTypeCreateView(generic.edit.CreateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_types/dish_type_form.html"
    success_url = reverse_lazy("dish_types:dish-type-list")


class DishTypeUpdateView(generic.edit.UpdateView):
    model = DishType
    form_class = DishTypeForm
    template_name = "kitchen/dish_types/dish_type_form.html"
    success_url = reverse_lazy("dish_types:dish-type-list")


class DishTypeDeleteView(generic.edit.DeleteView):
    model = DishType
    template_name = "kitchen/dish_types/dish_type_confirm_delete.html"
    success_url = reverse_lazy("dish_types:dish-type-list")