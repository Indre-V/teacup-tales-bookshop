"""Url Imports"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView.as_view(), name='all-products'),
    path('product/<str:pk>/', views.product_detail, name='product-detail'),
    path('search/', views.ProductSearchView.as_view(), name='product-search'),
]

