from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact, name='contact')
]
