from django.shortcuts import render
from django.http import HttpResponse
from .models import Students
# Create your views here.

def student_list(request):
    students=Students.objects.all()
    return render(request, 'student_list.html',)

def student(request):
    return render(request,'portfolio.html')

def profile(request):
    return render(request,'profile.html')

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')