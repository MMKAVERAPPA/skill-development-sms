from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Students

# Existing views
def student_list(request):
    students = Students.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student(request):
    return render(request, 'portfolio.html')

def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

# Create new student
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        if name and age:
            Students.objects.create(name=name, age=age)
            return redirect('student_list')
    return render(request, 'student_form.html')

# Update existing student
def student_update(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student})

# Delete student
def student_delete(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
