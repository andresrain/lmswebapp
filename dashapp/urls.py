from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'), # Ruta para el dashboard
]