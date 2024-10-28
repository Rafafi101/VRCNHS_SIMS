from django.urls import path

from . import views


urlpatterns = [
    path('classrooms/', views.classrooms, name='classrooms'),
    path('add/', views.add_classroom, name='add_classroom'),
    path('<int:classroom_id>/', views.classroom, name='classroom'),
]
