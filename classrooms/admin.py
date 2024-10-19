from django.contrib import admin
from .models import Classroom, Gradelevel
# Register your models here.


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('gradelevel', 'classroom', 'teacher')


class GradelevelAdmin(admin.ModelAdmin):
    list_display = ('grade', )


admin.site.register(Gradelevel, GradelevelAdmin)
admin.site.register(Classroom, ClassroomAdmin)
