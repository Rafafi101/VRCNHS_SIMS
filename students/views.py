from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
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


# Create your views here.
