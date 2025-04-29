import os
import dj_database_url
from pathlib import Path

# 1) import our local env.py (if present)
if (Path(__file__).parent / "env.py").is_file():
    from . import env

BASE_DIR = Path(__file__).resolve().parent.parent

# 2) read SECRET_KEY and DEBUG from environment
SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG      = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    ".app.github.dev",
    "labour-tool-45111572f062.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "https://localhost:8000",
    "https://labour-tool-45111572f062.herokuapp.com",
]


INSTALLED_APPS = [
    "widget_tweaks",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "employees",
    "shifts",
    "holidays",
    "reports",
    "skills",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",           # ← add WhiteNoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "labour_management.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "labour_management" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "labour_management.wsgi.application"

# Database
DATABASES = {
    "default": dj_database_url.config(
        default=os.environ["DATABASE_URL"],
        conn_max_age=600,
        ssl_require=True,
    )
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "labour_management" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # ← where collectstatic will gather files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # ← WhiteNoise


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Login / logout redirects
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/accounts/login/"
LOGOUT_REDIRECT_URL = "/accounts/login/?logged_out=1"
