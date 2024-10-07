"""Contexts file Imports"""
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
    This function includes coupon details if a coupon is applied.
    """
    cart_items = []
    subtotal = 0
    product_count = 0
    cart = request.session.get('cart', {})
    coupon_id = request.session.get('coupon_id')

    coupon = None
    discount = 0
    savings = 0

    # Calculate the subtotal and product count
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        price = product.sale_price if product.sale_price else product.price
        subtotal += quantity * price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if coupon_id:
        try:
            coupon = Coupon.objects.get(id=coupon_id)
            if coupon.is_valid():
                if coupon.discount_type == 'percentage':
                    discount = (coupon.discount_value / Decimal(100)) * subtotal
                elif coupon.discount_type == 'amount':
                    discount = coupon.discount_value
                savings = min(discount, subtotal)
            else:
                request.session['coupon_id'] = None
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    grand_total = subtotal - savings

    if grand_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.DELIVERY_FEE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - grand_total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Calculate final total including delivery
    final_total = grand_total + delivery

    wishlist_count = 0
    if request.user.is_authenticated:
        wishlist_count = Wishlist.objects.filter(user=request.user).count()

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal, 
        'subtotal_after_discount': subtotal - savings,
        'total': subtotal, 
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': final_total,
        'wishlist_count': wishlist_count,
        'coupon': coupon,
        'savings': savings,  
    }

    return context
