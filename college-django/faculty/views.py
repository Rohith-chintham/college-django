from django.shortcuts import render, get_object_or_404
from .models import Faculty, Course

def dashboard(request):
    faculty = get_object_or_404(Faculty, id=1)  # Replace with real user logic
    courses_count = faculty.courses.count()
    return render(request, 'faculty/dashboard.html', {'faculty': faculty, 'courses_count': courses_count})

def course_list(request):
    faculty = get_object_or_404(Faculty, id=1)
    courses = faculty.courses.all()
    return render(request, 'faculty/course_list.html', {'courses': courses})

def profile(request):
    faculty = get_object_or_404(Faculty, id=1)
    return render(request, 'faculty/profile.html', {'faculty': faculty})
