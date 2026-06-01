from django.db import models

# Create your models here.
#The group model represet a group of students
#it containt the name of the group, the date it was created at and the subject that is taught.
#It also contains the schedule of the class
class CourseGroup(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    schedule = models.CharField(max_length=100)    
    subject = models.CharField(max_length=100)

    def totalStudentsCount(self):
        return self.students.count()    
    
    def __str__(self):
        return self.name

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