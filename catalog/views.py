from django.shortcuts import render


def home_page(request):
    """Контроллер для отображения домашней страницы."""
    # products = Product.objects.all()
    return render(request, 'home.html')


def contact_page(request):
    """Контроллер для отображения страницы с контактной информацией."""
    return render(request, 'contact.html')
