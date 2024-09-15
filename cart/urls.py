"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.view_cart, name='view-cart'),
    path('add/<item_id>/', views.add_to_cart, name='add-to-cart'),
    path('adjust/<item_id>/', views.adjust_qty, name='change-quantity'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove-from-cart'),
]
