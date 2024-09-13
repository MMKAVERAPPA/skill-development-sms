from django.shortcuts import render, redirect,get_object_or_404
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
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        ph_num = request.POST['phone_number']
        dob = request.POST['date_of_birth']
        
        Students.objects.create(
            first_name = fname,
            last_name = lname,
            email = email,
            phone_number = ph_num,
            date_of_birth = dob,
        )
        return redirect('student_list')
    return render(request,'student_form.html')

# Update existing student
def student_update(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == 'POST':
        student.first_name = request.POST['first_name']
        student.last_name = request.POST['last_name']
        student.email = request.POST['email']
        student.phone_number = request.POST['phone_number']
        student.date_of_birth = request.POST['date_of_birth']
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
