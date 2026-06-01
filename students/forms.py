from .models import CourseGroup, Student
from django import forms    

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'email', 'group']


class CourseGroupForm(forms.ModelForm):
    class Meta:
        model = CourseGroup
        fields = ['name', 'subject', 'schedule']   