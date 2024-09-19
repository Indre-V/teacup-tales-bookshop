"""Profile forms imports"""
# forms.py
from django import forms
from django.core.exceptions import ValidationError
import re
from .models import UserProfile, User

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
    
    # Convert PhoneNumber object to string for regex validation
        phone_number_str = str(phone_number)

    # Check if the phone number starts with a '+' (for international numbers)
        if not phone_number_str.startswith('+') and not phone_number_str.isdigit():
            raise ValidationError("Phone number should start with a '+' or contain only digits.")
    
    # You could also check for minimal length (optional)
        if len(phone_number_str) < 7:
            raise ValidationError("Phone number is too short.")
    
        return phone_number  # Return the PhoneNumber object itself
  # Return the original PhoneNumber object, not the string


class UserForm(forms.ModelForm):
    """
    Form for user registration and profile information
    """
    class Meta:
        """
        Form fields
        """

        model = User
        fields = [
            "first_name",
            "last_name",
        ]

    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
