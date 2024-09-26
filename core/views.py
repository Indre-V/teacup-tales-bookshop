"""Core views imports"""
from django.shortcuts import render
from products.filters import ProductFilter
from products.models import Product

# pylint: disable=locally-disabled, no-member

def index(request):
    """ A view to return the index page """
    filter = ProductFilter(request.GET or None, queryset=Product.objects.none())

    return render(request, 'core/index.html', {'filter': filter})
