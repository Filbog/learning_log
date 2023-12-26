"""URL patterns for accounts"""

from django.urls import path, include

from . import views

app_name = "accounts"
urlpatterns = [
    # include default auth urls. In the "main" urls.py we set the namespace to "accounts"
    # and the str in include provides some default auth urls, so they'll look like
    # "accounts/login/" and so on
    path("", include("django.contrib.auth.urls")),
    # registration page
    path("register/", views.register, name="register"),
]
