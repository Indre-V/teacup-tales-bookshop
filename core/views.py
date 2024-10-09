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

    bestsellers_data = (
    OrderLineItem.objects
    .values('product__id')
    .annotate(total_sold=Sum('quantity'))
    .order_by('-total_sold')[:3]
)

    bestsellers = Product.objects.filter(id__in=[item['product__id'] for item in bestsellers_data])
    new_arrivals = Product.objects.order_by('-added')[:5]

    context = {
        'filter': product_filter,
        'bestsellers': bestsellers,
        'new_arrivals': new_arrivals,
    }

    return render(request, 'core/index.html', context)
