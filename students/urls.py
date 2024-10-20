from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='students'),
    path('<int:lrn>', views.student, name='student'),
]
