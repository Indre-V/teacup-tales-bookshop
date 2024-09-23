"""Contexts file imports"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from profiles.models import Wishlist
from coupons.models import Coupon

# pylint: disable=locally-disabled, no-member

def cart_contents(request):
    """
    Add cart information to context for all templates.

    This function also includes coupon details if a coupon is applied.
    """
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id')

    coupon = None
    discount = 0
    savings = 0

    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            if coupon.is_valid():
                if coupon.discount_type == 'percentage':
                    discount = coupon.discount_value
                elif coupon.discount_type == 'amount':
                    discount = coupon.discount_value
            else:
                request.session['coupon_id'] = None  # Remove invalid coupon
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

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

    if coupon:
        if coupon.discount_type == 'percentage':
            savings = (grand_total * (discount / Decimal(100)))
        elif coupon.discount_type == 'amount':
            savings = min(grand_total, discount)
        grand_total -= savings

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
        'coupon': coupon,
        'savings': savings,
        'wishlist_count': wishlist_count,
    }

    return context
