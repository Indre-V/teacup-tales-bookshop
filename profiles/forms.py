"""Profile forms imports"""
# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'phone_number', 'default_street_address1', 'default_street_address2', 
            'default_town_or_city', 'default_county', 'default_postcode', 
            'default_country'
        ]
        widgets = {
            'default_country': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            # Other widgets as needed
        }

    def clean_default_country(self):
        country = self.cleaned_data.get('default_country')
        if not country:
            raise ValidationError("Please select a country.")
        return country

    def clean_default_town_or_city(self):
        city = self.cleaned_data.get('default_town_or_city')
        if city is None:
            raise ValidationError("City cannot be empty.")
        if re.search('[^a-zA-Z]', city):
            raise ValidationError("City name should only contain alphabets.")
        return city.capitalize()

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number is None:
            raise ValidationError("Phone number cannot be empty.")
        if re.search('[^0-9]', phone_number):
            raise ValidationError("Phone number should only contain numbers.")
        return phone_number
