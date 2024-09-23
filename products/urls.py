"""Url Imports"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='all-products'),
    path('product/<str:pk>/', views.product_detail, name='product-detail'),
]
