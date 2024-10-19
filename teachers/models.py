from .choices import rank_choices
from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=date.today)
    appt_date = models.DateField(null=True, blank=True)  # Date of Appointment
    special_assignment = models.CharField(
        max_length=100, blank=True)  # Special Assignment
    department = models.CharField(max_length=50, blank=True)  # Department
    employee_id = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    rank = models.CharField(
        max_length=30, choices=rank_choices, default='None')

    def __str__(self):
        return self.last_name + ' ' + self.first_name
