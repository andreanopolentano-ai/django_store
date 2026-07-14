"""Контроллеры приложения catalog."""

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Отображает главную страницу со списком товаров."""

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        """Возвращает список товаров с учетом публикации и прав пользователя."""
        user = self.request.user

        if user.is_authenticated and user.has_perm("catalog.can_unpublish_product"):
            return Product.objects.all()

        if user.is_authenticated:
            return Product.objects.filter(
                Q(is_published=True) | Q(owner=user)
            )

        return Product.objects.filter(is_published=True)


class ContactsTemplateView(TemplateView):
    """Отображает страницу контактов."""

    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Отображает подробную информацию о товаре."""

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    raise_exception = True

    def test_func(self):
        """Проверяет доступ к карточке товара."""
        product = self.get_object()
        user = self.request.user

        return (
            product.is_published
            or product.owner == user
            or user.has_perm("catalog.can_unpublish_product")
        )


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создает новый товар."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def form_valid(self, form):
        """Автоматически назначает владельца продукта."""
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """Возвращает URL созданного товара."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Редактирует товар."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    raise_exception = True

    def test_func(self):
        """Проверяет право редактировать продукт."""
        product = self.get_object()
        user = self.request.user

        return (
            product.owner == user
            or user.has_perm("catalog.can_unpublish_product")
        )

    def get_success_url(self):
        """Возвращает URL отредактированного товара."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Удаляет товар."""

    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    raise_exception = True

    def test_func(self):
        """Проверяет право удалить продукт."""
        product = self.get_object()
        user = self.request.user

        return (
            product.owner == user
            or user.has_perm("catalog.delete_product")
        )


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """Снимает продукт с публикации."""

    permission_required = "catalog.can_unpublish_product"
    raise_exception = True

    def post(self, request, pk):
        """Меняет статус публикации продукта на False."""
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save(update_fields=["is_published"])

        return redirect("catalog:product_detail", pk=product.pk)
