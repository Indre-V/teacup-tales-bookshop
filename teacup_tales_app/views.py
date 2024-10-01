"""Error Handling"""
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# pylint: disable=unused-argument


def custom_400(request, exception):
    '''
    Render 400 page
    '''
    return render(request, 'errors/400.html', status=400)


def custom_404(request, exception):
    '''
    Render 404 page
    '''
    return render(request, 'errors/404.html', status=404)


def custom_403(request, exception):
    '''
    Render 403 page
    '''
    if isinstance(exception, PermissionDenied):
        return render(request, 'errors/403.html', status=403)
    else:
        return render(request, 'errors/500.html', status=500)


def custom_500(request):
    '''
    Render 500 page
    '''
    return render(request, 'errors/500.html', status=500)


def custom_csrf_failure(request, reason=""):
    """
    Handles missing csrf token
    """
    return render(request, 'errors/403.html', status=403)
