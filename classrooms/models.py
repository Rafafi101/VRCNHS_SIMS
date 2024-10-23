from .choices import grade_choices
from django.db import models
from accounts.models import Teacher

# Create your models here.


class Gradelevel(models.Model):
    grade = models.CharField(max_length=20, choices=grade_choices, unique=True)

    def __str__(self):
        return self.grade


class Classroom(models.Model):
    gradelevel = models.ForeignKey(
        Gradelevel, blank=True, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=50, null=True, default=None)
    teacher = models.ForeignKey(Teacher, blank=True, null=True, default=None,
                                verbose_name="Teachers", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "Classrooms"

    def __str__(self):
        return self.classroom
