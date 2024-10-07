"""Mixins Imports"""
from django.db.models import F, Case, When
from django.db.models import DecimalField
from .forms import SortForm


class SortingMixin:
    """
    Mixin to provide sorting functionality for product lists,
    including handling sale prices.
    """
    def apply_sorting(self, queryset):
        """
        Apply sorting based on the user's selection from SortForm.
        """
        sort_form = SortForm(self.request.GET)
        if sort_form.is_valid():
            sort_option = sort_form.cleaned_data.get('sort_by')

            if hasattr(queryset.model, 'product'):
                price_field = 'product__price'
                sale_price_field = 'product__sale_price'
                title_field = 'product__title'
            else:
                price_field = 'price'
                sale_price_field = 'sale_price'
                title_field = 'title'

            queryset = queryset.annotate(
                effective_price=Case(
                    When(**{f'{sale_price_field}__isnull': False}, then=F(sale_price_field)),
                    default=F(price_field),
                    output_field=DecimalField()
                )
            )

            if sort_option == 'title_asc':
                queryset = queryset.order_by(title_field)
            elif sort_option == 'title_desc':
                queryset = queryset.order_by(f'-{title_field}')
            elif sort_option == 'price_asc':
                queryset = queryset.order_by('effective_price')
            elif sort_option == 'price_desc':
                queryset = queryset.order_by('-effective_price')

        return queryset

    def get_context_data(self, **kwargs):
        """
        Add the sort form to the context to display the sorting options in the template.
        """
        context = super().get_context_data(**kwargs)
        context['sort_form'] = SortForm(self.request.GET)

        return context
