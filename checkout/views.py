"""Checkout View Imports"""
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib import messages
from .forms import CheckoutForm


# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument




class CheckoutView(View):
    """
    Displays the checkout page with an order form.
    If the cart is empty, redirects to the products page.
    """

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to display the checkout page.
        """
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        order_form = CheckoutForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
        }

        return render(request, template, context)
