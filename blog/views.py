from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from blog.forms import BlogPostForm
from blog.models import BlogPost


class BlogPostListView(ListView):
    """Отображает список опубликованных блоговых записей."""

    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        """Возвращает только опубликованные записи."""
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    """Отображает подробную информацию о блоговой записи."""

    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        """Увеличивает счетчик просмотров при открытии записи."""
        post = super().get_object(queryset)
        post.views_count += 1
        post.save(update_fields=["views_count"])
        return post


class BlogPostCreateView(CreateView):
    """Создает блоговую запись."""

    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blogpost_form.html"


class BlogPostUpdateView(UpdateView):
    """Редактирует блоговую запись."""

    model = BlogPost
    form_class = BlogPostForm
    template_name = "blog/blogpost_form.html"

    def get_success_url(self):
        """Перенаправляет на страницу отредактированной записи."""
        return reverse_lazy("blog:detail", kwargs={"pk": self.object.pk})


class BlogPostDeleteView(DeleteView):
    """Удаляет блоговую запись."""

    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:list")
