from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import products, product, contact

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home),
    path('contact/', contact, name='contact'),
    path('products/', products, name='products'),
    path('<int:pk>', product, name='product'),
]
