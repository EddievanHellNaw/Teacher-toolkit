from django.shortcuts import render, redirect, get_object_or_404

from students.forms import StudentForm
from .models import Student

# Create your views here.
def students_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/students_list.html', context)

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student
    }
    return render(request, 'students/student_detail.html', context)

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('students_list')

    else:
        form = StudentForm()
    
    return render(request, "students/student_form.html", {"form": form})

def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect('students_list')

    else:
        form = StudentForm(instance=student)
    
    return render(request, "students/student_form.html", {"form": form})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
        return redirect('students_list')
    else: 
        return render(request, "students/student_delete.html", {"student": student})