from django.contrib import admin
from .models import Student, CourseGroup

# Register your models here.

class CourseGroupAdmin (admin.ModelAdmin):
    list_display = ('name', 'subject', 'schedule', 'created_at', 'totalStudentsCount')

class StudentAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'group')

admin.site.register(Student, StudentAdmin)
admin.site.register(CourseGroup, CourseGroupAdmin)

