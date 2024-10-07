"""Forms Imports"""
from django import forms


class CouponApplyForm(forms.Form):
    """
    Form for applying a coupon code.
    """
    code = forms.CharField(max_length=50)
