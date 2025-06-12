from django.shortcuts import render, redirect
#from .models import AboutPage, ContactPage, Student, Notice, Teacher

# Create your views here.
#Miguel:
def home(request):

    return render(request, 'home.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    contact_text = contact.objects.all()
    data = {"contactDetails": contact_text}
    return render(request, 'contact.html', data)







