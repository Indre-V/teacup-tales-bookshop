from django import forms
from products.models import Category, Author

class ProductSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Title')
    author = forms.CharField(required=False, label='Author')
    description = forms.CharField(required=False, label='Description')
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False, label='Category')
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), required=False, label='Author')
    min_price = forms.DecimalField(
        required=False, min_value=0, label='Min Price')
    max_price = forms.DecimalField(
        required=False, min_value=0, label='Max Price')
