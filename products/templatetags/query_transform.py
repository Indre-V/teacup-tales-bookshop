"""query transform imports"""
from django import template

register = template.Library()

@register.simple_tag
def query_transform(request, **kwargs):
    """
    Allows updating query parameters in templates.
    Example usage: {% query_transform request page=2 %}
    """
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, None)
    return updated.urlencode()
