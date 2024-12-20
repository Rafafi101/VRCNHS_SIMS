from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from students.models import Student

from .models import Teacher
from .forms import TeacherForm, TeacherRegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username if currently exists in the database
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is takes')
                return redirect('register')
            else:
                # Check email if currently exists in the database
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    # looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def teacher_register(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "User registration was successful!")
            # Redirect to login page after successful registration
            return redirect('login')
        else:
            # If form is invalid, show an error message
            messages.error(
                request, "There was an error in the form. Please correct the fields highlighted in red.")
    else:
        form = TeacherRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def teachers(request):
    # form = TeacherSearchForm(request.GET or None)
    teachers = Teacher.objects.all()

    # if form.is_valid():
    #     query = form.cleaned_data['query']
    #     teachers = teachers.filter(
    #         Q(last_name__icontains=query) |
    #         Q(first_name__icontains=query)
    #     )
    #     print("Debug Statement: Searched Teacher -", query)  # Debug statement

    # context = {'form': form, 'teachers': teachers}
    context = {'teachers': teachers}
    return render(request, 'accounts/teachers.html', context)


def edit_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    user = teacher.user
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher, user=request.user)
        username = request.POST.get('username', '')
        if form.is_valid() and not User.objects.filter(username=username).exclude(pk=user.pk).exists():
            user.username = username
            user.save()
            form.save()
            messages.success(request, 'Teacher Updated')
            return redirect('teachers')
        else:
            messages.error(
                request, "Username already exists or form is invalid.")
    else:
        form = TeacherForm(instance=teacher, user=request.user)
    return render(request, 'accounts/edit_teacher.html', {'form': form, 'teacher_id': teacher_id, 'username': user.username})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('login')


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    # Check if the user has permission to delete the teacher
    if request.user.has_perm('delete_teacher', teacher):
        # Delete the associated user
        user = teacher.user  # Access the related user
        teacher.delete()  # Delete the Teacher instance
        user.delete()  # Delete the User instance
        messages.error(
            request, "Teacher and associated user deleted", extra_tags='danger')
        return redirect("teachers")
    else:
        # Handle unauthorized access (optional)
        return HttpResponse("Unauthorized access")


def teacher_page(request):
    # Retrieve the teacher associated with the current user
    teacher = get_object_or_404(Teacher, user=request.user)

    # Retrieve all classrooms associated with the teacher
    classrooms = teacher.classroom_set.all()

    if classrooms.exists():
        # If at least one classroom exists
        classroom = classrooms[0]  # Get the first classroom
        # Filter students based on the classroom
        students = Student.objects.filter(classroom=classroom)
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
    else:
        # If no classrooms exist
        classroom = None
        students = []
        teacher_name = None

    # Check if the teacher is not assigned a classroom
    if not classrooms:
        classroom_name = None
    else:
        classroom_name = f"{classroom.gradelevel.gradelevel} '{
            classroom.classroom}'"

    context = {
        'classroom_name': classroom_name,
        'teacher_name': teacher_name,
        'students': students
    }
    return render(request, 'accounts/teacher_page.html', context)
