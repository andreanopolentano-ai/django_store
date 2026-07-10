from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def home(request):
    """Отображает главную страницу."""
    return render(request, "catalog/home.html")


@require_http_methods(["GET", "POST"])
def contacts(request):
    """Отображает страницу контактов и обрабатывает форму."""
    success_message = None

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        print("Получены данные формы:")
        print(f"Имя: {name}")
        print(f"Почта: {email}")
        print(f"Сообщение: {message}")

        success_message = "Ваше сообщение успешно отправлено."

    context = {
        "success_message": success_message,
    }

    return render(request, "catalog/contacts.html", context)
