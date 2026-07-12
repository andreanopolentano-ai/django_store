"""Контроллеры приложения users."""

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import EmailAuthenticationForm, UserProfileForm, UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    """Регистрирует нового пользователя."""

    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        """Создает пользователя, отправляет письмо и авторизует его."""
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать в Django Store",
            message="Спасибо за регистрацию в Django Store.",
            from_email=None,
            recipient_list=[self.object.email],
            fail_silently=True,
        )

        login(self.request, self.object)

        return response


class UserLoginView(LoginView):
    """Авторизует пользователя по email и паролю."""

    form_class = EmailAuthenticationForm
    template_name = "users/login.html"


class UserLogoutView(LogoutView):
    """Завершает сессию пользователя."""

    next_page = reverse_lazy("catalog:home")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует профиль пользователя."""

    model = User
    form_class = UserProfileForm
    template_name = "users/profile_form.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        """Возвращает текущего пользователя."""
        return self.request.user
