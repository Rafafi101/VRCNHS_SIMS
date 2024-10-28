from django.urls import path

from . import views


urlpatterns = [
    path('classrooms/', views.classrooms, name='classrooms'),
    path('<int:classroom_id>/', views.classroom, name='classroom'),
]
