from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    """Форма для создания товара."""

    class Meta:
        model = Product
        fields = ("name", "description", "image", "category", "price")

    def __init__(self, *args, **kwargs):
        """Добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

        self.fields["name"].widget.attrs["placeholder"] = "Введите название товара"
        self.fields["description"].widget.attrs["placeholder"] = "Введите описание товара"
        self.fields["price"].widget.attrs["placeholder"] = "Введите цену товара"

        self.fields["name"].required = True
        self.fields["description"].required = True
        self.fields["category"].required = True
        self.fields["price"].required = True
