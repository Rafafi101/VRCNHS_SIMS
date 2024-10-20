from .choices import status_choices, religion_choices, strand_choices, sem_choices, sex_choices, transfer_status_choices, household_income_choices, is_returnee_choices
from datetime import date
from django.db import models
from classrooms.models import Classroom


class Student(models.Model):
    LRN = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    suffix_name = models.CharField(max_length=10, blank=True, null=True)
    status = models.CharField(
        max_length=30, blank=True, null=True, choices=status_choices)
    birthday = models.DateField(default=date.today, null=True)
    religion = models.CharField(
        max_length=30, default='other', null=True, choices=religion_choices)
    other_religion = models.CharField(max_length=30, blank=True, null=True)
    strand = models.CharField(max_length=50, null=True,
                              blank=True, choices=strand_choices)
    age = models.IntegerField(null=True)
    sem = models.CharField(max_length=30, null=True,
                           blank=True, default='None', choices=sem_choices)
    classroom = models.ForeignKey(
        Classroom, null=True, verbose_name="Classrooms", on_delete=models.SET_NULL, default=None)
    sex = models.CharField(max_length=10, null=True, choices=sex_choices)
    birth_place = models.CharField(max_length=100, null=True, blank=True)
    mother_tongue = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=120, null=True, blank=True)
    father_contact = models.CharField(max_length=15, null=True, blank=True)
    mother_name = models.CharField(max_length=120, null=True, blank=True)
    mother_contact = models.CharField(max_length=15, null=True, blank=True)
    guardian_name = models.CharField(max_length=120, null=True, blank=True)
    guardian_contact = models.CharField(max_length=15, null=True, blank=True)
    transfer_status = models.CharField(
        max_length=15, null=True, blank=True, default='Regular', choices=transfer_status_choices)
    household_income = models.CharField(
        max_length=30, null=True, blank=True, choices=household_income_choices)
    is_returnee = models.CharField(
        max_length=5, null=True, blank=True, choices=is_returnee_choices)
    is_dropout = models.BooleanField(default=True)
    is_working_student = models.BooleanField(default=True)
    health_bmi = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    is_4ps = models.BooleanField(default=False)
    notes = models.CharField(max_length=300, blank=True, null=True)

    # GRADE 7 STUDENT HISTORY
    g7_school = models.CharField(max_length=30, null=True, blank=True)
    g7_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g7_section = models.CharField(max_length=15, null=True, blank=True)
    g7_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g7_adviser = models.CharField(max_length=50, null=True, blank=True)
    g7_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # GRADE 8 STUDENT HISTORY
    g8_school = models.CharField(max_length=30, null=True, blank=True)
    g8_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g8_section = models.CharField(max_length=15, null=True, blank=True)
    g8_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g8_adviser = models.CharField(max_length=50, null=True, blank=True)
    g8_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # GRADE 9 STUDENT HISTORY
    g9_school = models.CharField(max_length=30, null=True, blank=True)
    g9_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g9_section = models.CharField(max_length=15, null=True, blank=True)
    g9_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g9_adviser = models.CharField(max_length=50, null=True, blank=True)
    g9_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # GRADE 10 STUDENT HISTORY
    g10_school = models.CharField(max_length=30, null=True, blank=True)
    g10_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g10_section = models.CharField(max_length=15, null=True, blank=True)
    g10_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g10_adviser = models.CharField(max_length=50, null=True, blank=True)
    g10_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # GRADE 11 STUDENT HISTORY
    g11_school = models.CharField(max_length=30, null=True, blank=True)
    g11_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g11_section = models.CharField(max_length=15, null=True, blank=True)
    g11_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g11_adviser = models.CharField(max_length=50, null=True, blank=True)
    g11_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # GRADE 11 STUDENT HISTORY
    g12_school = models.CharField(max_length=30, null=True, blank=True)
    g12_schoolYear = models.CharField(max_length=15, null=True, blank=True)
    g12_section = models.CharField(max_length=15, null=True, blank=True)
    g12_general_average = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    g12_adviser = models.CharField(max_length=50, null=True, blank=True)
    g12_adviserContact = models.CharField(max_length=50, null=True, blank=True)

    # save previous section
    previous_section = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Students"

    def save(self, *args, **kwargs):
        # Calculate the age only if the birthday is not None
        if self.birthday:
            self.age = date.today().year - self.birthday.year
        else:
            self.age = None

        # Call the save method of the parent class to save the object
        super().save(*args, **kwargs)

    def get_changes(self):
        """
        Get the changes made to this record.
        """
        history = self.history.all()
        changes = []
        for h in history:
            delta = h.diff_against(h.prev_record) if h.prev_record else None
            if delta:
                for change in delta.changes:
                    changes.append({
                        'field': change.field,
                        'old': change.old,
                        'new': change.new,
                        'date': h.history_date,
                        'user': h.history_user.get_username() if h.history_user else 'Unknown'
                    })
        return changes

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    def full_name(self):
        return f"{self.last_name}, {self.first_name}"

# Create your models here.
