from django.urls import path

from apps.dish_types.views import (
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

app_name = "dish_types"

urlpatterns = [
    path("", DishTypeListView.as_view(), name="dish-type-list"),
    path("create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path(
        "<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    )
]
