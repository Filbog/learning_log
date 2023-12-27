"""
Django settings for ll_project project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-&gln3c63q15*%k6o&c^8n*-if@gq^_h_kgbhj5m7gh!(2^wtf2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # my apps
    "learning_logs",
    "accounts",
    # third-party apps
    "django_bootstrap5",
    # default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ll_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "ll_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# My settings
LOGIN_REDIRECT_URL = "learning_logs:index"
LOGOUT_REDIRECT_URL = "learning_logs:index"
LOGIN_URL = "accounts:login"

# Settings for deployment on platform.sh to work
from platformshconfig import Config

config = Config()

# if-statement - only run the code below if this file is used on Platform.sh server
if config.is_valid_platform():
    # this is the host platform.sh uses
    ALLOWED_HOSTS.append(".platformsh.site")
    # DEBUG = False
    # If settings are being loaded in the deployed app’s directory, we set STATIC_ROOT so that
    # static files are served correctly.
    if config.appDir:
        STATIC_ROOT = Path(config.appDir) / "static"
    if config.projectEntropy:
        # setting a more secure SECRET_KEY on a remote server apparently
        SECRET_KEY = config.projectEntropy

    # if statement - only run code below if the "build" process has finished running
    if not config.in_build():
        # configuring DB settings, for example changing to postgres
        db_settings = config.credentials("database")
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": db_settings["path"],
                "USER": db_settings["username"],
                "PASSWORD": db_settings["password"],
                "HOST": db_settings["host"],
                "PORT": db_settings["port"],
            },
        }
