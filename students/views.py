from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from .forms import StudentForm
from .models import Student
from teachers.models import Teacher
from classrooms.models import Classroom
from django.contrib.auth.models import User, Group


def index(request):
    # # List of students
    students = Student.objects.order_by('last_name')

    # Setting into the dictionary
    context = {
        'students': students,
    }

    # Passing to template
    return render(request, 'students/students.html', context)


def student(request, lrn):
    user = request.user
    has_authorization = False

    try:
        # Check if the user is in the ADMIN group
        if Group.objects.get(name='ADMIN') in user.groups.all():
            # If the user is in the ADMIN group, allow access to all student details
            student = Student.objects.get(LRN=lrn)
            has_authorization = True
        else:
            # If the user is not in the ADMIN group, assume they are a teacher
            teacher = Teacher.objects.get(user=user)
            classroom = Classroom.objects.get(teacher=teacher)

            # Try to get the student only if they belong to the same classroom as the teacher
            student = Student.objects.get(LRN=lrn, classroom=classroom)
            has_authorization = True

    except (Group.DoesNotExist, Teacher.DoesNotExist, Classroom.DoesNotExist, Student.DoesNotExist):
        # Handle the case where the user is not a teacher, is not associated with a classroom,
        # or the student is not found. Redirect to the "students" page with an error message.
        messages.error(
            request, "You are not authorized to view this student's profile.")
        return redirect("students")

    context = {'student': student, 'has_authorization': has_authorization}

    return render(request, 'students/student.html', context)


def edit_student(request, lrn):
    student = get_object_or_404(Student, LRN=lrn)
    initial_data = model_to_dict(student)  # Store initial data for comparison
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            edited_fields = []  # Create a list to store edited fields and their previous values

            # Compare the new data with the initial data to detect edits
            for field_name, new_value in form.cleaned_data.items():
                if initial_data[field_name] != new_value:
                    previous_value = initial_data[field_name]
                    field_verbose_name = Student._meta.get_field(
                        field_name).verbose_name
                    edited_fields.append(
                        f"{field_verbose_name} (before: {previous_value})")

            # Store edited fields in the student object
            student.edited_fields = ', '.join(edited_fields)
            student.save()

            form.save()
            messages.success(request, "Student Updated Successfully")

            if request.user.groups.filter(name='TEACHER').exists():
                return redirect("student", lrn=lrn)
            else:
                return redirect("student", lrn=lrn)
    else:
        # Create the form instance without providing initial values
        form = StudentForm(instance=student)

        # Manually set the initial value for the 'sex' field
        form.fields['sex'].initial = student.sex
    context = {'form': form, 'student': student}

    return render(request, 'students/edit_student.html', context)
