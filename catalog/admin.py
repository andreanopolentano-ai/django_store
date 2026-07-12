"""Админка приложения catalog."""

from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки отображения категорий в админке."""

    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Настройки отображения продуктов в админке."""

    list_display = ("id", "name", "price", "category", "owner", "is_published")
    list_filter = ("category", "is_published")
    search_fields = ("name", "description")
