from django.views.generic.list import MultipleObjectMixin
from .forms import SortForm
from django.db.models import F, Case, When
from django.db.models import DecimalField

class SortingMixin:
    """
    Mixin to provide sorting functionality for product lists,
    including handling sale prices.
    Adapts based on whether sorting fields belong to the model itself
    or are related via a ForeignKey.
    """
    def apply_sorting(self, queryset):
        """
        Apply sorting based on the user's selection from SortForm.
        Sorting will prioritize 'sale_price' if it exists, and fall back to 'price' if no sale price is set.
        Detects whether sorting is applied to related 'Product' model or directly on 'Product' model.
        """
        sort_form = SortForm(self.request.GET)
        if sort_form.is_valid():
            sort_option = sort_form.cleaned_data.get('sort_by')

            # Determine if sorting is on a model with direct access to Product fields
            # or through a ForeignKey (e.g., Wishlist -> Product)
            if hasattr(queryset.model, 'product'):  # Check if the queryset model has a ForeignKey to 'Product'
                price_field = 'product__price'
                sale_price_field = 'product__sale_price'
                title_field = 'product__title'
            else:
                price_field = 'price'
                sale_price_field = 'sale_price'
                title_field = 'title'

            # Annotate the queryset with 'effective_price'
            queryset = queryset.annotate(
                effective_price=Case(
                    When(**{f'{sale_price_field}__isnull': False}, then=F(sale_price_field)),
                    default=F(price_field),
                    output_field=DecimalField()
                )
            )

            # Apply sorting based on user's selection
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
        # Ensure the form is passed to the template
        context['sort_form'] = SortForm(self.request.GET)
        return context