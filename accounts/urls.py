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
    path('teachers/', views.teachers, name='teachers'),
    path('edit_teacher/<int:teacher_id>/',
         views.edit_teacher, name='edit_teacher'),
    path('delete_teacher/<int:teacher_id>/',
         views.delete_teacher, name='delete_teacher'),
    path('teacher_page/', views.teacher_page, name='teacher_page'),
]
