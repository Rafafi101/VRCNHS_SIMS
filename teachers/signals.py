from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'yourappname':  # Replace 'yourappname' with the actual name of your app
        Group.objects.get_or_create(name='ADMIN')
        Group.objects.get_or_create(name='TEACHER')