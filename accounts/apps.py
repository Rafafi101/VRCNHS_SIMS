from django.apps import AppConfig
from django.contrib.auth.models import Group, User
from django.conf import settings
from django.db.models.signals import post_migrate


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import accounts.signals  # Import signals to ensure they are registered
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_migrate

        # Connect the post_migrate signal to create groups after migrations are complete
        post_migrate.connect(create_groups, sender=self)


def create_groups(sender, **kwargs):
    # Create the ADMIN and TEACHER groups if they don't exist
    Group.objects.get_or_create(name='ADMIN')
    Group.objects.get_or_create(name='TEACHER')
