from .dev import *


DEBUG = os.environ.get("DJANGO_DEBUG", "") == "False"

SECRET_KEY = os.environ.get("SECRET_KEY", "59%bf^=tswscl1!xaba!xub-ow#uaq!q^3+u!@04bnhtbo-l5h")

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

