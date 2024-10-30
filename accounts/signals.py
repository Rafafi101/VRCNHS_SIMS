from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'accounts':
        from django.contrib.auth.models import Group
        Group.objects.get_or_create(name='ADMIN')
        Group.objects.get_or_create(name='TEACHER')


@receiver(post_save, sender='auth.User')
def assign_group(sender, instance, created, **kwargs):
    if created:
        from django.contrib.auth.models import Group
        # Automatically assign ADMIN for staff users or superusers
        if instance.is_staff or instance.is_superuser:
            admin_group, _ = Group.objects.get_or_create(name='ADMIN')
            instance.groups.add(admin_group)
        else:
            # Non-staff, non-superuser users default to TEACHER group
            teacher_group, _ = Group.objects.get_or_create(name='TEACHER')
            instance.groups.add(teacher_group)
