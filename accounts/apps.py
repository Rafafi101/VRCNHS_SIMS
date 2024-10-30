from django.apps import AppConfig
from django.contrib.auth.models import Group, User
from django.conf import settings
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals  # Import signals to ensure they are registered
