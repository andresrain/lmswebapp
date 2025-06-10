from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html') # este es el template que se va a renderizar