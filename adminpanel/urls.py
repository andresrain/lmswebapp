from django.urls import path
from . import views

urlpatterns = [

    path('general/', views.general, name='dashboard'),
    path('cursos/', views.CursosDisponiblesView.as_view(), name='ver_cursos'),
    path('estudiantes/', views.EstudiantesRegistradosView.as_view(), name='ver_estudiantes'),
    path('recursos/', views.SubirRecursoView.as_view(), name='ver_recursos'),
    path('solicitudes/', views.SolicitudesView.as_view(), name='ver_solicitudes'),
]
