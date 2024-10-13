"""Apps file imports"""
from django.apps import AppConfig

# pylint: disable=unused-import
# pylint: disable=import-outside-toplevel


class ProfilesConfig(AppConfig):
    """
    Default Django
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import profiles.signals
