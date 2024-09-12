"""Views Imports """
from django.shortcuts import render
from .models import Product

# pylint: disable=locally-disabled, no-member

def product_list(request):
    """
    View to list all products
    """
    products = Product.objects.all()
    return render(request, 'stock-admin/dashboard.html', {'products': products})
