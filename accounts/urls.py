from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.teacher_register, name='register'),
    path('logout', views.logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_changed.html'),
         name='password_change_done'),

]
