"""Admin imports"""
from django.contrib import admin
from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    """
    Admin view for managing coupons in the admin interface.
    """
    list_display = ['code', 'discount_type', 'discount_value',
                    'valid_from', 'valid_to', 'active', 'is_used']
    list_filter = ['active', 'valid_from', 'valid_to', 'discount_type']
    search_fields = ['code']
