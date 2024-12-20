from django.apps import AppConfig


class ClassroomsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classrooms'

    def ready(self):
        import classrooms.signals  # Import signals to ensure they are registered
