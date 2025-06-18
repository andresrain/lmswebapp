from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView
from courses.models import Course


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_logeado')  # Ya está logueado, redirige

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home_logeado')  # Redirige al home personalizado
        else:
            messages.error(request, 'Usuario o contraseña inválidos.')
    else:
        form = AuthenticationForm()

    return render(request, 'sitiologin/login.html', {'form': form})


def home_logeado_view(request):
    all_courses = Course.objects.filter(is_active=True)
    context = {
        'usuario_actual': request.user,
        'cursos': all_courses
    }
    return render(request, 'sitiologin/home_logeado.html', context)


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect(reverse('login'))  # Redirige al login


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirige si ya está logueado
            return redirect('dashboard_usuario')
        return super().dispatch(request, *args, **kwargs)
