"""Forms Imports"""
from django import forms

class CouponApplyForm(forms.Form):
    """
    Form for applying a coupon code.

    Fields:
        code (str): The coupon code to apply.
    """
    code = forms.CharField(max_length=50)
