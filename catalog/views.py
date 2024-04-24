from django.shortcuts import render


def home(request):
    """Контроллер для отображения домашней страницы."""
    # products = Product.objects.all()
    return render(request, 'myproject/templates/home.html')


def contact(request):
    """Контроллер для отображения страницы с контактной информацией."""
    return render(request, 'myproject/templates/contact.html')


def catalog(request):
    return render(request, 'myproject/templates/catalog.html')
