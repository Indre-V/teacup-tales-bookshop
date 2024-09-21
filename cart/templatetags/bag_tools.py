from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.inclusion_tag('components/quantity-selector.html')
def quantity_selector(product, quantity):
    return {'product': product, 'quantity': quantity}