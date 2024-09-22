"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.AdminDashboardView.as_view(), name='dashboard'),
    path('admin/add/', views.AddProductView.as_view(), name='add-product'),
    path('dashboard/edit/<str:pk>/', views.EditProductView.as_view(), name='edit-product'),
    path('dashboard/delete/<str:pk>/', views.DeleteProductView.as_view(), name='delete-product'),
    path('add-genre/', views.GenreCreateView.as_view(), name='add-genre'),
    path('add-author/', views.AuthorCreateView.as_view(), name='add-author'),
    path('categories/', views.ManageCategoryView.as_view(), name='manage-category'),
]
