from django.core.management import BaseCommand, call_command

from catalog.models import Category, Product


class Command(BaseCommand):
    """Команда для загрузки тестовых данных каталога."""

    help = "Удаляет старые данные каталога и загружает фикстуры"

    def handle(self, *args, **options):
        """Удаляет данные и загружает фикстуры."""
        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command("loaddata", "categories.json")
        call_command("loaddata", "products.json")

        self.stdout.write(
            self.style.SUCCESS("Данные каталога успешно загружены")
        )
