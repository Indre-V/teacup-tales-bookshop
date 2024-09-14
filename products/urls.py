from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='all-products'),
    # path('product/<str:pk>/', views.product, name='product'),
    path('products/product/<uuid:pk>/', views.ProductDetailView.as_view(), name='product-detail')
]
