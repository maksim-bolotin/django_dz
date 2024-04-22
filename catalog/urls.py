from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home_page, name='home'),  # URL для домашней страницы
    path('contact/', views.contact_page, name='contact'),  # URL для страницы с контактной информацией
]
