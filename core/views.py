"""Core views imports"""
from django.shortcuts import render
from products.forms import ProductSearchForm

def index(request):
    """ A view to return the index page """
    form = ProductSearchForm()
    return render(request, 'core/index.html', {'form': form})
