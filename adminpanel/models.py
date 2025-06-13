from django.db import models
from django.contrib.auth.models import User

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cursos = models.ManyToManyField(Curso, blank=True)

    def __str__(self):
        return self.usuario.get_full_name()

class Recurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='recursos/', blank=True, null=True)
    enlace = models.URLField(blank=True, null=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class SolicitudInscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aprobada', 'Aprobada'), ('rechazada', 'Rechazada')], default='pendiente')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.estudiante} → {self.curso}"
