from django.shortcuts import render


def home(request):
    """Контроллер для отображения домашней страницы."""
    return render(request, 'catalog/home.html')


def contact(request):
    """Контроллер для отображения страницы с контактной информацией."""
    return render(request, 'catalog/contact.html')


def index(request):
    return render(request, 'catalog/index.html')
