"""Формы приложения catalog."""

from django import forms
from django.core.exceptions import ValidationError

from catalog.constants import ALLOWED_IMAGE_TYPES, FORBIDDEN_WORDS, MAX_IMAGE_SIZE
from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания и редактирования товара."""

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def __init__(self, *args, **kwargs):
        """Добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["rows"] = 4
            else:
                field.widget.attrs["class"] = "form-control"

        self.fields["name"].widget.attrs["placeholder"] = "Введите название товара"
        self.fields["description"].widget.attrs["placeholder"] = "Введите описание товара"
        self.fields["price"].widget.attrs["placeholder"] = "Введите цену товара"

        self.fields["name"].required = True
        self.fields["description"].required = True
        self.fields["category"].required = True
        self.fields["price"].required = True

    def clean_name(self) -> str:
        """Проверяет название товара на запрещенные слова."""
        name = self.cleaned_data["name"]
        self._validate_forbidden_words(name, "названии")
        return name

    def clean_description(self) -> str:
        """Проверяет описание товара на запрещенные слова."""
        description = self.cleaned_data["description"]
        self._validate_forbidden_words(description, "описании")
        return description

    def clean_price(self):
        """Проверяет, что цена товара не отрицательная."""
        price = self.cleaned_data["price"]

        if price < 0:
            raise ValidationError(
                "Цена товара не может быть отрицательной. "
                "Введите значение больше или равное 0."
            )

        return price

    def clean_image(self):
        """Проверяет формат и размер изображения."""
        image = self.cleaned_data.get("image")

        if not image:
            return image

        if hasattr(image, "content_type"):
            if image.content_type not in ALLOWED_IMAGE_TYPES:
                raise ValidationError(
                    "Недопустимый формат изображения. "
                    "Загрузите файл в формате JPEG или PNG."
                )

        if hasattr(image, "size") and image.size > MAX_IMAGE_SIZE:
            raise ValidationError("Размер изображения не должен превышать 5 МБ.")

        return image

    @staticmethod
    def _validate_forbidden_words(value: str, field_name: str) -> None:
        """Проверяет текстовое поле на наличие запрещенных слов."""
        value_lower = value.lower()

        for word in FORBIDDEN_WORDS:
            if word.lower() in value_lower:
                raise ValidationError(
                    f"Запрещено использовать слово '{word}' в {field_name} товара."
                )
