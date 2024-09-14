"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.AdminDashboardView.as_view(), name='dashboard'),
    path('admin/add/', views.AddProductView.as_view(), name='add-product'),
    path('dashboard/edit/<str:pk>/', views.EditProductView.as_view(), name='edit-product'),
    path('dashboard/delete/<str:pk>/', views.DeleteProductView.as_view(), name='delete-product'),
]
