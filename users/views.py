# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course

@login_required
def dashboard(request):
    user = request.user # get the current user
    # Fetch data for the dashboard
    enrolled_courses_count = request.user.enrolled_courses.count()  # Count courses the user is enrolled in
    active_courses_count = Course.objects.filter(students=request.user).count()
    online_courses_count = Course.objects.filter(students=request.user).count()
    #Corrected: Use user.completed_courses
    #completed_courses_count = user.completed_courses.count()
    completed_courses_count = 0  # Valor por defecto o lógico si no está implementado aún
    User = get_user_model()
    students_count = User.objects.count()

    # Example - Replace with actual calculation based on transactions
    total_earnings = "$7.461.767"
    courses_sold = "56.489"

    instructors_count = Course.objects.all().count() # Total courses instead of # instructors

    context = {
        'enrolled_courses_count': enrolled_courses_count,
        'active_courses_count': active_courses_count,
        'completed_courses_count': completed_courses_count,
        'students_count': students_count,
        'online_courses_count': online_courses_count,
        'total_earnings': total_earnings,
        'courses_sold': courses_sold,
        'instructors_count': instructors_count,

    }
    return render(request, 'users/dashboard.html', context) # Render dashboard.html

@login_required
def create_new_user(request):
  if request.method == 'POST':  # Only handle POST requests
      username = request.POST.get('username') # Get username from form
      password = request.POST.get('password') # Get password from form
      email = request.POST.get('email', '')       # Get email from form

      User = get_user_model()  # Get the User model

      try:
          if User.objects.filter(username=username).exists(): # Check is the username is already used
            messages.error(request, f'Error creating user: Username already exists') # Display success message
            return render(request, 'users/create_user.html')
          user = User.objects.create_user(username=username, password=password, email=email)
          messages.success(request, f'User {username} created successfully!') # Display success message
          return redirect('admin:index') # Redirect to Admin page or login page, or a 'success' page
      except Exception as e: # Catch any errors
          messages.error(request, f'Error creating user: {e}') # Display error message
          return render(request, 'users/create_user.html')# Redisplay form with error
  else:
      return render(request, 'users/create_user.html') # Display form initially