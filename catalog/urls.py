from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, contacts, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    ]
