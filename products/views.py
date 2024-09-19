"""Views Imports """
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from profiles.models import Wishlist
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


@login_required
def product_detail(request, pk):
    """
    View to display product details and wishlist status.
    """
    product = get_object_or_404(Product, pk=pk)

    # Check if the product is in the user's wishlist
    is_favourited = Wishlist.objects.filter(user=request.user, product=product).exists()
    wishlist_count = Wishlist.objects.filter(user=request.user).count()

    context = {
        'product': product,
        'is_favourited': is_favourited,
        'wishlist_count': wishlist_count,
    }

    return render(request, 'products/product-detail.html', context)