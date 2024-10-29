from django.urls import path

from . import views


urlpatterns = [
    path('download-template/', views.download_template, name='download_template'),
    path('import_students/', views.import_students, name='import_students'),
    path('export_students/', views.export_students_to_excel, name='export_students'),
    path('export_classroom_students/', views.export_classroom_students_to_excel,
         name='export_classroom_students'),
    path('export_and_delete_students_for_departure/', views.export_and_delete_students_for_departure,
         name='export_and_delete_students_for_departure'),
    path('import_classrooms/', views.import_classrooms_from_excel,
         name='import_classrooms'),
    path('export_classrooms/', views.export_classrooms_to_excel,
         name='export_classrooms'),

]
