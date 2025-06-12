from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('course/', views.course, name="course"),
    path('details/', views.details, name="details"),
    path('feature/', views.feature, name="feature"), 
    path('team/', views.team, name="team"), 
    path('review/', views.review, name="review"), 

]