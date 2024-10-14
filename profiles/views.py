"""Profiles views imports"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.mixins import SortingMixin
from products.models import Product
from checkout.models import Order
from .models import UserProfile, Wishlist
from .forms import UserProfileForm, UserForm


# pylint: disable=locally-disabled, no-member


@login_required
def view_profile(request):
    """
    This view is used to display user profile page
    """
    user_profile = get_object_or_404(
        UserProfile, user=request.user)

    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        if request.POST.get('form_type') == 'user_form':
            user_form = UserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(
                    request, 'Personal info updated successfully.')
                return JsonResponse({'success': True})

            return JsonResponse({'success': False, 'errors': user_form.errors})

        elif request.POST.get('form_type') == 'profile_form':
            profile_form = UserProfileForm(
                request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(
                    request, 'Shipping info updated successfully.')
                return JsonResponse({'success': True})

            return JsonResponse(
                {'success': False, 'errors': profile_form.errors})

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def profile_delete(request, pk):
    """
    View for deleting a user profile.
    """
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':

        user.delete()
        logout(request)

        messages.success(
            request, "Your profile has been successfully deleted.")

        return redirect('home')

    return render(request, 'components/delete-modal.html')


@login_required
def add_remove_wishlist_items(request, pk):
    """
    Add or remove a product from the wishlist.
    """
    product = get_object_or_404(Product, pk=pk)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product)

    if not created:

        wishlist_item.delete()
        messages.success(
            request, f"{product.title} has been removed from your wishlist.")
    else:

        messages.success(
            request, f"{product.title} has been added to your wishlist.")

    return redirect(request.META.get('HTTP_REFERER', 'home'))


class MyOrdersView(LoginRequiredMixin, ListView):
    """
    Display the logged-in user's order history.
    """
    model = Order
    template_name = 'profiles/my-orders.html'
    context_object_name = 'orders'
    paginate_by = 5

    def get_queryset(self):
        """
        Return the orders of the logged-in user.
        """
        return Order.objects.filter(
            user_profile__user=self.request.user).order_by('-date')


class MyWishlistView(LoginRequiredMixin, SortingMixin, ListView):
    """
    Class-based view to display user's wishlist with sorting and pagination.
    """
    model = Wishlist
    template_name = 'profiles/wishlist.html'
    context_object_name = 'wishlist'
    paginate_by = 6

    def get_queryset(self):
        """
        Get the user's wishlist items and apply sorting.
        """
        profile = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        queryset = Wishlist.objects.filter(
            user=profile.user
        ).select_related('product')

        queryset = self.apply_sorting(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add the query string to the context
        to preserve sorting during pagination.
        """
        context = super().get_context_data(**kwargs)

        get_params = self.request.GET.copy()
        if 'page' in get_params:
            get_params.pop('page')

        context['query_string'] = get_params.urlencode()

        return context
