from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.dish_types.models import DishType
from apps.dishes.models import Dish

Cook = get_user_model()


class DishModelTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Pasta")
        self.cook = Cook.objects.create_user(
            username="john_doe", password="password123"
        )
        self.dish = Dish.objects.create(
            name="Carbonara",
            description="Pasta with bacon and cream sauce",
            price=Decimal("10.00"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_str_representation(self):
        self.assertEqual(str(self.dish), "Carbonara")

    def test_dish_type_relation(self):
        self.assertEqual(self.dish.dish_type, self.dish_type)
        self.assertIn(self.dish, self.dish_type.dishes.all())

    def test_cooks_relation(self):
        self.assertIn(self.cook, self.dish.cooks.all())
        self.assertIn(self.dish, self.cook.dishes.all())


class DishListViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )
        self.dish_type = DishType.objects.create(name="Pasta")
        Dish.objects.create(
            name="Carbonara",
            description="desc",
            price=Decimal("10.00"),
            dish_type=self.dish_type,
        )

    def test_login_required(self):
        response = self.client.get(reverse("dishes:dish-list"))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response, f"/accounts/login/?next={reverse('dishes:dish-list')}"
        )

    def test_list_view_returns_200_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("dishes:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dishes/dish_list.html")
        self.assertContains(response, "Carbonara")


class DishDetailViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )
        self.dish_type = DishType.objects.create(name="Pasta")
        self.dish = Dish.objects.create(
            name="Carbonara",
            description="desc",
            price=Decimal("10.00"),
            dish_type=self.dish_type,
        )

    def test_login_required(self):
        response = self.client.get(
            reverse("dishes:dish-detail", args=[self.dish.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_detail_view_returns_200_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("dishes:dish-detail", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dishes/dish_detail.html")


class DishCreateViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )
        self.dish_type = DishType.objects.create(name="Pasta")

    def test_login_required(self):
        response = self.client.get(reverse("dishes:dish-create"))
        self.assertNotEqual(response.status_code, 200)

    def test_create_dish_assigns_current_user_as_cook(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("dishes:dish-create"),
            {
                "name": "Tiramisu",
                "description": "Coffee dessert",
                "price": "7.50",
                "dish_type": self.dish_type.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        dish = Dish.objects.get(name="Tiramisu")
        self.assertIn(self.user, dish.cooks.all())


class DishUpdateDeleteViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )
        self.dish_type = DishType.objects.create(name="Pasta")
        self.dish = Dish.objects.create(
            name="Carbonara",
            description="desc",
            price=Decimal("10.00"),
            dish_type=self.dish_type,
        )

    def test_update_dish(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("dishes:dish-update", args=[self.dish.pk]),
            {
                "name": "Updated Carbonara",
                "description": "desc",
                "price": "12.00",
                "dish_type": self.dish_type.pk,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.dish.refresh_from_db()
        self.assertEqual(self.dish.name, "Updated Carbonara")

    def test_delete_dish(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("dishes:dish-delete", args=[self.dish.pk])
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(pk=self.dish.pk).exists())
