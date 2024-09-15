"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.view_cart, name='view-cart'),
    path('add/<item_id>/', views.add_to_cart, name='add-to-cart'),
]
