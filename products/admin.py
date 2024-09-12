"""Imports for Admin page"""
from django.contrib import admin

from .models import Product, Author, Category, Genre


class ProductAdmin(admin.ModelAdmin):
    """
    Allows admin to manage stock via the admin panel
    """
    list_display = ['title', 'genre', 'date_published']
    list_filter = ['genre', 'date_published']
    search_fields = ['title', 'author__name', ]

    ordering = ('-added',)

class ReviewAdmin(admin.ModelAdmin):
    """Allows admin to manage reviews on products via the admin panel"""
    list_display = ['user', 'product', 'content', 'created_on']
    list_filter = ('created_on',)
    search_fields = ['user', 'content', 'product']


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Author)
