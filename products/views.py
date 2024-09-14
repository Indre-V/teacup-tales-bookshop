"""Views Imports """
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

# pylint: disable=locally-disabled, no-member

def product_list(request):
    """
    View to list all products
    """
    products = Product.objects.all()
    return render(request, 'products/product-list.html', {'products': products})

class ProductDetailView(DetailView):
    """
    Basic view to display product details.
    """
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'