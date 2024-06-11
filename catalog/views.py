from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from catalog.models import Category, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
    success_url = reverse_lazy('catalog:list')


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/products.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'product_image', 'product_category', 'product_price')
    success_url = reverse_lazy('catalog:list')

    def get_success_url(self):
        return reverse('products:detail', args=[self.kwargs.get('pk')])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


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
