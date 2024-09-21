"""Profiles views imports"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from products.models import Product
from .forms import UserProfileForm, UserForm
from .models import UserProfile, Wishlist


# pylint: disable=locally-disabled, no-member

@login_required
def view_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Initialize forms with instances
    user_form = UserForm(instance=request.user)
    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        if request.POST.get('form_type') == 'user_form':
            user_form = UserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Personal info updated successfully.')
                return redirect('profile')

        elif request.POST.get('form_type') == 'profile_form':
            profile_form = UserProfileForm(request.POST, instance=user_profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Shipping info updated successfully.')
                return redirect('profile')

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'profiles/profile.html', context)




@login_required
def profile_delete(request, pk):
    """
    View for deleting a user profile.
    """
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        # Handle profile deletion
        user.delete()
        # Log the user out
        logout(request)
        # Display a success message
        messages.success(request, "Your profile has been successfully deleted.")
        # Redirect to the home page
        return redirect('home')

    # If not a POST request, show confirmation page
    return render(request, 'components/delete-modal.html')


@login_required
def add_remove_wishlist_items(request, pk):
    """
    Add or remove a product from the wishlist.
    """
    product = get_object_or_404(Product, pk=pk)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if not created:
        # Item was found, so it is being removed
        wishlist_item.delete()
        messages.success(request, f"{product.title} has been removed from your wishlist.")
    else:
        # Item was not found, so it is being added
        messages.success(request, f"{product.title} has been added to your wishlist.")

    # Redirect to the referring page
    return redirect(request.META.get('HTTP_REFERER', 'home'))

@login_required
def my_wishlist(request, pk):
    """Renders wishlist page """

    profile = get_object_or_404(UserProfile, id=pk)

    wishlist = Wishlist.objects.filter(user=profile.user).order_by('product__title')


    context = {
        'wishlist': wishlist,

    }
    return render(request, 'profiles/wishlist.html', context)
