from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib import messages

from .forms import AdminTeacherStudentForm, EditStudentForm, AddStudentForm
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

    is_admin = request.user.groups.filter(name='ADMIN').exists()
    teacher = None
    if not is_admin:
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            messages.error(
                request, "You are not authorized to edit this student's profile.")
            return redirect('students')

    if request.method == 'POST':
        # Pass teacher and is_admin to the form
        form = EditStudentForm(request.POST, instance=student,
                               teacher=teacher, is_admin=is_admin)
        if form.is_valid():
            edited_fields = []  # Create a list to store edited fields and their previous values
            for field_name, new_value in form.cleaned_data.items():
                if initial_data.get(field_name) != new_value:
                    previous_value = initial_data.get(field_name)
                    field_verbose_name = Student._meta.get_field(
                        field_name).verbose_name
                    edited_fields.append(
                        f"{field_verbose_name} (before: {previous_value})")

            student.edited_fields = ', '.join(edited_fields)
            form.save()  # Save the updated student instance
            messages.success(request, "Student Updated Successfully")
            # Redirect after successful update
            return redirect("student", lrn=lrn)
        else:
            print(form.errors)  # Print form errors in the console for debugging
            messages.error(
                request, "There was an issue with the form. Please check the errors.")

    else:
        # Pass teacher and is_admin to the form for GET requests
        form = EditStudentForm(
            instance=student, teacher=teacher, is_admin=is_admin)
        # Preserve initial value for sex field
        form.fields['sex'].initial = student.sex

    context = {'form': form, 'student': student}
    return render(request, 'students/edit_student.html', context)

# RETURN once( )


def add_student(request):
    # Base Add_student
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added Successfully")
            return redirect("students")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {
                                   form[field].label}: {error}")
    else:
        form = AddStudentForm()

    return render(request, 'students/add_student.html', {'form': form})


def delete_student(request, lrn):
    student = Student.objects.get(LRN=lrn)
    student.delete()
    # Set extra_tags to 'danger' for red color
    messages.error(request, "Student Deleted", extra_tags='danger')

    # # Check if the user belongs to the "TEACHER" group
    # if request.user.groups.filter(name='TEACHER').exists():
    #     # Redirect to "user_page" if the user is a teacher
    #     return redirect("user_page")
    # else:
    # Redirect to "students" if the user is not a teacher
    return redirect("students")
