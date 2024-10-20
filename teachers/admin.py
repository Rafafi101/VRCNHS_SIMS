from django.contrib import admin
from .models import Teacher
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class TeacherInline(admin.StackedInline):
    model = Teacher
    can_delete = False  # Teacher should not be deletable unless the user is deleted first
    verbose_name_plural = 'Teachers'


class CustomizedUserAdmin(UserAdmin):
    inlines = (TeacherInline, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
