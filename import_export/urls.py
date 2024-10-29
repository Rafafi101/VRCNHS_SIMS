from django.urls import path

from . import views


urlpatterns = [
    path('import_students/', views.import_students, name='import_students'),
    path('export_students/', views.export_students_to_excel, name='export_students'),
    path('export_classroom_students/', views.export_classroom_students_to_excel,
         name='export_classroom_students'),


]
