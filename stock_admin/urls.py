"""URL Patterns"""
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.AdminDashboardView.as_view(), name='product-dashboard'),
    path('admin/add/', views.AddProductView.as_view(), name='add-product'),
    path('dashboard/edit/<str:pk>/', views.EditProductView.as_view(), name='edit-product'),
    path('dashboard/delete/<str:pk>/', views.DeleteProductView.as_view(), name='delete-product'),
    path('genre/', views.ManageGenreView.as_view(), name='manage-genre'),
    path('categories/', views.ManageCategoryView.as_view(), name='manage-category'),
    path('author/', views.ManageAuthorView.as_view(), name='manage-author'),
    path('coupons/', views.ManageCouponView.as_view(), name='manage-coupon'),
    path('orders/', views.ManageOrdersView.as_view(), name='manage-orders'),
]
