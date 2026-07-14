"""Сервисы приложения catalog."""

from django.core.cache import cache

from catalog.constants import CATEGORY_PRODUCTS_CACHE_TTL
from catalog.models import Product


def get_products_by_category(category_id: int) -> list[Product]:
    """Возвращает список продуктов указанной категории из кеша или базы данных."""
    cache_key = f"category_{category_id}"

    products = cache.get(cache_key)

    if products is None:
        products = list(
            Product.objects.select_related(
                "category",
                "owner",
            ).filter(
                category_id=category_id,
            )
        )

        cache.set(
            cache_key,
            products,
            CATEGORY_PRODUCTS_CACHE_TTL,
        )

    return products
