"""Imports for Views page"""
from django.contrib import messages
from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse
)
from coupons.forms import CouponApplyForm
from products.models import Product



def view_cart(request):
    '''
    A view to display the shopping cart page
    '''
    coupon_apply_form = CouponApplyForm()
    return render(request, 'cart/cart.html', {'coupon_apply_form': coupon_apply_form})


def add_to_cart(request, item_id):
    """
    Add quantity of product to bag
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if product.stock_amount >= cart[item_id] + quantity:
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.title} quantity \
                    to {cart[item_id]}')
        else:
            messages.error(
                request, f'Error {product.title} has only \
                {product.stock_amount} units left, you have {cart[item_id]} \
                    in your bag')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.title} to your shopping bag')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_qty(request, item_id):
    """
    Adjust the quantity of the product
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity > product.stock_amount:
            messages.error(
                request, f'Error {product.title} has only \
                {product.stock_amount} units left')
        else:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.title} quantity \
                to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.title} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view-cart'))


def remove_from_cart(request, item_id):
    """
    Remove a product from the cart
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {product.title} from your cart')

        request.session['cart'] = cart
        return redirect('view-cart')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
