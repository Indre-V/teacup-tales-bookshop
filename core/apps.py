"""Apps imports"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Default Django
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
