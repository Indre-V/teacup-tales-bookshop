"""Views Imports """
from django.shortcuts import render
from django.views.generic import DetailView
from django.utils import timezone
from datetime import timedelta
from .models import Product

# pylint: disable=locally-disabled, no-member

def product_list(request):
    """
    View to list all products
    """
    current_time = timezone.now()

    new_in_threshold = current_time - timedelta(days=30)

    products = Product.objects.all()

    for product in products:
        product.is_new = product.added >= new_in_threshold

    return render(request, 'products/product-list.html', {'products': products})

class ProductDetailView(DetailView):
    """
    Basic view to display product details.
    """
    model = Product
    template_name = 'products/product-detail.html'
    context_object_name = 'product'