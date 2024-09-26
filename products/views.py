"""Views Imports """
from datetime import timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.utils import timezone
from profiles.models import Wishlist
from reviews.models import Review
from reviews.forms import ReviewProductForm
from django.db.models import Q
from .forms import ProductSearchForm
from .models import Product

# pylint: disable=locally-disabled, no-member


def product_list(request):
    """
    View to list all products
    """
    current_time = timezone.now()

    new_in_threshold = current_time - timedelta(days=30)

    products = Product.objects.all()

    for product in products:
        product.is_new = product.added >= new_in_threshold

    return render(request, 'products/product-list.html', {'products': products})


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

def product_search(request):
    form = ProductSearchForm(request.GET or None)
    products = Product.objects.all()

    if form.is_valid():
        title = form.cleaned_data.get('title')
        author = form.cleaned_data.get('author')
        category = form.cleaned_data.get('category')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')

        query = Q()

        if title:
            query &= Q(title__icontains=title)
        if author:
            query &= Q(author__name__icontains=author)
        if category:
            query &= Q(genre__category=category)  # Corrected field lookup
        if min_price is not None:
            query &= Q(price__gte=min_price)
        if max_price is not None:
            query &= Q(price__lte=max_price)

        products = products.filter(query).distinct()
    else:
        products = Product.objects.none()

    context = {
        'form': form,
        'products': products,
    }
    return render(request, 'products/search-results.html', context)