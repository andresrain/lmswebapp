from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homeapp_index'), # Ruta para el hommeapp
]