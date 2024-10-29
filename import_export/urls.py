from django.urls import path

from . import views


urlpatterns = [
    path('import_students/', views.import_students, name='import_students'),
    path('export_students/', views.export_all_students, name='export_students'),
]
