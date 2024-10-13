"""Order Admin Imports"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Inline model admin to display order line items within the order admin page.
    """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin model for managing orders. Displays the order details, including
    related line items, and allows management
    of order status and applied discounts.
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag',
                       'stripe_pid', 'discount')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'discount',
              'coupon', 'original_bag', 'stripe_pid', 'status')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'discount',
                    'delivery_cost', 'grand_total', 'status')

    list_filter = ('status', 'date', 'coupon')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
