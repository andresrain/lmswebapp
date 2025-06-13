# users/urls.py

from django.urls import path
from . import views

app_name = 'users'  # Add this line

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_new_user, name='create_user'),
]

