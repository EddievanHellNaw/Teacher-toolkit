from django.db import models
from groups.models import CourseGroup

#The student model represent a student.
# It contains the first name, the last name, the group and the student ID number  
# it also contains the email of the student 
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    group = models.ForeignKey(CourseGroup, on_delete=models.PROTECT, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"