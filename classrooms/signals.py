from django.db.models.signals import post_migrate
from .models import Gradelevel, Classroom
from django.dispatch import receiver


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'classrooms':
        Gradelevel.objects.get_or_create(grade='Grade 7')
        Gradelevel.objects.get_or_create(grade='Grade 8')
        Gradelevel.objects.get_or_create(grade='Grade 9')
        Gradelevel.objects.get_or_create(grade='Grade 10')
        Gradelevel.objects.get_or_create(grade='Grade 11')
        Gradelevel.objects.get_or_create(grade='Grade 12')
