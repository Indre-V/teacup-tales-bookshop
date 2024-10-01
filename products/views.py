"""Views Imports """
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.db.models import Avg
from django.utils import timezone
from django_filters.views import FilterView
from profiles.models import Wishlist
from reviews.models import Review
from reviews.forms import ReviewProductForm
from .models import Product
from .filters import ProductFilter
from .mixins import SortingMixin

# pylint: disable=locally-disabled, no-member


class ProductListView(SortingMixin, ListView):
    """
    View to list all products with filtering and sorting functionality.
    """
    model = Product
    template_name = 'products/product-list.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        current_time = timezone.now()
        new_in_threshold = current_time - timedelta(days=30)


        queryset = super().get_queryset()
        product_filter = ProductFilter(self.request.GET or None, queryset=queryset)
        queryset = product_filter.qs


        queryset = self.apply_sorting(queryset)


        for product in queryset:
            product.is_new = product.added >= new_in_threshold

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product_filter = ProductFilter(self.request.GET or None, queryset=self.get_queryset())
        context['filter'] = product_filter

        return context


def product_detail(request, pk):
    """
    View to display product details and wishlist status.
    """
    product = get_object_or_404(Product, pk=pk)

    # Initialize the wishlist status and count
    is_favourited = False


    if request.user.is_authenticated:
        # Check if the product is in the user's wishlist
        is_favourited = Wishlist.objects.filter(user=request.user, product=product).exists()

    if request.method == 'POST':
        review_form = ReviewProductForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product  # Assign the product to the review
            review.user = request.user  # Assign the logged-in user to the review
            review.save()
            return redirect('product-detail', pk=pk)  # Redirect to avoid form resubmission
    else:
        review_form = ReviewProductForm()

    reviews = Review.objects.filter(product=product).order_by('-created_on')

    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0


    context = {
        'product': product,
        'is_favourited': is_favourited,
        'review_form': review_form,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),

    }

    return render(request, 'products/product-detail.html', context)

class ProductSearchView(SortingMixin, FilterView):
    """
    View to display search results with filtering and sorting functionality.
    """
    model = Product
    template_name = 'products/search-results.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset()

        # Apply filtering using the filterset class
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs

        # Apply sorting using the SortingMixin
        return self.apply_sorting(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context