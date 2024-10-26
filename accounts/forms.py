import datetime
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


class TeacherForm(forms.ModelForm):
    # Additional fields for username, password, and group
    username = forms.CharField(max_length=150, required=True)
    group = forms.ChoiceField(choices=(
        (1, 'TEACHER'), (2, 'ADMIN'), (3, 'BOTH TEACHER AND ADMIN')), required=True)

    class Meta:
        model = Teacher
        fields = '__all__'  # Use all fields from the Teacher model in the form
        exclude = ['user']  # Exclude the user field
        widgets = {
            'birthday': forms.SelectDateWidget(years=range(1900, datetime.date.today().year+1)),
            'appt_date': forms.SelectDateWidget(years=range(1900, datetime.date.today().year+1)),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Set initial values for username and group
        self.fields['username'].initial = self.instance.user.username
        groups = self.instance.user.groups.all()
        if groups.filter(name='TEACHER').exists():
            self.fields['group'].initial = '1'  # TEACHER
        elif groups.filter(name='ADMIN').exists():
            self.fields['group'].initial = '2'  # ADMIN

        # Set custom field order
        self.order_fields(
            ['username', 'first_name', 'last_name', 'group', 'birthday', 'appt_date'])

        # Add the 'date-auto-width' class to birthday and appointment date fields
        self.fields['birthday'].widget.attrs.update(
            {'class': 'date-auto-width'})
        self.fields['appt_date'].widget.attrs.update(
            {'class': 'date-auto-width'})

        # Hide the 'group' field for TEACHER group users
        if user and user.groups.filter(name='TEACHER').exists():
            self.fields.pop('group')

    def save(self, commit=True):
        # Save the teacher model
        teacher = super().save(commit=False)
        username = self.cleaned_data['username']
        group_choice = int(self.cleaned_data['group'])

        # Update the associated user model
        user = teacher.user
        user.username = username
        user.first_name = teacher.first_name  # Update the first name
        user.last_name = teacher.last_name  # Update the last name

        if commit:
            teacher.save()
            user.save()
            # Update the group of the associated user
            teacher_group = Group.objects.get(name='TEACHER')
            admin_group = Group.objects.get(name='ADMIN')

            if group_choice == 1:  # TEACHER
                user.groups.set([teacher_group])
            elif group_choice == 2:  # ADMIN
                user.groups.set([admin_group])

        return teacher
