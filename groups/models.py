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