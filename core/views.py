"""Core views imports"""
from django.shortcuts import render
from django.db.models import Sum
from products.filters import ProductFilter
from products.models import Product
from checkout.models import OrderLineItem

# pylint: disable=locally-disabled, no-member

def index(request):
    """ A view to return the index page """
    product_filter = ProductFilter(request.GET or None, queryset=Product.objects.none())
     
    bestsellers = OrderLineItem.objects.values('product__id', 'product__title', 'product__image').annotate(total_sold=Sum('quantity')).order_by('-total_sold')[:4]

    context = {
        'filter': product_filter,
        'bestsellers': bestsellers,
    }


    return render(request, 'core/index.html', context)
