from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='students'),
    path('<int:lrn>', views.student, name='student'),
    path('edit/<int:lrn>', views.edit_student, name='edit_student'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:lrn>/', views.delete_student, name='delete_student'),
]
