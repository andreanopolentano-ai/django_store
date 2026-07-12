"""Модели приложения catalog."""

from django.conf import settings
from django.db import models


class Category(models.Model):
    """Модель категории товара."""

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self) -> str:
        """Возвращает строковое представление категории."""
        return self.name


class Product(models.Model):
    """Модель товара."""

    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
        verbose_name="Владелец",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликован",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата последнего изменения",
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [
            (
                "can_unpublish_product",
                "Может отменять публикацию продукта",
            ),
        ]

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return self.name
