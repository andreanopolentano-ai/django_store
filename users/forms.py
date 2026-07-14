"""Формы приложения users."""

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from users.models import User


class UserRegisterForm(forms.ModelForm):
    """Форма регистрации пользователя."""

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        """Добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["email"].widget.attrs["placeholder"] = "Введите email"
        self.fields["password1"].widget.attrs["placeholder"] = "Введите пароль"
        self.fields["password2"].widget.attrs["placeholder"] = "Повторите пароль"

    def clean_email(self) -> str:
        """Проверяет уникальность email."""
        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")

        return email

    def clean(self):
        """Проверяет совпадение паролей."""
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают.")

        return cleaned_data

    def save(self, commit=True):
        """Создает пользователя с зашифрованным паролем."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user


class EmailAuthenticationForm(forms.Form):
    """Форма авторизации пользователя по email и паролю."""

    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
    )

    def __init__(self, request=None, *args, **kwargs):
        """Сохраняет request и добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        self.request = request
        self.user_cache = None

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["email"].widget.attrs["placeholder"] = "Введите email"
        self.fields["password"].widget.attrs["placeholder"] = "Введите пароль"

    def clean(self):
        """Проверяет email и пароль пользователя."""
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            self.user_cache = authenticate(
                self.request,
                username=email,
                password=password,
            )

            if self.user_cache is None:
                raise ValidationError("Неверный email или пароль.")

            if not self.user_cache.is_active:
                raise ValidationError("Учетная запись отключена.")

        return cleaned_data

    def get_user(self):
        """Возвращает авторизованного пользователя."""
        return self.user_cache


class UserProfileForm(forms.ModelForm):
    """Форма редактирования профиля пользователя."""

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "avatar", "phone", "country")

    def __init__(self, *args, **kwargs):
        """Добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
