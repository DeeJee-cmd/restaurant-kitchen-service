from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.urls import reverse

from apps.dish_types.models import DishType

Cook = get_user_model()


class DishTypeModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pasta")

    def test_str_representation(self):
        self.assertEqual(str(self.dish_type), "Pasta")

    def test_name_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                DishType.objects.create(name="Pasta")


class DishTypeListViewTests(TestCase):
    def setUp(self):
        DishType.objects.create(name="Pasta")
        DishType.objects.create(name="Pizza")
        DishType.objects.create(name="Soups")

    def test_list_view_accessible_without_login(self):
        response = self.client.get(reverse("dish_types:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "kitchen/dish_types/dish_type_list.html"
        )

    def test_search_by_name(self):
        response = self.client.get(
            reverse("dish_types:dish-type-list"), {"name": "Pizza"}
        )
        dish_types = list(response.context["dish_type_list"])
        self.assertTrue(any(dt.name == "Pizza" for dt in dish_types))
        self.assertFalse(any(dt.name == "Pasta" for dt in dish_types))


class DishTypeCreateViewTests(TestCase):
    def test_create_dish_type(self):
        response = self.client.post(
            reverse("dish_types:dish-type-create"), {"name": "Desserts"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(DishType.objects.filter(name="Desserts").exists())


class DishTypeUpdateDeleteViewTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pasta")

    def test_update_dish_type(self):
        response = self.client.post(
            reverse("dish_types:dish-type-update", args=[self.dish_type.pk]),
            {"name": "Updated Pasta"},
        )
        self.assertEqual(response.status_code, 302)
        self.dish_type.refresh_from_db()
        self.assertEqual(self.dish_type.name, "Updated Pasta")

    def test_delete_dish_type(self):
        response = self.client.post(
            reverse("dish_types:dish-type-delete", args=[self.dish_type.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            DishType.objects.filter(pk=self.dish_type.pk).exists()
        )
