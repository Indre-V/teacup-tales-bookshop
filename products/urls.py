from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_products, name='all-products'),
    path('product/<str:pk>/', views.product, name='product'),

]