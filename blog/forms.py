from django import forms

from blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Форма блоговой записи."""

    class Meta:
        model = BlogPost
        fields = ("title", "content", "preview", "is_published")

    def __init__(self, *args, **kwargs):
        """Добавляет стили полям формы."""
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields["is_published"].widget.attrs["class"] = "form-check-input"
