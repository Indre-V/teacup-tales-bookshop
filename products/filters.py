# products/filters.py
import django_filters
from django.db.models import Q
from .models import Product, Category

class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    author_name = django_filters.CharFilter(method='filter_by_author', label='Author')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category', empty_label='All Categories')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')

    class Meta:
        model = Product
        fields = ['title', 'author_name', 'category', 'min_price', 'max_price']

    def filter_by_author(self, queryset, name, value):
        return queryset.filter(author__name__icontains=value)
