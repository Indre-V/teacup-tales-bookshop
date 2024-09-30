"""Url Imports"""
from django.urls import path
from . import views

urlpatterns = [
    path('shipping-returns/', views.shipping_returns_view, name='shipping-returns'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy-policy'),
    path('terms-of-service/', views.terms_of_service_view, name='terms-of-service'),
]
