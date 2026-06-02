from .models import CourseGroup
from django import forms


class CourseGroupForm(forms.ModelForm):
    class Meta:
        model = CourseGroup
        fields = ['name', 'schedule', 'subject']   