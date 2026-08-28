from .base import *


DEBUG = True

SECRET_KEY = "django-insecure-change-me"

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 3-rd party apps
    "crispy_bootstrap5",
    "crispy_forms",

    # user apps
    "apps.core",
    "apps.dish_types",
    "apps.dishes",
    "apps.cooks",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_USER_MODEL = "cooks.Cook"

LOGIN_REDIRECT_URL = "/"