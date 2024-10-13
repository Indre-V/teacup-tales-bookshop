"""Imports for Forms page"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from products.models import Product, Category, Genre, Author
from checkout.models import Order
from coupons.models import Coupon
from .widgets import CustomClearableFileInput


# pylint: disable=locally-disabled, no-member


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a product with an HTML5 date picker.
    """
    author = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2'})
    )

    date_published = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
        }),
        required=True
    )

    def clean_date_published(self):
        """
        Ensure that the 'date_published' is not in the future.
        Raises a ValidationError if the date is a future date.
        """
        date_published = self.cleaned_data.get('date_published')
        if date_published > timezone.now().date():
            raise ValidationError("Date published cannot be in the future.")
        return date_published

    def user_is_admin(self):
        """
        Helper method to check if the user is an admin.
        """
        return self.user and self.user.is_superuser

    class Meta:
        """
        Options for Product form
        """
        model = Product
        exclude = ('discount', 'out_of_stock')
        image = forms.ImageField(
                label='Image', required=False, widget=CustomClearableFileInput)

        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'style': 'height: 200px;',
                'placeholder': 'Enter product description...',
            }),
            'author': forms.SelectMultiple(attrs={
                'class': 'form-control author-input',
            }),
        }


class CategoryForm(forms.ModelForm):
    """
    Form for creating or updating categories.
    """
    class Meta:
        """
        Meta options to specify the Category
        model and include the 'name' field.
        """
        model = Category
        fields = ['name']


class GenreForm(forms.ModelForm):
    """
    Form for managing genres, including assigning a category.
    """
    class Meta:
        """
        Meta options to specify the Genre model,
        including 'name' and 'category'.
        """
        model = Genre
        fields = ['name', 'category']


class AuthorForm(forms.ModelForm):
    """
    Form for creating or updating author details.
    """
    class Meta:
        """
        Meta options to specify the Author model and
        include 'name' and 'bio' fields.
        """
        model = Author
        fields = ['name', 'bio']


class CouponForm(forms.ModelForm):
    """
    A form for adding and editing coupons. This form allows the user
    to create or modify coupon details such as code, validity dates,
    discount type, and other relevant fields.
    """

    class Meta:
        """
        Meta options for CouponForm. Defines the model and fields
        to be used in the form, as well as custom widgets for date fields.
        """
        model = Coupon
        fields = [
            'code', 'valid_from', 'valid_to',
            'discount_type', 'discount_value', 'active', 'is_used'
        ]
        widgets = {
            'valid_from': forms.DateInput(
                attrs={'type': 'date'}, format='%Y-%m-%d'),
            'valid_to': forms.DateInput(
                attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def clean_valid_to(self):
        """
        Validate the 'valid_to' date to ensure it is not in the past.
        """
        valid_to = self.cleaned_data.get('valid_to')
        if valid_to and valid_to < timezone.now():
            raise ValidationError(
                'The "Valid To" date cannot be in the past.')
        return valid_to

    def clean_code(self):
        """
        Validate the 'code' field to ensure it is unique.
        """
        code = self.cleaned_data.get('code')
        if Coupon.objects.filter(code=code).exists():
            raise ValidationError(
                'A coupon with this code already exists.')
        return code


class OrderStatusForm(forms.ModelForm):
    """
    Form for updating the status of an order.
    """
    class Meta:
        """
        Options for Order form
        """
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_status(self):
        """
        Ensure that status is not blank.
        """
        status = self.cleaned_data.get('status')
        if not status:
            raise forms.ValidationError("This field is required.")
        return status
