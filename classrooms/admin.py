from django.contrib import admin
from .models import Classroom, Gradelevel
# Register your models here.


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('classroom', 'gradelevel', 'teacher')


class GradelevelAdmin(admin.ModelAdmin):
    list_display = ('gradelevel', )


admin.site.register(Gradelevel, GradelevelAdmin)
admin.site.register(Classroom, ClassroomAdmin)
