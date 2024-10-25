from django import forms
from django.contrib.auth.models import User, Group
from .models import Teacher
from .choices import rank_choices
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class TeacherRegistrationForm(UserCreationForm):
    # Additional fields for Teacher model
    birthday = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}), required=True)
    appt_date = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}), required=False)
    special_assignment = forms.CharField(max_length=100, required=False)
    department = forms.CharField(max_length=50, required=False)
    employee_id = forms.CharField(max_length=30, required=True)
    rank = forms.ChoiceField(choices=rank_choices, required=True)
    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2',
                  'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()

            # Add user to TEACHER group
            teacher_group = Group.objects.get(name='TEACHER')
            user.groups.add(teacher_group)

            # Create Teacher instance with additional fields
            Teacher.objects.create(
                user=user,
                birthday=self.cleaned_data['birthday'],
                appt_date=self.cleaned_data['appt_date'],
                special_assignment=self.cleaned_data['special_assignment'],
                department=self.cleaned_data['department'],
                employee_id=self.cleaned_data['employee_id'],
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                rank=self.cleaned_data['rank']
            )

        return user
