from django import forms

from apps.dishes.models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type"]


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control border-0 rounded-pill bg-transparent ps-4 shadow-none",
                "placeholder": "Search...",
            }
        )
    )