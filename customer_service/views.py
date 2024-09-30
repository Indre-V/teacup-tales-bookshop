"""VIews import"""
from django.shortcuts import render


def shipping_returns_view(request):
    """
    View to render the Shipping & Returns page.
    """
    return render(request, 'customer_service/shipping-returns.html')


def privacy_policy_view(request):
    """
    View to render the Privacy Policy page.
    """
    return render(request, 'customer_service/privacy-policy.html')


def terms_of_service_view(request):
    """
    View to render the Terms of Service page.
    """
    return render(request, 'customer_service/terms-of-service.html')
