from datetime import date
from django import forms

from classrooms.models import Classroom
from students.models import Student


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        if self.instance.birthday:
            today = date.today()
            age = today.year - self.instance.birthday.year
            if today.month < self.instance.birthday.month or (today.month == self.instance.birthday.month and today.day < self.instance.birthday.day):
                age -= 1
            self.fields['age'] = forms.IntegerField(initial=age, disabled=True)

        if teacher and not is_admin:
            # Limit the choices for the classroom field to the classrooms of the teacher
            self.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)
            # Set the default value for the classroom field to the teacher's classroom
            self.fields['classroom'].initial = Classroom.objects.filter(
                teacher=teacher)

    class Meta:
        model = Student
        fields = '__all__'
