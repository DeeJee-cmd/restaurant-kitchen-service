from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

Cook = get_user_model()


class CookModelTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create_user(
            username="john_doe",
            password="password123",
            first_name="John",
            last_name="Doe",
            years_of_experience=5,
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.cook), "John Doe (john_doe)"
        )

    def test_years_of_experience_default(self):
        cook = Cook.objects.create_user(
            username="new_cook", password="password123"
        )
        self.assertEqual(cook.years_of_experience, 0)

    def test_username_unique_constraint(self):
        with self.assertRaises(Exception):
            Cook.objects.create_user(
                username="john_doe", password="another_password"
            )


class CookListViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )
        Cook.objects.create_user(
            username="alice", password="password123", first_name="Alice"
        )
        Cook.objects.create_user(
            username="bob", password="password123", first_name="Bob"
        )

    def test_login_required(self):
        response = self.client.get(reverse("cooks:cook-list"))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(
            response, f"/accounts/login/?next={reverse('cooks:cook-list')}"
        )

    def test_list_view_returns_200_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("cooks:cook-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cooks/cook_list.html")

    def test_search_by_username(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("cooks:cook-list"), {"username": "alice"})
        cooks = list(response.context["cook_list"])
        self.assertTrue(all("alice" in cook.username for cook in cooks))
        self.assertTrue(any(cook.username == "alice" for cook in cooks))
        self.assertFalse(any(cook.username == "bob" for cook in cooks))


class CookDetailViewTests(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="tester", password="password123"
        )

    def test_login_required(self):
        response = self.client.get(
            reverse("cooks:cook-detail", args=[self.user.pk])
        )
        self.assertNotEqual(response.status_code, 200)

    def test_detail_view_returns_200_for_logged_in_user(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("cooks:cook-detail", args=[self.user.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cooks/cook_detail.html")


class CookCreateViewTests(TestCase):
    def test_create_view_accessible_without_login(self):
        response = self.client.get(reverse("cooks:cook-create"))
        self.assertEqual(response.status_code, 200)

    def test_create_cook(self):
        response = self.client.post(
            reverse("cooks:cook-create"),
            {
                "username": "new_cook",
                "password1": "SuperSecret123!",
                "password2": "SuperSecret123!",
                "first_name": "New",
                "last_name": "Cook",
                "years_of_experience": 2,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cook.objects.filter(username="new_cook").exists())
