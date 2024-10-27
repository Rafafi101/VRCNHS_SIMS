from django.shortcuts import render

from .models import Classroom

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
