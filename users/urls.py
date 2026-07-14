"""Маршруты приложения users."""

from django.urls import path

from users.apps import UsersConfig
from users.views import ProfileUpdateView, RegisterView, UserLoginView, UserLogoutView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", ProfileUpdateView.as_view(), name="profile"),
]
