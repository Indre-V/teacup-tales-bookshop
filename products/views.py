"""Views Imports """
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.utils import timezone
from django_filters.views import FilterView
from profiles.models import Wishlist
from reviews.models import Review
from reviews.forms import ReviewProductForm
from .models import Product
from .filters import ProductFilter

# pylint: disable=locally-disabled, no-member


def product_list(request):
    """
    View to list all products
    """
    current_time = timezone.now()

    new_in_threshold = current_time - timedelta(days=30)

    products = Product.objects.all()
    product_filter = ProductFilter(request.GET or None, queryset=Product.objects.none())

    for product in products:
        product.is_new = product.added >= new_in_threshold

    return render(request, 'products/product-list.html', {'products': products, 'filter': product_filter})


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
    print("Average Rating:", average_rating)

    context = {
        'product': product,
        'is_favourited': is_favourited,
        'review_form': review_form,
        'reviews': reviews,
        'average_rating': round(average_rating, 1),

    }

    return render(request, 'products/product-detail.html', context)

class ProductSearchView(FilterView):
    model = Product
    template_name = 'products/search-results.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    paginate_by = 10 

    def get_queryset(self):
        # Start with all products
        queryset = super().get_queryset()

        # Apply filters
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context