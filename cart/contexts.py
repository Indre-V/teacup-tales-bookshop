"""Contexts file imports"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import Wishlist

# pylint: disable=locally-disabled, no-member

def cart_contents(request):
    """
    Add cart information to context for all templates.
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    discount = request.session.get('discount')

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    if discount:
        savings = (grand_total/100) * discount
        grand_total -= savings
    else:
        savings = 0

    wishlist_count = 0
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount': discount,
        'savings': savings,
        'wishlist_count': wishlist_count,
    }

    return context
