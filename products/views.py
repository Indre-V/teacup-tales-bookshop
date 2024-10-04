"""Views Imports """
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Avg
from django.utils import timezone
from django_filters.views import FilterView
from profiles.models import Wishlist, UserProfile
from reviews.models import Review
from reviews.forms import ReviewProductForm
from checkout.models import OrderLineItem
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
    reviews = Review.objects.filter(product=product).order_by('-created_on')
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0

    is_favourited = False
    can_review = False

    if request.user.is_authenticated:

        user_profile = UserProfile.objects.get(user=request.user)


        is_favourited = Wishlist.objects.filter(user=request.user, product=product).exists()


        user_has_purchased = OrderLineItem.objects.filter(
            order__user_profile=user_profile, product=product
        ).exists()

        if user_has_purchased or request.user.is_superuser:
            can_review = True

        # Handle form submission
        if request.method == 'POST' and can_review:
            review_form = ReviewProductForm(request.POST)
            if review_form.is_valid():
                review = review_form.save
                review.user = request.user
                review.save()
                messages.success(request, "Your review has been submitted successfully.")
                return redirect('product-detail', pk=pk)
        else:
            review_form = ReviewProductForm()
    else:
        review_form = None

    context = {
        'product': product,
        'is_favourited': is_favourited,
        'review_form': review_form,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),
        'can_review': can_review,
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

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        queryset = self.filterset.qs

        return self.apply_sorting(queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context
