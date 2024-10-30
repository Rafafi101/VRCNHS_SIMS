from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Teacher


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'accounts':
        Group.objects.get_or_create(name='ADMIN')
        Group.objects.get_or_create(name='TEACHER')


@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        try:
            # Automatically assign ADMIN for staff users or superusers
            if instance.is_staff or instance.is_superuser:
                admin_group = Group.objects.get(name='ADMIN')
                instance.groups.add(admin_group)
            else:
                # Non-staff, non-superuser users default to TEACHER group
                teacher_group = Group.objects.get(name='TEACHER')
                instance.groups.add(teacher_group)
        except Group.DoesNotExist:
            # If the group doesn't exist yet, skip assignment
            pass
