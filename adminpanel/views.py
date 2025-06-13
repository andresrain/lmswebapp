from django.shortcuts import render, redirect
from django.views import View
from .models import Curso, Estudiante, Recurso, SolicitudInscripcion
from .forms import RecursoForm

def general(request):
    return render(request, 'adminpanel/general.html')

class CursosDisponiblesView(View):
    def get(self, request):
        cursos = Curso.objects.all()
        return render(request, 'adminpanel/cursos_disponibles.html', {'cursos': cursos})

class EstudiantesRegistradosView(View):
    def get(self, request):
        estudiantes = Estudiante.objects.select_related('usuario').all()
        return render(request, 'adminpanel/estudiantes_registrados.html', {'estudiantes': estudiantes})

class SubirRecursoView(View):
    def get(self, request):
        form = RecursoForm()
        return render(request, 'adminpanel/subir_recurso.html', {'form': form})

    def post(self, request):
        form = RecursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cursos')  # o a donde desees
        return render(request, 'adminpanel/subir_recurso.html', {'form': form})

class SolicitudesView(View):
    def get(self, request):
        solicitudes = SolicitudInscripcion.objects.select_related('estudiante', 'curso').order_by('-fecha_envio')
        return render(request, 'adminpanel/solicitudes.html', {'solicitudes': solicitudes})
