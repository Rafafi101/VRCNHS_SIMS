from datetime import date
from django import forms

from classrooms.models import Classroom
from students.models import Student


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        # Disable the LRN field to make it read-only
        self.fields['LRN'].disabled = True

        if self.instance.birthday:
            today = date.today()
            age = today.year - self.instance.birthday.year
            if today.month < self.instance.birthday.month or (today.month == self.instance.birthday.month and today.day < self.instance.birthday.day):
                age -= 1
            self.fields['age'] = forms.IntegerField(initial=age, disabled=True)

        if teacher and not is_admin:
            # Limit the choices for the classroom field to the teacher's classrooms
            self.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)
            self.fields['classroom'].initial = Classroom.objects.filter(
                teacher=teacher).first()

    class Meta:
        model = Student
        fields = ['LRN', 'last_name', 'first_name', 'middle_name', 'suffix_name', 'status', 'birthday', 'religion', 'other_religion', 'strand', 'age', 'sem', 'classroom', 'sex', 'birth_place', 'mother_tongue', 'address', 'father_name', 'father_contact', 'mother_name', 'mother_contact', 'guardian_name', 'guardian_contact', 'transfer_status', 'household_income', 'is_returnee', 'is_dropout', 'is_working_student', 'health_bmi', 'general_average', 'is_4ps', 'notes', 'g7_school', 'g7_schoolYear', 'g7_section', 'g7_general_average', 'g7_adviser', 'g7_adviserContact',
                  'g8_school', 'g8_schoolYear', 'g8_section', 'g8_general_average', 'g8_adviser', 'g8_adviserContact', 'g9_school', 'g9_schoolYear', 'g9_section', 'g9_general_average', 'g9_adviser', 'g9_adviserContact', 'g10_school', 'g10_schoolYear', 'g10_section', 'g10_general_average', 'g10_adviser', 'g10_adviserContact', 'g11_school', 'g11_schoolYear', 'g11_section', 'g11_general_average', 'g11_adviser', 'g11_adviserContact', 'g12_school', 'g12_schoolYear', 'g12_section', 'g12_general_average', 'g12_adviser', 'g12_adviserContact', 'previous_section']
