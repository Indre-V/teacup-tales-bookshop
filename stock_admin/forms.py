"""Imports for Forms page"""
from django import forms
from products.models import Product, Category, Genre, Author

# pylint: disable=locally-disabled, no-member

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a product with an HTML5 date picker.
    """
    date_published = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date', 
        }),
        required=True
    )

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
        exclude = ('discount', 'out_of_stock')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply form-control class to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

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
