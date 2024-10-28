from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import Teacher
from students.models import Student

from .models import Classroom, Gradelevel

# Create your views here.


def classrooms(request):
    classrooms_grade_7 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 7')
    classrooms_grade_8 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 8')
    classrooms_grade_9 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 9')
    classrooms_grade_10 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 10')
    classrooms_grade_11 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 11')
    classrooms_grade_12 = Classroom.objects.filter(
        gradelevel__gradelevel='Grade 12')

    context = {
        'classrooms_grade_7': classrooms_grade_7,
        'classrooms_grade_8': classrooms_grade_8,
        'classrooms_grade_9': classrooms_grade_9,
        'classrooms_grade_10': classrooms_grade_10,
        'classrooms_grade_11': classrooms_grade_11,
        'classrooms_grade_12': classrooms_grade_12,
    }

    return render(request, 'classrooms/classrooms.html', context)


def classroom(request, classroom_id):
    # Retrieve the classroom with the given ID
    classroom = get_object_or_404(Classroom, id=classroom_id)
    # Get all students assigned to this classroom
    students = Student.objects.filter(classroom=classroom)

    context = {
        'classroom': classroom,
        'students': students,
    }
    return render(request, 'classrooms/classroom.html', context)


def add_classroom(request):
    if request.method == 'POST':
        # Retrieve the values from the form
        classroom_name = request.POST.get('classroom_name')
        gradelevel_id = request.POST.get('gradelevel_id')
        teacher_id = request.POST.get('teacher_id')

        try:
            # Attempt to retrieve the Gradelevel object with the given ID
            gradelevel = Gradelevel.objects.get(id=gradelevel_id)

            if teacher_id:  # Check if a teacher is selected
                # Retrieve the Teacher object with the given ID
                teacher = Teacher.objects.get(id=teacher_id)
            else:
                teacher = None  # Set teacher to None if no teacher is selected

            # Create a new Classroom object with the provided values
            Classroom.objects.create(
                classroom=classroom_name, gradelevel=gradelevel, teacher=teacher)

            # Redirect to classrooms view after successful addition
            return redirect('classrooms')

        except Gradelevel.DoesNotExist:
            # Handle case where gradelevel is not found
            return render(request, 'classrooms/add_classroom.html', {
                'error_message': 'Selected grade level does not exist.',
                'gradelevels': Gradelevel.objects.all(),
                'teachers': Teacher.objects.all()
            })
        except Teacher.DoesNotExist:
            # Handle case where teacher is not found
            return render(request, 'classrooms/add_classroom.html', {
                'error_message': 'Selected teacher does not exist.',
                'gradelevels': Gradelevel.objects.all(),
                'teachers': Teacher.objects.all()
            })

    # Retrieve all the available grade levels and teachers for GET request
    gradelevels = Gradelevel.objects.all()
    teachers = Teacher.objects.all()

    # Render the add classroom template with the grade levels and teachers
    return render(request, 'classrooms/add_classroom.html', {'gradelevels': gradelevels, 'teachers': teachers})
