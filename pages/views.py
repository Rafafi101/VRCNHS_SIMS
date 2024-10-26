import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from students.models import Student
from accounts.models import Teacher
from classrooms.models import Classroom
from django.db.models import Count, Q
from plotly.io import to_html as pio_to_html
import plotly.graph_objs as go
import plotly.express as px

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
    )
    return fig

# Homepage


def index(request):
    # Redirect to teacher page if the user is in the TEACHER group
    if request.user.groups.filter(name='TEACHER').exists():
        # Adjust to your actual URL name for teacher page
        return redirect('teacher_page')

    # Logic for ADMIN users
    count = User.objects.count()
    # Calculate male and female student counts
    male_count = Student.objects.filter(Q(sex='M') | Q(sex='Male')).count()
    female_count = Student.objects.filter(Q(sex='F') | Q(sex='Female')).count()
    # Calculate total student count
    total_students = male_count + female_count
    # Create pie chart for gender distribution
    gender_fig = create_pie_chart(
        labels=['Male', 'Female'],
        sizes=[male_count, female_count],
        title='Student Gender Distribution'
    )
    gender_chart_div = pio_to_html(
        gender_fig, full_html=False, include_plotlyjs='cdn')

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

    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Retrieve total teachers and classrooms
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
