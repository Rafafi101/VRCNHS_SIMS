from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reports', views.reports, name='reports'),
    path('sectioning/', views.sectioning, name='sectioning'),
]
