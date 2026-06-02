from django.contrib import admin
from .models import Student, CourseGroup

# Register your models here.



class StudentAdmin (admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'student_id', 'email', 'group')

admin.site.register(Student, StudentAdmin)

