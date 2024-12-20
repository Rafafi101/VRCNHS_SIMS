from datetime import date
from django import forms

from classrooms.models import Classroom
from students.models import Student


class EditStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        # Disable the LRN field to make it read-only
        self.fields['LRN'].disabled = True

        # Calculate and display age if birthday is set
        if self.instance.birthday:
            today = date.today()
            age = today.year - self.instance.birthday.year
            if today.month < self.instance.birthday.month or (today.month == self.instance.birthday.month and today.day < self.instance.birthday.day):
                age -= 1
            self.fields['age'] = forms.IntegerField(initial=age, disabled=True)

        # Limit classrooms based on user's role
        if teacher and not is_admin:
            # Limit choices for classroom to the teacher's classrooms
            self.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)
            self.fields['classroom'].initial = Classroom.objects.filter(
                teacher=teacher).first()
        else:
            # Admin can see all classrooms
            self.fields['classroom'].queryset = Classroom.objects.all()

    class Meta:
        model = Student
        fields = '__all__'  # Or specify fields if you want only certain fields


class AddStudentForm(forms.ModelForm):
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
            # Limit the choices for the classroom field to the teacher's classrooms
            self.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)
            self.fields['classroom'].initial = Classroom.objects.filter(
                teacher=teacher).first()

    class Meta:
        model = Student
        fields = fields = '__all__'


class AdminTeacherStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        # When the dae is placed it should adjust to the code.
        if self.instance.birthday:  # the student age automatically calculated when new year comes
            today = date.today()
            next_birthday = self.instance.birthday.replace(year=today.year + 1)
            age = next_birthday.year - self.instance.birthday.year

            if today < next_birthday:
                age -= 1

            self.fields['age'] = forms.IntegerField(initial=age, disabled=True)

        if teacher and is_admin:
            # Include all classrooms in the queryset
            self.fields['classroom'].queryset = Classroom.objects.all()
            # Set the default value for the classroom field to the teacher's classroom
            self.fields['classroom'].initial = teacher.classroom

    class Meta:
        model = Student
        fields = '__all__'


class SpecifiClassroomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extract 'teacher' and 'is_admin' arguments
        teacher = kwargs.pop('teacher', None)
        is_admin = kwargs.pop('is_admin', False)
        super().__init__(*args, **kwargs)

        # Calculate age based on the birthday field in the instance, if available
        if self.instance.birthday:
            today = date.today()
            age = today.year - self.instance.birthday.year
            if today.month < self.instance.birthday.month or (today.month == self.instance.birthday.month and today.day < self.instance.birthday.day):
                age -= 1
            self.fields['age'] = forms.IntegerField(initial=age, disabled=True)

        # Limit the 'classroom' queryset to classrooms associated with the teacher, unless user is admin
        if teacher and not is_admin:
            self.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)
            self.fields['classroom'].initial = Classroom.objects.filter(
                teacher=teacher)

    class Meta:
        model = Student  # Replace with the correct model name for the form
        # Or specify fields explicitly, e.g., ['name', 'classroom', 'birthday']
        fields = '__all__'
