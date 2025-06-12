from django.shortcuts import render, redirect
#from .models import AboutPage, ContactPage, Student, Notice, Teacher

#Miguel:
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def course(request):
    return render(request, 'course.html')

def details(request):
    return render(request, 'details.html')

def feature(request):
    
    return render(request, 'feature.html')

def team(request):
    
    return render(request, 'team.html')

def review(request):
    
    return render(request, 'review.html')

def contact(request):

    return render(request, 'contact.html')

