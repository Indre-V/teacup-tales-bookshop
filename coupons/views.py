"""Coupon Views Imports"""
from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Coupon
from .forms import CouponApplyForm


# pylint: disable=locally-disabled, no-member

@require_POST
def coupon_apply(request):
    """
    View to apply a coupon code to the shopping cart.
    This view checks the validity of the coupon code and, if valid, stores it
    in the user's session.
    """
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True,
                is_used=False
            )
            request.session['coupon_id'] = coupon.id
            messages.success(request, 'Coupon applied successfully!')
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(request, 'This coupon does not exist or is not valid.')
    return redirect('view-cart')
