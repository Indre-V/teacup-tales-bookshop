# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def view_profile(request):
    """View to display the user's profile"""
    # Get the user profile linked to the logged-in user
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    # Pass the profile to the template
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profile.html', context)
