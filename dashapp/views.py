from django.shortcuts import render


def index(request):
    return render(request, 'dashapp/index.html') # Renderiza la plantilla index.html del dashboard