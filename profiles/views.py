"""Profiles views imports"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from .models import UserProfile

@login_required
def view_profile(request):
    """
    Profile view to display and update user profile.
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thanks {user_profile.user.get_full_name()}, your details have been updated.')
            return redirect('view_profile')  # Redirect to avoid form resubmission
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
        'profile': user_profile,  
    }

    return render(request, 'profiles/profile.html', context)
