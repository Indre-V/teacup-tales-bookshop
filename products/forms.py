"""Forms Imports"""
from django import forms


class SortForm(forms.Form):
    """
    Form to allow users to sort products on the product listing page.

    """

    SORT_CHOICES = [
        ('', 'Sort by'),
        ('title_asc', 'Title (A to Z)'),
        ('title_desc', 'Title (Z to A)'),
        ('price_asc', 'Price (Low to High)'),
        ('price_desc', 'Price (High to Low)'),
    ]

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

