"""Forms file imports"""
import re
from django import forms
from django.core.exceptions import ValidationError
from django_countries.widgets import CountrySelectWidget
from .models import Order


class CheckoutForm(forms.ModelForm):
    """
    Form for placing an order during checkout with placeholders,
    classes, and no labels. Uses custom styling for Stripe integration.
    """

    class Meta:
        """
        Form options
        """
        model = Order
        fields = ['full_name', 'email', 'phone_number', 'country', 'postcode',
                  'town_or_city', 'street_address1', 'street_address2',
                  'county', 'coupon']
        widgets = {
            'country': CountrySelectWidget(attrs={
                'class': 'stripe-style-input form-control',

            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
            'coupon': 'Coupon Code (Optional)',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                placeholder = placeholders.get(field, '')
                if self.fields[field].required:
                    placeholder += ' *'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = (
                    'stripe-style-input form-control'
                )

                self.fields[field].label = False

        self.fields['country'].widget.attrs['class'] = (
            'stripe-style-input form-control'
        )

        self.fields['email'].widget.attrs['readonly'] = True

    def clean_phone_number(self):
        """
        Validates the 'phone_number' field.
        Ensures the phone number starts with a '+' and contains only digits.
        """
        phone_number = self.cleaned_data.get('phone_number')

        if not phone_number:
            raise ValidationError("Phone number cannot be empty.")

        phone_number_pattern = r'^\+\d{7,15}$'
        if not re.match(phone_number_pattern, phone_number):
            raise ValidationError(
                "Phone number must start with '+' and contain only digits.")

        return phone_number
