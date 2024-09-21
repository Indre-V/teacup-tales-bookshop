"""Profile forms imports"""
import re
from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile, User


class UserProfileForm(forms.ModelForm):
    """
    A form for handling the UserProfile model.
    """
    class Meta:
        """
        Model and the fields that will be used in this form.
        Fields are mapped to UserProfile model attributes.
        """
        model = UserProfile
        fields = [
            'phone_number', 'default_street_address1', 'default_street_address2', 
            'default_town_or_city', 'default_county', 'default_postcode', 
            'default_country'
        ]
        widgets = {
            'default_country': forms.Select(attrs={'class': 'form-select'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address1': forms.TextInput(attrs={'class': 'form-control'}),
            'default_street_address2': forms.TextInput(attrs={'class': 'form-control'}),
            'default_town_or_city': forms.TextInput(attrs={'class': 'form-control'}),
            'default_county': forms.TextInput(attrs={'class': 'form-control'}),
            'default_postcode': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'City',
            'default_county': 'County',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }

    def clean_default_country(self):
        """
        Validates that the 'default_country' field is not empty.
        """
        country = self.cleaned_data.get('default_country')
        if not country:
            raise ValidationError("Please select a country.")
        return country

    def clean_default_town_or_city(self):
        """
        Validates the 'default_town_or_city' field.
        """
        city = self.cleaned_data.get('default_town_or_city')
        if city is None:
            raise ValidationError("City cannot be empty.")
        if re.search('[^a-zA-Z]', city):
            raise ValidationError("City name should only contain alphabets.")
        return city.capitalize()

    def clean_phone_number(self):
        """
        Validates the 'phone_number' field.
        Error if the phone number is empty, doesn't start with a '+', or is too short.
        """
        phone_number = self.cleaned_data.get('phone_number')

        if phone_number is None:
            raise ValidationError("Phone number cannot be empty.")

        phone_number_str = str(phone_number)

        if not phone_number_str.startswith('+') and not phone_number_str.isdigit():
            raise ValidationError("Phone number should start with a '+' or contain only digits.")

        if len(phone_number_str) < 7:
            raise ValidationError("Phone number is too short.")

        return phone_number



class UserForm(forms.ModelForm):
    """
    Form for user registration and profile information
    """
    class Meta:
        """
        Form fields
        """

        model = User
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 3:
            raise forms.ValidationError("First name must be at least 3 characters long.")
        if re.search('[^a-zA-Z]', first_name):
            raise forms.ValidationError("First name should only contain alphabets.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 3:
            raise forms.ValidationError("Last name must be at least 3 characters long.")
        if re.search('[^a-zA-Z]', last_name):
            raise forms.ValidationError("Last name should only contain alphabets.")
        return last_name
