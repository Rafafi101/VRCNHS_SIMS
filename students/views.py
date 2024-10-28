from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.db.models import Q
import logging


from .forms import AdminTeacherStudentForm, EditStudentForm, AddStudentForm, SpecifiClassroomForm
from .models import Student
from accounts.models import Teacher
from classrooms.models import Classroom, Gradelevel


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

    # For non-admin users, retrieve the teacher instance if possible
    if not is_admin:
        try:
            teacher = Teacher.objects.get(user=request.user)
        except Teacher.DoesNotExist:
            messages.error(
                request, "You are not authorized to edit this student's profile.")
            return redirect('students')

    if request.method == 'POST':
        # Pass teacher and is_admin to the form
        form = EditStudentForm(
            request.POST, instance=student, teacher=teacher, is_admin=is_admin)
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

            # Conditional redirect based on group
            if is_admin:
                return redirect("students")  # Redirect for admin
            else:
                return redirect("teacher_page")  # Redirect for teacher
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
    user = request.user

    if user.groups.filter(name='ADMIN').exists():
        # ADMIN Add_student
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

    elif user.groups.filter(name='TEACHER').exists():
        # Access the teacher profile related to the user
        teacher = user.teacher_profile
        is_admin = user.groups.filter(name='ADMIN').exists()

        if request.method == 'POST':
            form = SpecifiClassroomForm(
                request.POST, teacher=teacher, is_admin=is_admin)
            if form.is_valid():
                form.save()
                # Notify user of successful Creation of student
                messages.success(request, "Student Added Successfully")
                return redirect("teacher_page")
        else:
            form = SpecifiClassroomForm(teacher=teacher, is_admin=is_admin)
            form.fields['classroom'].queryset = Classroom.objects.filter(
                teacher=teacher)

    return render(request, 'students/add_student.html', {'form': form})


def search_student(request):
    students_list = Student.objects.order_by('last_name', 'first_name')

    if 'query_student' in request.GET:
        query_student = request.GET['query_student']
        if query_student:
            students_list = students_list.filter(
                Q(LRN__icontains=query_student) |
                Q(last_name__icontains=query_student) |
                Q(first_name__icontains=query_student) |
                Q(middle_name__icontains=query_student)
            )
    context = {'students': students_list,
               'values': request.GET}

    return render(request, 'students/search_student.html', context)


def delete_student(request, lrn):
    student = Student.objects.get(LRN=lrn)
    student.delete()
    # Set extra_tags to 'danger' for red color
    messages.error(request, "Student Deleted", extra_tags='danger')

    # Check if the user belongs to the "TEACHER" group
    if request.user.groups.filter(name='TEACHER').exists():
        # Redirect to "user_page" if the user is a teacher
        return redirect("teacher_page")
    else:
        # Redirect to "students" if the user is not a teacher
        return redirect("students")


logger = logging.getLogger(__name__)


def get_next_grade(current_grade):
    grade_sequence = ['Grade 7', 'Grade 8',
                      'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12']
    try:
        current_index = grade_sequence.index(current_grade)
        next_index = current_index + 1
        if next_index < len(grade_sequence):
            return grade_sequence[next_index]
        else:
            return None  # No next grade (end of sequence)
    except ValueError:
        return None  # Current grade not found in the sequence


def bulk_promote_students(request):
    response_data = {'success': False, 'message': 'Failed to promote students'}

    if not request.user.groups.filter(name='TEACHER').exists():
        messages.error(
            request, "You don't have permission to promote students.")
        return redirect('teacher_page')

    # Check if there are students with the status "Currently Enrolled"
    if Student.objects.filter(classroom__teacher__user=request.user, status='Currently Enrolled').exists():
        messages.error(
            request, 'No student should have a status of "Currently Enrolled" anymore if you want to Promote in Bulk.')
        return redirect('teacher_page')

    if request.method == 'POST':
        try:
            # Retrieve the teacher instance for the current user
            try:
                teacher_instance = Teacher.objects.get(user=request.user)
            except Teacher.DoesNotExist:
                messages.error(
                    request, 'No teacher profile found for the current user.')
                return redirect('teacher_page')

            # Find students associated with the teacher by filtering students through the classroom
            students_to_promote = Student.objects.filter(
                classroom__teacher=teacher_instance)

            if not students_to_promote.exists():
                # If no students are found, raise an error message
                logger.error(
                    "No students found for the current teacher's classroom.")
                response_data['message'] = 'No students are associated with your classroom.'
                messages.error(request, response_data['message'])
                return redirect('teacher_page')

            # Assuming all students belong to the same grade level since they are in the same classroom
            user_classroom = students_to_promote.first().classroom
            current_grade = user_classroom.gradelevel.gradelevel

            # Determine the next grade level based on the teacher's current grade level
            next_grade = get_next_grade(current_grade)

            if next_grade is None:
                # If there's no next grade, the student is in Grade 12 and will be moved to "FOR DEPARTURE"
                next_grade_instance = Gradelevel.objects.get(
                    gradelevel='Grade 12')
                next_classroom = Classroom.objects.get(
                    gradelevel=next_grade_instance, classroom='FOR DEPARTURE')
            else:
                # For students being promoted to the next grade level, they will go to the "SECTIONING" classroom
                next_grade_instance = Gradelevel.objects.get(
                    gradelevel=next_grade)
                next_classroom = Classroom.objects.get(
                    gradelevel=next_grade_instance, classroom='SECTIONING')

            for student in students_to_promote:
                # Store current classroom name
                student.previous_section = str(student.classroom)

                if student.status == 'For Promotion':
                    # Update student details for promotion
                    update_student_promotion_data(
                        student, current_grade, user_classroom, request.user)
                    student.gradelevel = next_grade_instance
                    student.classroom = next_classroom

                elif student.status == 'For Retention':
                    # Update student details for retention, keep the same grade level but assign SECTIONING classroom
                    update_student_promotion_data(
                        student, current_grade, user_classroom, request.user)
                    student.classroom = Classroom.objects.get(
                        gradelevel__gradelevel=current_grade, classroom='SECTIONING')

                elif student.status in ['For Graduation', 'For Dropout', 'For Transfer']:
                    # Students with these statuses will be assigned to the "FOR DEPARTURE" classroom in Grade Level 12
                    student.classroom = Classroom.objects.get(
                        gradelevel__gradelevel='Grade 12', classroom='FOR DEPARTURE')

                student.save()

            response_data['success'] = True
            response_data['message'] = f'Bulk promotion to {
                next_grade if next_grade else "Grade 12 FOR DEPARTURE"} successful!'
            messages.success(request, response_data['message'])

            return redirect('teacher_page')

        except Exception as e:
            logger.error(f"An error occurred during bulk promotion: {str(e)}")
            response_data['message'] = f"Failed to promote students: {str(e)}"
            messages.error(request, response_data['message'])
            return redirect('teacher_page')

    return redirect('teacher_page')


def update_student_promotion_data(student, current_grade, classroom, user):
    """Helper function to update student data for promotion or retention"""
    if current_grade == 'Grade 7':
        student.g7_section = classroom.classroom
        student.g7_general_average = student.general_average
        student.g7_adviser = f"{user.first_name} {user.last_name}"
    elif current_grade == 'Grade 8':
        student.g8_section = classroom.classroom
        student.g8_general_average = student.general_average
        student.g8_adviser = f"{user.first_name} {user.last_name}"
    elif current_grade == 'Grade 9':
        student.g9_section = classroom.classroom
        student.g9_general_average = student.general_average
        student.g9_adviser = f"{user.first_name} {user.last_name}"
    elif current_grade == 'Grade 10':
        student.g10_section = classroom.classroom
        student.g10_general_average = student.general_average
        student.g10_adviser = f"{user.first_name} {user.last_name}"
    elif current_grade == 'Grade 11':
        student.g11_section = classroom.classroom
        student.g11_general_average = student.general_average
        student.g11_adviser = f"{user.first_name} {user.last_name}"
    elif current_grade == 'Grade 12':
        student.g12_section = classroom.classroom
        student.g12_general_average = student.general_average
        student.g12_adviser = f"{user.first_name} {user.last_name}"


def sectioning(request):
    # Filter students who are either 'For Promotion' or 'For Retention' and are in the "SECTIONING" classroom
    query_conditions = Q(
        (Q(status='For Promotion') | Q(status='For Retention')) &
        Q(classroom__classroom='SECTIONING')
    )

    # Get students per grade level individually
    students_grade_8 = Student.objects.filter(
        query_conditions, classroom__gradelevel__gradelevel='Grade 8')
    students_grade_9 = Student.objects.filter(
        query_conditions, classroom__gradelevel__gradelevel='Grade 9')
    students_grade_10 = Student.objects.filter(
        query_conditions, classroom__gradelevel__gradelevel='Grade 10')
    students_grade_11 = Student.objects.filter(
        query_conditions, classroom__gradelevel__gradelevel='Grade 11')
    students_grade_12 = Student.objects.filter(
        query_conditions, classroom__gradelevel__gradelevel='Grade 12')

    # Filter students for departure based on status
    for_departure = Student.objects.filter(
        Q(status='For Graduation') | Q(
            status='For Dropout') | Q(status='For Transfer')
    )

    # Assuming you have a predefined list of grade levels
    grade_levels = Gradelevel.objects.all()
    grade_level_classrooms = {grade.id: Classroom.objects.filter(
        gradelevel=grade) for grade in grade_levels}

    # Add classroom options to each student
    for student in students_grade_8:
        student.classroom_options = grade_level_classrooms.get(
            student.classroom.gradelevel.id, [])
        student.LRN_str = str(student.LRN)

    for student in students_grade_9:
        student.classroom_options = grade_level_classrooms.get(
            student.classroom.gradelevel.id, [])
        student.LRN_str = str(student.LRN)

    for student in students_grade_10:
        student.classroom_options = grade_level_classrooms.get(
            student.classroom.gradelevel.id, [])
        student.LRN_str = str(student.LRN)

    for student in students_grade_11:
        student.classroom_options = grade_level_classrooms.get(
            student.classroom.gradelevel.id, [])
        student.LRN_str = str(student.LRN)

    for student in students_grade_12:
        student.classroom_options = grade_level_classrooms.get(
            student.classroom.gradelevel.id, [])
        student.LRN_str = str(student.LRN)

    # Prepare context data with the updated queries
    context = {
        'students_grade_8': students_grade_8,
        'students_grade_9': students_grade_9,
        'students_grade_10': students_grade_10,
        'students_grade_11': students_grade_11,
        'students_grade_12': students_grade_12,
        'for_departure': for_departure,
    }

    return render(request, 'pages/sectioning.html', context)


def assign_classroom_bulk(request, grade):
    if request.method == 'POST':
        # List to store student LRNs for updating status
        student_lrns = []

        for key, value in request.POST.items():
            if key.startswith('classroom_'):
                student_lrn_str = key.split('_')[1]
                classroom_id = value

                try:
                    # Convert LRN to string for comparison
                    student = Student.objects.get(LRN=str(student_lrn_str))
                    classroom = Classroom.objects.get(id=classroom_id)
                    student.classroom = classroom
                    student.status = 'Currently Enrolled'  # Update status to "Currently Enrolled"
                    student.general_average = None
                    student.save()
                    student_lrns.append(student_lrn_str)  # Use LRN_str here

                except Student.DoesNotExist:
                    messages.warning(request, f"Student with LRN {
                                     student_lrn_str} does not exist. Skipping.")
                    continue

                except Classroom.DoesNotExist:
                    messages.warning(request, f"Classroom with ID {
                                     classroom_id} does not exist. Skipping.")
                    continue

        # Update status for all selected students
        Student.objects.filter(LRN__in=student_lrns).update(
            status='Currently Enrolled')

        messages.success(
            request, 'Students assigned to classrooms successfully.')
        return redirect('sectioning')  # Redirect back to the sectioning page
