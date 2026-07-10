from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    """Отображает главную страницу со списком товаров."""

    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"

    def get_queryset(self):
        """Возвращает список всех товаров."""
        return Product.objects.all()


class ContactsTemplateView(TemplateView):
    """Отображает страницу контактов."""

    template_name = "catalog/contacts.html"


class ProductDetailView(DetailView):
    """Отображает подробную информацию о товаре."""

    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    """Создает новый товар."""

    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"

    def get_success_url(self):
        """Возвращает URL созданного товара."""
        return reverse_lazy("catalog:product_detail", kwargs={"pk": self.object.pk})
