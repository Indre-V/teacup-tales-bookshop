from django.db import models
from django.views.generic.list import MultipleObjectMixin
from .forms import SortForm
from django.db.models import F, Case, When

class SortingMixin(MultipleObjectMixin):
    """
    Mixin to provide sorting functionality for product lists,
    including handling sale prices.
    """
    def get_queryset(self):
        # Get the base queryset from the view
        queryset = super().get_queryset()

        # Apply sorting
        queryset = self.apply_sorting(queryset)

        return queryset

    def apply_sorting(self, queryset):
        """
        Apply sorting based on the user's selection from SortForm.
        Sorting will prioritize 'sale_price' if it exists, and fall back to 'price' if no sale price is set.
        """
        sort_form = SortForm(self.request.GET)
        if sort_form.is_valid():
            sort_option = sort_form.cleaned_data.get('sort_by')

            # Annotate the queryset with 'effective_price'
            queryset = queryset.annotate(
                effective_price=Case(
                    When(sale_price__isnull=False, then=F('sale_price')),
                    default=F('price'),
                    output_field=models.DecimalField()
                )
            )

            # Apply sorting based on user's selection
            if sort_option == 'title_asc':
                queryset = queryset.order_by('title')
            elif sort_option == 'title_desc':
                queryset = queryset.order_by('-title')
            elif sort_option == 'price_asc':
                queryset = queryset.order_by('effective_price')  # Sort by 'effective_price' for ascending order
            elif sort_option == 'price_desc':
                queryset = queryset.order_by('-effective_price')  # Sort by 'effective_price' for descending order

        return queryset

    def get_context_data(self, **kwargs):
        # Get the existing context
        context = super().get_context_data(**kwargs)
        
        # Add the sort form to the context
        context['sort_form'] = SortForm(self.request.GET)
        
        return context
