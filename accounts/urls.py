from django.urls import include, path

from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.teacher_register, name='register'),
    path('logout', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
]
