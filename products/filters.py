"""Filters.py imports"""
import django_filters
from django.db.models import Q
from django import forms
from .models import Product, Category, Genre

# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument

class ProductFilter(django_filters.FilterSet):
    """
    Search fields for product search and filters
    """
    PRICE_RANGE_CHOICES = [
        ('up_to_10', 'Up to €10'),
        ('10_20', '€10 - €20'),
        ('20_30', '€20 - €30'),
        ('over_30', 'Over €30'),
    ]

    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title',
        widget=forms.TextInput(attrs={'placeholder': 'Search by title'})
    )
    author_name = django_filters.CharFilter(
        method='filter_by_author',
        label='Author',
        widget=forms.TextInput(attrs={'placeholder': 'Search by author'})
    )
    description = django_filters.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        label='Description',
        widget=forms.TextInput(attrs={'placeholder': 'Search by description'})
    )
    isbn = django_filters.CharFilter(
        field_name='isbn',
        lookup_expr='icontains',
        label='ISBN',
        widget=forms.TextInput(attrs={'placeholder': 'Search by ISBN'})
    )
    genre = django_filters.ModelMultipleChoiceFilter(
        queryset=Genre.objects.all(),
        label='Genre',
        widget=forms.CheckboxSelectMultiple
    )
    category = django_filters.ModelMultipleChoiceFilter(
        field_name='genre__category',
        queryset=Category.objects.all(),
        label='Category',
        widget=forms.CheckboxSelectMultiple
    )

    price_ranges = django_filters.MultipleChoiceFilter(
        label='Price Ranges',
        choices=PRICE_RANGE_CHOICES,
        method='filter_multiple_price_ranges',
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        """
        Meta class for the filter
        """
        model = Product
        fields = ['title', 'author_name', 'description', 'isbn', 'genre', 'category', 'price_ranges']

    def filter_by_author(self, queryset, name, value):
        """
        Filters Authors
        """
        return queryset.filter(author__name__icontains=value)

    def filter_multiple_price_ranges(self, queryset, name, value):
        """
        Filters the queryset based on selected price ranges.
        Supports multiple selections.
        """
        queries = Q()
        if 'up_to_10' in value:
            queries |= Q(price__lte=10)
        if '10_20' in value:
            queries |= Q(price__gte=10, price__lte=20)
        if '20_30' in value:
            queries |= Q(price__gte=20, price__lte=30)
        if 'over_30' in value:
            queries |= Q(price__gte=30)
        return queryset.filter(queries).distinct()
