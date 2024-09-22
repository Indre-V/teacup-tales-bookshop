"""Imports for Forms page"""
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput
from products.models import Product, Category, Genre, Author

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
        Meta options to specify the Product model.
        """
        model = Product
        image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)
        exclude = ('discount', 'out_of_stock')
        widgets = {
            'description': SummernoteWidget(attrs={'rows': 5}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control author-input'})

        }


class CategoryForm(forms.ModelForm):
    """
    Form for creating or updating categories.
    """
    class Meta:
        """
        Meta options to specify the Category model and include the 'name' field.
        """
        model = Category
        fields = ['name']


class GenreForm(forms.ModelForm):
    """
    Form for managing genres, including assigning a category.
    """
    class Meta:
        """
        Meta options to specify the Genre model, including 'name' and 'category'.
        """
        model = Genre
        fields = ['name', 'category']


class AuthorForm(forms.ModelForm):
    """
    Form for creating or updating author details.
    """
    class Meta:
        """
        Meta options to specify the Author model and include 'name' and 'bio' fields.
        """
        model = Author
        fields = ['name', 'bio']
