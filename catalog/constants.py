"""Константы приложения catalog."""

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]

MAX_IMAGE_SIZE = 5 * 1024 * 1024

ALLOWED_IMAGE_TYPES = [
    "image/jpeg",
    "image/png",
]

PRODUCT_DETAIL_CACHE_TTL = 60 * 15
CATEGORY_PRODUCTS_CACHE_TTL = 60 * 15
