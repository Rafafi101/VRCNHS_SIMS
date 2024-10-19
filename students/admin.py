from django.contrib import admin
from .models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('LRN', 'full_name',
                    'status', 'age', 'classroom', 'general_average')


admin. site.register(Student, StudentAdmin)
