from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Настройки отображения блоговых записей в админке."""

    list_display = ("id", "title", "is_published", "views_count", "created_at")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
