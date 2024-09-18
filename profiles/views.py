# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def view_profile(request):
    """View to display the user's profile"""
    user_profile = get_object_or_404(UserProfile, user=request.user)
    
    context = {
        'user_profile': user_profile
    }
    return render(request, 'profiles/profile.html', context)