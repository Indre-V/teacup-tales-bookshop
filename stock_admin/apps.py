"""Apps """
from django.apps import AppConfig


class StockAdminConfig(AppConfig):
    """
    Django Default
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock_admin'
