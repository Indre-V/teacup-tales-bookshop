"""Imports for Forms page"""
from django import forms
from products.models import Product, Category, Genre, Author

class ProductForm(forms.ModelForm):
    """
    Form for creating and updating a product with an HTML5 date picker.
    """
    date_published = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',  # This uses the native HTML5 date picker
        }),
        required=False
    )

    class Meta:
        model = Product
        exclude = ('discount', 'out_of_stock')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Apply form-control class to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'friendly_name', 'category']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']
