"""Apps file imports"""
from django.apps import AppConfig

# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel

class CheckoutConfig(AppConfig):
    """
    Default Django
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals
