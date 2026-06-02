from django.contrib import admin
from groups.models import CourseGroup

# Register your models here.
class CourseGroupAdmin (admin.ModelAdmin):
    list_display = ('name', 'subject', 'schedule', 'created_at', 'totalStudentsCount')


admin.site.register(CourseGroup, CourseGroupAdmin)