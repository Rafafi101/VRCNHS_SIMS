from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from .models import Teacher


@receiver(post_save, sender=User)
def assign_group(sender, instance, created, **kwargs):
    if created:
        # Automatically assign ADMIN for staff users or superusers
        if instance.is_staff or instance.is_superuser:
            admin_group, _ = Group.objects.get_or_create(name='ADMIN')
            instance.groups.add(admin_group)
        else:
            # Non-staff, non-superuser users default to TEACHER group
            teacher_group, _ = Group.objects.get_or_create(name='TEACHER')
            instance.groups.add(teacher_group)
