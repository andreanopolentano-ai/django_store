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

    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        return self.name
