from django.urls import path

from apps.cooks.views import (
    CookListView,
    CookDetailView,
    CookCreateView,
    CookUpdateView,
    CookDeleteView,
)

app_name = "cooks"

urlpatterns = [
    path("", CookListView.as_view(), name="cook-list"),
    path("<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("create/", CookCreateView.as_view(), name="cook-create"),
    path("<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"),
    path("<int:pk>/delete/>", CookDeleteView.as_view(), name="cook-delete"),
]
