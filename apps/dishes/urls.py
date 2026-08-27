from django.urls import path

from apps.dishes.views import (
    DishesListView,
    DishCreateView,
    DishDetailView,
    DishUpdateView,
    DishDeleteView,
)

app_name = "dishes"

urlpatterns = [
    path("", DishesListView.as_view(), name="dish-list"),
    path("create/", DishCreateView.as_view(), name="dish-create"),
    path("<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
]
