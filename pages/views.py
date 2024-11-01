from django.shortcuts import render
from django.db.models import Count, Value as V, CharField
from django.contrib.auth.decorators import login_required
from django.urls import reverse  # for reverse URL lookup
from django.db.models.functions import Coalesce
from django.shortcuts import redirect
import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from students.models import Student
from accounts.models import Teacher
from classrooms.models import Classroom, Gradelevel
from django.db.models import Count, Q
from plotly.io import to_html as pio_to_html
import plotly.graph_objs as go
import plotly.express as px
from django.db.models import Value as V


# Create your views here.

# Chart aesthetic


def create_pie_chart(labels, sizes, title, chart_width=None, chart_height=None):
    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes)])
    fig.update_layout(title=title, autosize=True,
                      width=chart_width, height=chart_height)
    return fig


def create_bar_chart(labels, sizes, title, chart_width=None, chart_height=None, colorscale='bright'):
    colors = px.colors.qualitative.Plotly
    fig = go.Figure(data=[go.Bar(x=labels, y=sizes, marker_color=colors)])
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)
    fig.update_layout(title=title, autosize=True,
                      width=chart_width, height=chart_height)
    fig.update_layout(
        autosize=True,
        margin=dict(l=0, r=0, b=0, t=30),
        template="plotly",
        modebar_remove=['lasso2d', 'select2d']
    )
    return fig

# Homepage


@login_required(login_url='login')  # Redirects to login if unauthenticated
def index(request):
    # Redirect to teacher page if the user is in the TEACHER group
    if request.user.groups.filter(name='TEACHER').exists():
        return redirect('teacher_page')

    # Logic for ADMIN users
    count = User.objects.count()
    # Calculate male and female student counts
    male_count = Student.objects.filter(Q(sex='M') | Q(sex='Male')).count()
    female_count = Student.objects.filter(Q(sex='F') | Q(sex='Female')).count()
    total_students = male_count + female_count

    # Create pie chart for gender distribution
    gender_fig = create_pie_chart(
        labels=['Male', 'Female'],
        sizes=[male_count, female_count],
        title='Student Gender Distribution'
    )
    gender_chart_div = pio_to_html(
        gender_fig, full_html=False, include_plotlyjs='cdn'
    )

    students = Student.objects.all()

    # Calculate religion distribution
    religion_counts = students.values(
        'religion').annotate(count=Count('religion'))
    religion_fig = create_bar_chart(
        [item['religion'] for item in religion_counts],
        [item['count'] for item in religion_counts],
        'Distribution of Religions'
    )

    # Calculate scholarship distribution (BooleanField)
    is_4ps_true_count = students.filter(is_4ps=True).count()
    is_4ps_false_count = students.filter(is_4ps=False).count()
    scholarship_fig = create_bar_chart(
        ['4Ps Scholar', 'Non-4Ps Scholar'],
        [is_4ps_true_count, is_4ps_false_count],
        'Distribution of Scholars'
    )

    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total_teachers = Teacher.objects.count()
    total_classrooms = Classroom.objects.exclude(
        Q(classroom='SECTIONING') | (
            Q(gradelevel__grade='Grade 12') & Q(classroom='FOR DEPARTURE'))
    ).count()

    # Add variables to context dictionary
    context = {
        'total_students': total_students,
        'gender_chart_div': gender_chart_div,
        'religion_chart': religion_fig.to_html(full_html=False, include_plotlyjs='cdn'),
        'current_datetime': current_datetime,
        'count': count,
        'total_teachers': total_teachers,
        'total_classrooms': total_classrooms,
        'scholarship_chart': scholarship_fig.to_html(full_html=False, include_plotlyjs='cdn'),
    }

    # Render the home.html template with the context data for ADMIN users
    return render(request, 'pages/index.html', context)


def reports(request):
    # Retrieve all students
    students = Student.objects.all()

    # Filter based on grade level (from dropdown)
    selected_gradelevel = request.GET.get('gradelevel', 'all')
    if selected_gradelevel != 'all':
        if selected_gradelevel == 'myclassroom' and request.user.groups.filter(name='TEACHER').exists():
            students = students.filter(classroom__teacher__user=request.user)
        else:
            students = students.filter(
                classroom__gradelevel__id=selected_gradelevel)

    # Aggregate counts for each relevant field with explicit output_field set
    strand_counts = students.values(
        strand_value=Coalesce('strand', V('None'), output_field=CharField())
    ).annotate(count=Count('strand_value'))

    economic_counts = students.values(
        household_income_value=Coalesce(
            'household_income', V('None'), output_field=CharField())
    ).annotate(count=Count('household_income_value'))

    religion_counts = students.values(
        religion_value=Coalesce('religion', V(
            'None'), output_field=CharField())
    ).annotate(count=Count('religion_value'))

    dropout_counts = students.values(
        is_dropout_value=Coalesce(
            'is_dropout', V('No'), output_field=CharField())
    ).annotate(count=Count('is_dropout_value'))

    working_student_counts = students.values(
        is_working_student_value=Coalesce(
            'is_working_student', V('No'), output_field=CharField())
    ).annotate(count=Count('is_working_student_value'))

    scholarship_counts = students.values(
        is_4ps_value=Coalesce('is_4ps', V('No'), output_field=CharField())
    ).annotate(count=Count('is_4ps_value'))

    sex_counts = students.values(
        sex_value=Coalesce('sex', V('Unknown'), output_field=CharField())
    ).annotate(count=Count('sex_value'))

    returnee_counts = students.values(
        is_returnee_value=Coalesce(
            'is_returnee', V('No'), output_field=CharField())
    ).annotate(count=Count('is_returnee_value'))

    status_counts = students.values(
        status_value=Coalesce('status', V('Unknown'), output_field=CharField())
    ).annotate(count=Count('status_value'))

    # Create charts
    strand_chart = create_bar_chart(
        [item['strand_value'] for item in strand_counts],
        [item['count'] for item in strand_counts],
        'Academic Strand Distribution'
    )

    economic_chart = create_bar_chart(
        [item['household_income_value'] for item in economic_counts],
        [item['count'] for item in economic_counts],
        'Household Status Distribution'
    )

    religion_chart = create_bar_chart(
        [item['religion_value'] for item in religion_counts],
        [item['count'] for item in religion_counts],
        'Religion Distribution'
    )

    dropout_chart = create_pie_chart(
        [item['is_dropout_value'] for item in dropout_counts],
        [item['count'] for item in dropout_counts],
        'Dropout Status Distribution'
    )

    working_student_chart = create_pie_chart(
        [item['is_working_student_value'] for item in working_student_counts],
        [item['count'] for item in working_student_counts],
        'Working Student Distribution'
    )

    scholarship_chart = create_pie_chart(
        [item['is_4ps_value'] for item in scholarship_counts],
        [item['count'] for item in scholarship_counts],
        '4P\'s Scholars Distribution'
    )

    sex_chart = create_pie_chart(
        [item['sex_value'] for item in sex_counts],
        [item['count'] for item in sex_counts],
        'Gender Distribution'
    )

    returnee_chart = create_pie_chart(
        [item['is_returnee_value'] for item in returnee_counts],
        [item['count'] for item in returnee_counts],
        'Returnee Status Distribution'
    )

    status_chart = create_bar_chart(
        [item['status_value'] for item in status_counts],
        [item['count'] for item in status_counts],
        'Student Status Distribution'
    )

    # Add charts to context
    context = {
        'strand_chart': strand_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'economic_chart': economic_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'religion_chart': religion_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'dropout_chart': dropout_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'working_student_chart': working_student_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'scholarship_chart': scholarship_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'sex_chart': sex_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'returnee_chart': returnee_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'status_chart': status_chart.to_html(full_html=False, include_plotlyjs='cdn'),
        'selected_gradelevel': selected_gradelevel,
        'current_datetime': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'gradelevels': Gradelevel.objects.all(),
        'user_is_teacher': request.user.groups.filter(name='TEACHER').exists(),
        'selected_filter_name': 'My Classroom' if selected_gradelevel == 'myclassroom' else 'All Grade Levels',
        'values': request.GET,
    }

    return render(request, 'pages/reports.html', context)


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
