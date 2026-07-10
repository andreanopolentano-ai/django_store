from django.shortcuts import get_object_or_404, redirect, render

from catalog.forms import ProductForm
from catalog.models import Product


def home(request):
    """Отображает главную страницу со списком товаров."""
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "catalog/home.html", context)


def contacts(request):
    """Отображает страницу контактов."""
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    """Отображает подробную информацию о товаре."""
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, "catalog/product_detail.html", context)


def product_create(request):
    """Создает новый товар."""
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save()
            return redirect("catalog:product_detail", pk=product.pk)
    else:
        form = ProductForm()

    context = {
        "form": form,
    }
    return render(request, "catalog/product_form.html", context)
