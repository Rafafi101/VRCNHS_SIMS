from django.contrib.auth.models import User
from django.db import models
from datetime import date
from .choices import rank_choices


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    birthday = models.DateField(default=date.today)
    appt_date = models.DateField(null=True, blank=True)  # Date of Appointment
    special_assignment = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=50, blank=True)
    employee_id = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    rank = models.CharField(
        max_length=30, choices=rank_choices, default='None')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    @property
    def user_type(self):
        return 'TEACHER'
