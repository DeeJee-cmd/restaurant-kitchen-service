from django.urls import path

from apps.dish_types.views import (
    DishTypeListView,
)

app_name = "dish_types"

urlpatterns = [
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
]