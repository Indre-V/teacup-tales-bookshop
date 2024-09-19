"""Views Imports """
from django.shortcuts import render, get_object_or_404
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



def product_detail(request, pk):
    """
    View to display product details and wishlist status.
    """
    product = get_object_or_404(Product, pk=pk)

    # Initialize the wishlist status and count
    is_favourited = False


    if request.user.is_authenticated:
        # Check if the product is in the user's wishlist
        is_favourited = Wishlist.objects.filter(user=request.user, product=product).exists()

        # Count the number of items in the user's wishlist
        

    context = {
        'product': product,
        'is_favourited': is_favourited,

    }

    return render(request, 'products/product-detail.html', context)