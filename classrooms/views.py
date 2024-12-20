from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import Teacher
from students.models import Student

from .models import Classroom, Gradelevel
from django.contrib import messages

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


def edit_classroom(request, classroom_id):
    # Retrieve the classroom object based on the provided classroom_id
    classroom = get_object_or_404(Classroom, id=classroom_id)

    if request.method == 'POST':
        # Retrieve the form data submitted via POST
        classroom_name = request.POST.get('classroom_name')
        gradelevel_id = request.POST.get('gradelevel_id')
        teacher_id = request.POST.get('teacher_id')

        # Retrieve and validate the gradelevel
        try:
            gradelevel = Gradelevel.objects.get(id=gradelevel_id)
        except Gradelevel.DoesNotExist:
            messages.error(request, "Grade level does not exist.")
            return redirect('edit_classroom', classroom_id=classroom_id)

        # Retrieve and validate the teacher if a teacher is selected
        if teacher_id == "-1":
            teacher = None
        else:
            try:
                teacher = Teacher.objects.get(id=teacher_id)
            except Teacher.DoesNotExist:
                messages.error(request, "Teacher does not exist.")
                return redirect('edit_classroom', classroom_id=classroom_id)

        # Update the classroom object with the new data
        classroom.classroom = classroom_name
        classroom.gradelevel = gradelevel
        classroom.teacher = teacher
        classroom.save()

        # Add success message
        messages.success(request, 'Classroom was successfully edited!')

        # Redirect to the classrooms page
        return redirect('classrooms')

    # Retrieve all gradelevels and teachers for rendering the form
    gradelevels = Gradelevel.objects.all()
    teachers = Teacher.objects.all()

    # Prepare the context to pass to the template
    context = {
        'classroom': classroom,
        'gradelevels': gradelevels,
        'teachers': teachers,
        'current_gradelevel': classroom.gradelevel.id
    }

    # Render the edit_classroom.html template with the provided context
    return render(request, 'classrooms/edit_classroom.html', context)


def classrooms(request):
    # Retrieve all classrooms by grade level
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

    # Retrieve all teachers
    teachers = Teacher.objects.all()

    context = {
        'classrooms_grade_7': classrooms_grade_7,
        'classrooms_grade_8': classrooms_grade_8,
        'classrooms_grade_9': classrooms_grade_9,
        'classrooms_grade_10': classrooms_grade_10,
        'classrooms_grade_11': classrooms_grade_11,
        'classrooms_grade_12': classrooms_grade_12,
        'teachers': teachers,
    }

    return render(request, 'classrooms/classrooms.html', context)


def assign_teacher(request, classroom_id):
    # Only handle POST requests
    if request.method == 'POST':
        # Retrieve the classroom object
        classroom = get_object_or_404(Classroom, id=classroom_id)

        # Get the selected teacher ID from the form
        teacher_id = request.POST.get('teacher_id')

        if teacher_id == "":
            # If no teacher selected, set teacher to None
            classroom.teacher = None
        else:
            try:
                # Get the teacher object
                teacher = Teacher.objects.get(id=teacher_id)
                classroom.teacher = teacher
            except Teacher.DoesNotExist:
                messages.error(request, "Selected teacher does not exist.")
                return redirect('classrooms')

        # Save the updated classroom object
        classroom.save()
        messages.success(request, "Teacher assignment updated successfully.")

    # Redirect back to the classrooms page
    return redirect('classrooms')


def delete_classroom(request, classroom_id):
    # Retrieve the classroom object based on the provided classroom_id
    classroom = get_object_or_404(Classroom, id=classroom_id)

    if request.method == 'POST':
        # Debug statement for deleting classroom
        print("Debug Statement: Deleting Classroom -", classroom.classroom)

        # Capture the classroom name before deletion for messaging
        classroom_name = classroom.classroom

        # Delete the classroom
        classroom.delete()

        # Add a success message with the name of the deleted classroom
        messages.error(request, f'Classroom "{
            classroom_name}" was deleted.')

    # Redirect back to the classrooms page
    return redirect('classrooms')
