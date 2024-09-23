"""Bag Tools imports"""
from decimal import Decimal
from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """
    Calculate the subtotal for a product.
    """
    return price * quantity


@register.inclusion_tag('components/quantity-selector.html')
def quantity_selector(product, quantity):
    """
    Renders the quantity selector component for a product.
    """
    return {'product': product, 'quantity': quantity}


@register.filter(name='calc_discount')
def calc_discount(total, discount):
    """
    Calculate the discount amount based on the total and discount percentage.
    """
    return (total * (discount / Decimal(100))) if discount > 0 else Decimal(0)


@register.filter(name='total_after_discount')
def total_after_discount(total, discount_amount):
    """
    Calculate the total amount after applying the discount.
    """
    return total - discount_amount


@register.inclusion_tag('components/coupon-info.html')
def coupon_info(coupon, savings):
    """
    Renders the coupon information component.
    """
    return {'coupon': coupon, 'savings': savings}
