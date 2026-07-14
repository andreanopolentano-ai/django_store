"""Команда для создания группы модераторов продуктов."""

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    """Создает группу Модератор продуктов и назначает права."""

    help = "Создает группу Модератор продуктов с нужными правами"

    def handle(self, *args, **options):
        """Создает группу и назначает ей права модерации продуктов."""
        group, _ = Group.objects.get_or_create(name="Модератор продуктов")

        content_type = ContentType.objects.get_for_model(Product)

        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                "can_unpublish_product",
                "delete_product",
            ],
        )

        group.permissions.set(permissions)

        self.stdout.write(
            self.style.SUCCESS(
                "Группа 'Модератор продуктов' создана и права назначены."
            )
        )
