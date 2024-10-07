"""Imports for Views page"""
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse
)
from coupons.forms import CouponApplyForm

from products.models import Product

# pylint: disable=locally-disabled, no-member

def view_cart(request):
    """
    A view to display the shopping cart page.
    """
    # Get the current coupon apply form
    coupon_apply_form = CouponApplyForm()

    # Render the cart template with the coupon apply form
    context = {
        'coupon_apply_form': coupon_apply_form,
    }

    return render(request, 'cart/cart.html', context)


    
def add_to_cart(request, item_id):
    """
    Add quantity of product to bag.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if product.stock_amount >= cart[item_id] + quantity:
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.title} quantity to {cart[item_id]}'
            )
        else:
            messages.error(
                request, f'Error: {product.title} has only {product.stock_amount} units left. You have {cart[item_id]} in your bag.'
            )
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.title} to your shopping bag')

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
        # Attempt to get the quantity from the POST request
        quantity = int(request.POST.get('quantity'))
    except (ValueError, TypeError):
        # Handle invalid or non-numeric quantity values
        messages.error(request, 'Invalid quantity provided.')
        return redirect(reverse('view-cart'))

    # Ensure the quantity is positive and valid
    if quantity > 0:
        if quantity > product.stock_amount:
            # If the user tries to add more than the available stock
            messages.error(
                request, f'Error: You cannot add more than {product.stock_amount} units of {product.title}.'
            )
            quantity = product.stock_amount  # Optionally, set it to the max available stock
        # Update the cart with the valid quantity
        cart[item_id] = quantity
        messages.success(
            request, f'Updated {product.title} quantity to {cart[item_id]}.'
        )
    elif quantity == 0:
        # Remove the item from the cart if quantity is 0
        cart.pop(item_id, None)
        messages.success(request, f'Removed {product.title} from your cart.')
    else:
        # Handle negative quantity attempts
        messages.error(request, 'Quantity cannot be negative.')

    # Save the updated cart back to the session
    request.session['cart'] = cart
    return redirect(reverse('view-cart'))

def remove_from_cart(request, item_id):
    """
    Remove a product from the cart.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        if item_id in cart:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.title} from your cart')

        request.session['cart'] = cart
        return redirect('view-cart')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
