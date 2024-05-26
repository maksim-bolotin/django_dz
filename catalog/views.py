from django.shortcuts import render
from catalog.models import Category, Product


def home(request):
    """Контроллер для отображения домашней страницы."""
    category = Category.objects.all()
    context = {
        'object_list': category,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    """Контроллер для отображения страницы с контактной информацией."""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'You have a new message from {name}({email}): {message}')
    context = {
        'title': 'Обратная связь'
    }
    return render(request, 'catalog/contact.html', context)


def index(request):
    return render(request, 'catalog/index.html')


def products(request):
    product = Product.objects.all
    context = {
        'object_list': product,
        'title': 'Товары'
    }
    return render(request, 'catalog/products.html', context=context)


def product(request, pk):
    context = {
        'object_list': Product.objects.get(pk=pk)
    }
    return render(request, 'catalog/product.html', context=context)
