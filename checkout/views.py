"""Checkout View Imports"""
import json
import stripe
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from products.models import Product
from cart.contexts import cart_contents
from .forms import CheckoutForm
from .models import OrderLineItem, Order, Coupon


# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    Checkout functionality
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('all-products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key

    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if request.method == 'POST':
        coupon_id = request.session.get('coupon_id')

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = CheckoutForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            if coupon_id:
                try:
                    coupon = Coupon.objects.get(id=coupon_id)
                    if coupon.is_valid():
                        order.coupon = coupon
                except Coupon.DoesNotExist:
                    request.session['coupon_id'] = None
                    messages.error(request, "The coupon is no longer valid.")
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(cart)
            order.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )

                    product.stock_amount = (
                        product.stock_amount - order_line_item.quantity)
                    product.save()

                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the products wasn't found in our database."
                            "Please call us for assistance!"
                        )
                    )

                    order.delete()
                    return redirect(reverse('view-cart'))

            save_info = 'save-info' in request.POST
            if save_info and request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                profile.phone_number = (
                    order.phone_number or profile.phone_number)
                profile.default_country = (
                    order.country or profile.default_country)
                profile.default_postcode = (
                    order.postcode or profile.default_postcode)
                profile.default_town_or_city = (
                    order.town_or_city or profile.default_town_or_city)
                profile.default_street_address1 = (
                    order.street_address1 or profile.default_street_address1)
                profile.default_street_address2 = (
                    order.street_address2 or profile.default_street_address2)
                profile.default_county = order.county or profile.default_county
                profile.save()

            return redirect(reverse('checkout-success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'Please double-check your information.')
    else:
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = CheckoutForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = CheckoutForm()
        else:
            order_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'on_checkout': True
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout-success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
