from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Student


def index(request):
    # # List of students
    students = Student.objects.order_by('last_name')

    # Setting into the dictionary
    context = {
        'students': students,
    }

    # Passing to template
    return render(request, 'students/students.html', context)


def student(request):
    return render(request, 'students/student.html')


# Create your views here.
