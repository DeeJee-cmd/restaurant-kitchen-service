from django.urls import path

from apps.dish_types.views import (
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
)

app_name = "dish_types"

urlpatterns = [
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dish-types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
    )
]