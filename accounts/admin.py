from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'rank', 'get_group')

    def get_group(self, obj):
        groups = obj.user.groups.all()
        return ', '.join([group.name for group in groups]) if groups else 'No Group'

    get_group.short_description = 'Group'

admin.site.register(Teacher, TeacherAdmin)
