"""Apps imports"""
from django.apps import AppConfig


class CustomerServiceConfig(AppConfig):
    """
    Configuration class for the 'customer_service' app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customer_service'
