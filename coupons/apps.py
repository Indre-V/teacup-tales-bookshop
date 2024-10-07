"""Apps imports"""
from django.apps import AppConfig


class CouponsConfig(AppConfig):
    """
    Configuration class for the 'coupons' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coupons'
