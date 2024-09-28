"""Navigation Tags"""
# stock_admin/templatetags/navigation_tags.py
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context=True)
def active_url(context, url_name):
    request = context['request']
    if request.resolver_match.url_name == url_name:
        return 'active'
    return ''

