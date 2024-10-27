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
    total_classrooms = Classroom.objects.count()

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

    # Pass the aggregated data to the template for chart rendering or display
    context = {
        'strand_counts': strand_counts,
        'economic_counts': economic_counts,
        'religion_counts': religion_counts,
        'dropout_counts': dropout_counts,
        'working_student_counts': working_student_counts,
        'scholarship_counts': scholarship_counts,
        'sex_counts': sex_counts,
        'returnee_counts': returnee_counts,
        'status_counts': status_counts,
    }

    return render(request, 'pages/reports.html', context)
