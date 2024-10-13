"""Imports for Views page"""
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404, reverse
)
from coupons.forms import CouponApplyForm
from products.models import Product


# pylint: disable=locally-disabled, no-member


def view_cart(request):
    """
    A view to display the shopping cart page.
    """

    coupon_apply_form = CouponApplyForm()

    context = {
        'coupon_apply_form': coupon_apply_form,
    }

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """
    Add quantity of product to the shopping cart,
    ensuring the quantity does not exceed stock.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in cart:
        new_quantity = cart[item_id] + quantity
        if new_quantity > product.stock_amount:
            new_quantity = product.stock_amount
            messages.error(
                request,
                f'Error: {product.title} has only '
                f'{product.stock_amount} units left.'
                f' You now have {new_quantity} in your cart.'
            )
        else:
            messages.success(
                request, f'Updated {product.title} quantity to {new_quantity}'
            )
        cart[item_id] = new_quantity
    else:
        if quantity > product.stock_amount:
            quantity = product.stock_amount
            messages.error(
                request,
                f'Error: {product.title} has only '
                f'{product.stock_amount} units left.'
            )
        else:
            messages.success(
                    request, f'Added {product.title} to your shopping bag')
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_qty(request, item_id):
    """
    Adjust the quantity of the product in the cart.
    Prevent users from adding more than the available stock.
    """
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    try:
        quantity = int(request.POST.get('quantity'))
    except (ValueError, TypeError):
        messages.error(request, 'Invalid quantity provided.')
        return redirect(reverse('view-cart'))

    if quantity > 0:
        if quantity > product.stock_amount:
            messages.error(
                request,
                f'Error: You cannot add more than '
                f'{product.stock_amount} units of {product.title}.'
            )
            quantity = product.stock_amount

        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.title} quantity to {cart[item_id]}.'
        )
    elif quantity == 0:
        cart.pop(item_id, None)
        messages.success(request, f'Removed {product.title} from your cart.')
    else:
        messages.error(request, 'Quantity cannot be negative.')

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))


def remove_from_cart(request, item_id):
    """
    Remove a product from the cart.
    """
    product = get_object_or_404(Product, pk=item_id)
    cart = request.session.get('cart', {})

    if item_id in cart:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.title} from your cart')
    else:
        messages.error(request, "Item not found in your cart.")

    request.session['cart'] = cart
    return redirect('view-cart')
