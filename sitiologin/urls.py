from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('dashboard/', views.home_logeado_view, name="dashboard_usuario"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # 🔹 Verifica que esté esta línea
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'), # 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'), 
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'), 
    path('login/', CustomLoginView.as_view(), name='login'),

]

