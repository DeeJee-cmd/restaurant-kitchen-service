from django import forms

from apps.dish_types.models import DishType


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name",]


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )
